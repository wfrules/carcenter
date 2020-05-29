from socket import *
class Car:
    _socket = None
    def __init__(self):
        pass

    def sendCmd(self,cmd):
        self._socket = socket(AF_INET, SOCK_STREAM)
        self._socket.connect(("192.168.1.130", 80))
        self._socket.send(cmd.encode())
        recv_data = self._socket.recv(1024)
        if recv_data:
            sRet = recv_data.decode('gbk')
        else:
            sRet = "对方已离线。。"
        self._socket.close()
        return sRet