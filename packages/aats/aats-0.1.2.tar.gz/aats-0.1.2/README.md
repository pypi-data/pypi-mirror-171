# Apifiny Algo Trading System

AATS is a light weight trading system with low-latency and high-scalability for Live trading on multi-crypto exchanges. 

## Key Features
* Light weight: you only need to take care of your strategy component and you can trade alive!
* Low latency: the low-level system is optimizied by C++, such as exchange connectivity, order book management and order placement
* High flexibility: with raw tick data and quote data, you can freely build samplers, pricing models, variables and signals on your own into your strategy
* Distributed broadcast: You can only start one market instance and connect to multiple trading instances

## Quick Start
This quick start gives you all the steps that you need to do before start trading.

#### Install docker
Please download and install Docker CE or Docker Desktop for your computer/server if it isn't installed:

- [Mac](https://docs.docker.com/docker-for-mac/install/)
- [Windows](https://docs.docker.com/docker-for-windows/install/)
- [Linux](https://docs.docker.com/install/)

Get and run the Algo SDK docker image using the following command:
```
docker run -it apifinyalgo/algo-sdk:1.1.0
```
his step will automatically run control server which will be used to start market/trading instance later. Depending on system, you may need to run this with sudo.

TBA: how to check if it is running, i.e. ps command
#### Install aats package
```
# install stable version from pip (support python version >=3.7)
pip install aats (TBA: currently pip install -i https://test.pypi.org/simple/ aats)

# clone the repository with latest version
git clone http://git.ddesk.io/exone-plus/algo-client-api.git (TBA: replace with public repo link)
```

#### Maintain your unique cid symbol mapping table 
It requires to be consistent in both market engine and trade engine
```
sym_cid_map = {
    1001: "BTCUSDT.BINANCE",
    1002: "ETHUSDT.BINANCE",
    1003: "DOGEUSDT.BINANCE",
    1004: "BTCUSDTSWAP.BINANCE_SWAP"
    }
```

#### Start market instance to listen subscribed symbols and exchanges
TBA: change the below to one command line to start market instance
```
from aats.market_engine import MarketEngine

# start market engine
mkt_engine = MarketEngine(sym_cid_map)
mkt_engine.set_control_server(6000)  # default control server port
mkt_engine.set_multicast_cfg('239.0.0.4', 4141)
# mkt_engine.add_listen_symbol('BTCUSDT', 'BINANCE', 5)
# mkt_engine.add_listen_symbol('ETHUSDT', 'BINANCE', 5)
mkt_engine.add_listen_symbol('DOGEUSDT', 'BINANCE', 5)
mkt_engine.add_listen_symbol('BTCUSDTSWAP', 'BINANCE_SWAP', 5)
mkt_engine.run()

```
Once console returns the following message, it means market instance is running successfully
```
{'result': 'ok', 'type': 'market_instance'}
```

#### Write your strategy and ready to trade
In the examples folder, we provide two sample strategies and demo_main.py script which illustrates how to setup config and run strategy

- SimpleTakerStrategy: it is a naive taker strategy, place order on a fixed time interval
- SimpleMakerStrategy: it is a bit complicated maker strategy with order management system

```
##############################################
#               Demo strategy                #
##############################################
import time
from aats.trade_engine import TradeEngine
from simple_maker_strategy import SimpleMakerStrategy
from simple_taker_strategy import SimpleTakerStrategy



sym_cid_map = {
    1001: "BTCUSDT.BINANCE",
    1002: "DOGEUSDT.BINANCE"
    }

# init trade engine
trade_engine = TradeEngine(sym_cid_map)

# setup public config
trade_engine.set_md_multicast_cfg(send_to_ip='239.0.0.3', send_to_port=4141)
trade_engine.add_md_symbol(symbol='BTCUSDT', exchange='BINANCE')
# trade_engine.add_md_symbol(symbol='DOGEUSDT', exchange='BINANCE')

# setup private config
trade_engine.set_control_server(server_port=6000)
trade_engine.config_exchange(exchange='BINANCE', trade_type='sandbox')
trade_engine.set_apikey(exchange="BINANCE", 
                        key="02SvhZEYG1p92JWdekP75XQKayqfLxmjHWNEfWU1KrCPjJ5xrLcOU1YHZ5SUBVFA", 
                        secret="iKnZvDKMGQuEINhjDX8gbIVJDLl48fV6GFLL5gcFT8Sfj9yxGrnP7uFm7AAVWeFP", 
                        password="",
                        subaccount="")
trade_engine.set_fee('BINANCE', 0.0003, 0)
trade_engine.add_trade_symbol(symbol='BTCUSDT', exchange='BINANCE')

# setup your strategy
# my_strategy = SimpleMakerStrategy()
my_strategy = SimpleTakerStrategy(msecs=10000)
trade_engine.add_strategy(my_strategy)

# start run
try:
    trade_engine.run()
except KeyboardInterrupt as err:
    # trade_engine.stop()
    print("close strategy and close open orders")
    # trade_engine.manager.stop()
    my_strategy.close()
    time.sleep(1)
    print("trade closed")    
```