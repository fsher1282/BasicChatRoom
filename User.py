import socket
import threading


nickname = input('Enter chat name here: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 34451))


def user_receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            print(message)
        except:
            print('Something broke idk...')
            print('Please touch grass')
            client.close()
            break

def write_message():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=user_receive)
receive_thread.start()

write_thread = threading.Thread(target=write_message)
write_thread.start()



