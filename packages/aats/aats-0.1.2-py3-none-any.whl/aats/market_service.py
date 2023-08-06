import socket
import json
import time
import datetime
from enum import Enum
from struct import pack, unpack


class NetWorkType(Enum):
    P2P = 1
    BROADCAST = 2
    MULTIBROAD = 3


class MarketService(object):
    def __init__(self, sym_cid_map):
        self.sym_cid_map = sym_cid_map
        self.cid_sym_map = {v: k for k, v in self.sym_cid_map.items()}
        # self.host = socket.gethostname()
        self.ip_port = None
        self.send_to_ip = None
        self.send_to_port = None
        self.symbols = []
        self.exchanges = []        
        self.exchanges_table=[]
        self.l2_change = False
        return

    def open_l2_data(self):
        self.l2_change = True

    def set_control_server(self, ip, port):
        self.control_ip = ip
        self.control_port = port

    def set_network_cfg(self, ip, port, send_type, netcard_name=''):
        self.send_to_ip = ip
        self.send_to_port = port
        self.send_type = send_type
        self.netcard_name = netcard_name

    def add_exchange(self, exchange, market_data_type='',market_data_channel=''):
        for ex in self.exchanges_table:
            if ex == exchange:
                return
        
        self.exchanges_table.append(exchange)
        if market_data_type == '':
            self.exchanges.append(
                {'exchange': exchange}
            )
        else:
            self.exchanges.append(
                {'exchange': exchange,"market_data_type": market_data_type,"market_data_channel": market_data_channel}
            )  

    def add_listen_symbol(self, symbol, exchange, book_level):
        cid = self.cid_sym_map[symbol+'.'+exchange]
        self.symbols.append(
            {'cid': cid, 'port': [symbol, exchange], 'book_level': book_level})
      

    def send_msg(self, msg, socket):
        message_len = len(msg)
        message_format = '>i' + str(message_len) + 's'
        send_message = pack(message_format, message_len, msg.encode('utf-8'))
        socket.send(send_message)

    def recv_msg(self):
        data = self.server_socket.recv(1024)
        self.server_socket.close()
        if len(data) <= 0:
            return ''

        # print(data)
        length = unpack('i', data[:4])[0]
        resp = json.loads(data[4:length+4].decode('utf-8'))
        # print(resp)
        return resp        

    def run(self):
        self.server_socket = socket.socket()
        self.server_socket.connect((self.control_ip, self.control_port))
        # request new instance and wait for pin and instance port
        msg = {"type": "new_market_instance",
                "cfg": {
                    "instance": {"license_id": "TRAIL001", "license_key": "apifiny123456", "log_path": "/data/cc/log/md_server", "log_level": 1, "name": "trader_service", "l2_change": self.l2_change}, 
                    "servers": {"redis_server": "127.0.0.1"}, 
                    "network": {"send_type": self.send_type.value , "network_card_name": self.netcard_name, "local_port": self.send_to_port, "send_to_ip": self.send_to_ip, "send_to_port": self.send_to_port}, 
                    "exchanges":self.exchanges, 
                    "symbols": self.symbols}
                    }
        # print(msg)
        msg = json.dumps(msg)
        self.send_msg(msg, self.server_socket)

        resp = self.recv_msg()
        if len(resp) <= 0:
           return
        print(resp)
        resp_type = resp.get("type")

        if resp_type == 'market_instance':
            self._pid = resp.get("data").get("pid")

        while True:
            state = self.check_process()
            # print(state)
            if state == 'ok':
                print("require_market_data_state: ok")
                break
            elif state == 'bind error!':
                print("Failed to start the market data server. Please try another port.")
                break
            else:
                time.sleep(1)
        

    def check_process(self):
        self.server_socket = socket.socket()
        self.server_socket.connect((self.control_ip, self.control_port))
        # request new instance and wait for pin and instance port

        msg = {"type": "require_market_data_state", "pid": self._pid}
        # print(msg)

        msg = json.dumps(msg)
        self.send_msg(msg,self.server_socket)

        resp = self.recv_msg()
        if len(resp) <= 0:
            return "unknown"
        print(resp)
        resp_type = resp.get("type")
        result = resp.get("result")
        if resp_type == "require_market_data_state":
            if resp.get("data"):
                return resp.get("data").get("output")
            else:
                return None
        return "unknown"

        
