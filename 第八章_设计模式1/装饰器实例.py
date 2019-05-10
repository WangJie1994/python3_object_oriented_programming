import socket
import gzip
from io import BytesIO


def respond(client):
    response = input("enter a value:")
    client.send(bytes(response, 'utf8'))
    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 2401))
server.listen(1)


class LogSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        print('send {} to {}'.format(data, self.socket.getpeername()[0]))
        self.socket.send(data)

    def close(self):
        self.socket.close()


class GzipSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self, data):
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode='w')
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())

    def close(self):
        self.socket.close()


try:
    while True:
        client, addr = server.accept()
        if log_send:
            client = LogSocket(client)
        if client.getpeername()[0] in compress_hosts:
            client = GzipSocket(client)
        respond(client)
finally:
    server.close()
