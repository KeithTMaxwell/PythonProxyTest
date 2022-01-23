from UDPSocket import UDPSocket


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


if __name__ == "__main__":
    server_ip = '192.168.28.126'
    server_port = 12345
    server = UDPServer(server_ip, server_port)
    server.test_func()
