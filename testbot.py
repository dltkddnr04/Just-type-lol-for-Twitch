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

client_socket = irc_connect.set_socket(token, channel, nickname)
print('ready')

once_check = False
chat_delay = 0
chat_sensitive = 2

while True:
    data = irc_connect.recive_data(client_socket)
    data = irc_connect.process_data(data)
    if data == 'PING':
        irc_connect.pong(client_socket)
    elif data != None:
        emoji_count = function.get_emoji_count(data[2])
        #print('chat: {}, emoji: {}'.format(data[2], emoji_count))
        print(emoji_count)
        