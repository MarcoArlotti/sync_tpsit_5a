import socket



class client:
    def __init__(self,ip,porta):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect(ip, porta)
    
    def send():
        
    def recive():
        # https://www.programmareinpython.it/video-corso-python-intermedio/06-il-modulo-socket-introduzione/