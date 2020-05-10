from UDPSocket import UDPSocket

server_ip = '192.168.124.13'
server_port = 12345


class UDPServer(UDPSocket):
    def __init__(self, ip, port):
        UDPSocket.__init__(self)
        self.bind_ip_port(ip, port)
        self.is_start = True

    def test_func(self):
        while self.is_start:
            msg, ip, port = self.receive(8192)
            print('message from ' + ip + ':' + str(port) + ' : ' + msg)
            self.send_to(msg, ip, port)


server = UDPServer('192.168.124.13', 12345)
server.test_func()
