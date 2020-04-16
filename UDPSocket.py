import socket


class UDPSocket:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # only server needs to bind ip port
    # input     ip: string, ipv4
    #           port: int
    # output    True/False: success/fail
    def bind_ip_port(self, ip, port):
        try:
            ip_port = (ip, port)
            self.socket.bind(ip_port)
            return True
        except WindowsError as error:
            print('socket bind ip failed: ' + str(error))
            return False

    # send a message to specified ip:port
    # input     msg: string
    #           ip: string, destination ip
    #           port: int, destination port
    # output    True/False: success/fail
    def send_to(self, msg, ip, port):
        ip_port = (ip, port)
        try:
            self.socket.sendto(msg.encode(), ip_port)
            return True
        except WindowsError as error:
            print('send message failed: ' + str(error))
            return False

    # read socket buffer
    # input     read_bytes: read bytes from buffer
    # output    message: string, received message
    #           ip: string, source ip
    #           port: int, source port
    def receive(self, read_bytes=1024):
        try:
            msg, (ip, port) = self.socket.recvfrom(read_bytes)
            return str(msg.decode()), ip, port
        except WindowsError as error:
            print('receiving error: ' + str(error))
            return None, None, None

