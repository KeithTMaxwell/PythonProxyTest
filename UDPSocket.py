import socket


class UDPSocket:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # only server need to bind ip port
    def bind_ip_port(self, ip, port):
        try:
            ip_port = (ip, port)
            self.socket.bind(ip_port)
            return True
        except WindowsError as error:
            print('socket bind ip failed: ' + str(error))
            return False

    # can be executed without binding ip port
    def send_to(self, msg, ip, port):
        dist_ip_port = (ip, port)
        try:
            self.socket.sendto(msg.encode(), dist_ip_port)
            return True
        except WindowsError as error:
            print('send message failed: ' + str(error))
            return False

    # can be executed without binding ip port
    # read receive buffer, an UDP package max_len is 8192
    def receive(self, max_buffer_len=1024):
        try:
            msg, (ip, port) = self.socket.recvfrom(max_buffer_len)
            return str(msg.decode()), ip, port
        except WindowsError as error:
            print('receiving error: ' + str(error))
            return None, None, None

