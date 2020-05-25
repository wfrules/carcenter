from socket import *
class Car:
    def __init__(self):
        pass

    def sendCmd(self,cmd):
        tcp_client_socket = socket(AF_INET, SOCK_STREAM)
        tcp_client_socket.connect(("192.168.1.130", 80))
        tcp_client_socket.send(cmd.encode())
        recv_data = tcp_client_socket.recv(1024)
        if recv_data:
            sRet = "返回的消息为:", recv_data.decode('gbk')
        else:
            sRet = "对方已离线。。"
        tcp_client_socket.close()
        return sRet