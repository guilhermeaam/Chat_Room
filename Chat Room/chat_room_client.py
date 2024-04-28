import threading
import socket
from _thread import *

nickname = input('Diga seu nickname ')
host = '127.0.0.1'
port = 54321

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Aguardando conexão com o servidor...')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

def client_receive():
    while True:
        try:
            message = ClientSocket.recv(1024).decode('utf-8')
            if message == 'Você se conectou ao chatroom':
                ClientSocket.send(nickname.encode('utf-8'))
            if message== 'sair':
                print('Desconectado!')
                ClientSocket.close()
                break
            else:
                print(message)
        except:
            print('Error!')
            ClientSocket.close()
            break


def client_send():
    while True:
        message = input('')
        ClientSocket.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
