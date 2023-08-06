##############################################
#               Demo strategy                #
##############################################
import time
import sys
sys.path.insert(0,'/home/zhangtian/dev/algo-client-api/Python/src/')
from aats.trade_service import TradeService
from aats.base_strategy import BaseStrategy
from aats.base.order import Order
from aats.base.const import OrderType, Side
from aats.market_service import NetWorkType

# control_server_ip = "127.0.0.1"
control_server_ip = "54.199.162.238"

sym_cid_map = {
    1001: "BTCUSDT.BINANCE",
    1002: "ETHUSDT.BINANCE",
    1003: "DOGEUSDT.BINANCE"
    }

## define your strategy
class SimpleTakerStrategy(BaseStrategy):
    """
    Naive Taker Strategy: place IOC buy order on fixed time interval
    """
    def __init__(self, msecs):
        self.msecs = msecs
        self.start_time = time.time_ns()
        self.next_fire_time = self.start_time + self.msecs * 1e6

    def onNotify(self, no_type):
        current_time = time.time_ns()
        if current_time > self.next_fire_time:
            self.next_fire_time = current_time + self.msecs * 1e6
            self.onTimer()

    def onTimer(self):
        qpx = self.si[self.trade_cid].ask_px
        size = 0.001
        new_order = Order(exchange=self.trade_exchange, 
                            symbol=self.trade_symbol, 
                            price=qpx, 
                            size=size, 
                            side=Side.BUY.value, 
                            tif=OrderType.IOC.value)
        self.send_order(new_order)
        print(f"send order {new_order}")




# init trade engine
trade_service = TradeService(sym_cid_map)

# setup public config
trade_service.set_md_connection(ip=control_server_ip, port=15031, send_type = NetWorkType.P2P)  # default setting
trade_service.add_md_symbol(symbol='BTCUSDT', exchange='BINANCE', level_num=5)
# trade_service.add_md_symbol(symbol='DOGEUSDT', exchange='BINANCE')

# setup private config
trade_service.set_ts_connection(ip=control_server_ip, port=8060)  # default setting
trade_service.config_exchange(exchange='BINANCE', trade_type='sandbox')
trade_service.set_apikey(exchange="BINANCE", 
                        key="02SvhZEYG1p92JWdekP75XQKayqfLxmjHWNEfWU1KrCPjJ5xrLcOU1YHZ5SUBVFA", 
                        secret="iKnZvDKMGQuEINhjDX8gbIVJDLl48fV6GFLL5gcFT8Sfj9yxGrnP7uFm7AAVWeFP", 
                        password="",
                        subaccount="")
trade_service.set_fee('BINANCE', 0.0003, 0)
trade_service.add_trade_symbol(symbol='BTCUSDT', exchange='BINANCE', level_num=5)

# setup your strategy
# my_strategy = SimpleMakerStrategy()
my_strategy = SimpleTakerStrategy(msecs=10000)
trade_service.add_strategy(my_strategy)

# start run
try:
    trade_service.run()
except KeyboardInterrupt as err:
    print("close strategy and close open orders")
    my_strategy.close()
    time.sleep(1)
    trade_service.stop()
    print("trade server closed")    