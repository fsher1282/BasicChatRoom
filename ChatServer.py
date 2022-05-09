import socket
import threading

host = '127.0.0.1'  # localhost
port = 34451

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
chatnames = []


# Send message to all connected to server
def broadcast_all(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast_all(message)
        except:
            index = client.index(client)
            clients.remove(index)
            client.close()
            chatname = chatnames[index]
            broadcast_all(f'{chatname} left the chat'.encode('ascii'))
            chatnames.remove(index)
            break


def receive():
    while True:
        client, address = server.accept()
        print('Connected to ' + str(address))

        client.send('NICK'.encode('ascii'))
        chatname = client.recv(1024).decode('ascii')
        chatnames.append(chatname)
        clients.append(client)

        print('Name of client is: ' + chatname)

        broadcast_all(f'{chatname} joined the chat'.encode('ascii'))
        client.send('\nConnected to server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print('We good...')
receive()
print('I think')
