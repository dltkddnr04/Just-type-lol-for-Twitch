import socket
import datetime
from emoji import demojize

def set_socket(access_token, channel_name, nickname):
    token = 'oauth:' + access_token
    channel = '#' + channel_name
    server = 'irc.chat.twitch.tv'
    port = 6667

    client_socket = socket.socket()
    client_socket.connect((server, port))
    client_socket.send(f"PASS {token}\n".encode('utf-8'))
    client_socket.send(f"NICK {nickname}\n".encode('utf-8'))
    client_socket.send(f"JOIN {channel}\n".encode('utf-8'))

    return client_socket

def process_data(data):
    try:
        if data.startswith('PING'):
            return "PING"
        elif data != None:
            data = data.replace('\r\n', '')
            recived_time = datetime.datetime.now()
            recived_user_name = data.split('!')[0][1:]
            recived_message = data.split('PRIVMSG')[1].split(':')[-1]
            recived_message = demojize(recived_message)
            # make it to list
            return [recived_time, recived_user_name, recived_message]
    except:
        return None

def recive_data(client_socket):
    data = client_socket.recv(1024).decode('utf-8')
    return data

def send_message(client_socket, channel, data):
    client_socket.send(f"PRIVMSG #{channel} :{data}\n".encode('utf-8'))
    return

def pong(client_socket):
    client_socket.send("PONG\n".encode('utf-8'))