from UDPSocket import UDPSocket

server_ip = '192.168.124.13'
server_port = 12345


class UDPClient(UDPSocket):
    def __init__(self):
        UDPSocket.__init__(self)
        self.is_start = True

    def test_func(self):
        while self.is_start:
            msg = input()
            self.send_to(msg, server_ip, server_port)
            msg_r = self.receive()
            print(msg_r)


client = UDPClient()
client.test_func()

