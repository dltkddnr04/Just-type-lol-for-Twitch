from function import (irc_connect, function)
import json
import threading
import time
import random
import math
import datetime

file = open('config.json', 'r')
data = file.read()
data = json.loads(data)
file.close()
token, channel, nickname = data['token'], data['channel'], data['nickname']
if token == '' or channel == '' or nickname == '':
    print('Please fill in the config.json file')
    exit()

def chat_recive_loop(client_socket):
    while True:
        data = irc_connect.recive_data(client_socket)
        data = irc_connect.process_data(data)
        if data == 'PING':
            irc_connect.pong(client_socket)
        elif data != None:
            chat_list.append(data)

client_socket = irc_connect.set_socket(token, channel, nickname)
print('ready')

chat_list = []
threading.Thread(target=chat_recive_loop, args=(client_socket,)).start()

once_check = False
chat_delay = 0
chat_sensitive = 2

while True:
    recent_list = function.get_recent_chat(chat_list, 60)
    user_count = function.get_current_live_chat_headcount(recent_list)
    print('user_count: {}'.format(user_count))
    time.sleep(1)