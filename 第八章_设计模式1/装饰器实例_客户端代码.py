import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 2401))
print('recerved: {}'.format(client.recv(1024)))
client.close()
