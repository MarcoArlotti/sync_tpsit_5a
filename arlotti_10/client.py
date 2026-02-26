import socket



class client:
    def __init__(self,ip,porta):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect(ip, porta)
    
    def send():
        
    def recive():