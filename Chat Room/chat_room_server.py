import threading 
import socket
from _thread import *

host = '127.0.0.1'
port = 54321
SocketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    SocketServer.bind((host, port))
except socket.error as e:
    print(str(e))

print(f'Servidor está na escuta na porta ==> {port}..')
SocketServer.listen()

clients = []
aliases = []

def broadcast(sock, message):
    for client in clients:
        if client != SocketServer and client != sock:
            try:
                client.send(message)
            except:
                client.close()

def client_handler(client):
    client.send(str.encode('Bem-vindo ao servidor! Digite sair para deixar o chat.'))
    while True:
        message = client.recv(1024)
        data = message.decode('utf-8')
        index = clients.index(client)
        nickname = aliases[index]
        if data == 'sair':
            break
        else:
            message1= (f'{nickname}: '.encode('utf-8'))
            message1= message1 + message
            broadcast(client, message1)

    client.send('sair'.encode('utf-8'))
    clients.remove(client)
    client.close()
    broadcast(client,f'{nickname}  deixou  chat'.encode('utf-8'))
    print(f'{nickname}  deixou  chat'.encode('utf-8'))
    aliases.remove(nickname)

def accept_connection():
    while True:
        client, address = SocketServer.accept()
        print(f'Conexão com {str(address)} foi estabelecida.')
        client.send('Você se conectou ao chatroom'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print((f'O nickname do cliente e {alias}.').encode('utf-8'))
        broadcast(client,(f'{alias} se conectou ao chat').encode('utf-8'))
        thread = threading.Thread(target=client_handler, args=(client,))
        thread.start()

accept_connection()