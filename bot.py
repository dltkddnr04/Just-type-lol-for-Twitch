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
    if function.calc_chat_status(recent_list, 'ㅋ', 60, 10):
        chat_delay = function.continuity_check(recent_list, 'ㅋ')
        if not once_check and chat_delay >= chat_sensitive:
            once_check = True
            time.sleep(random.random())
            sending_message = 'ㅋ' * math.ceil(function.get_average(recent_list, 'ㅋ'))
            #irc_connect.send_message(client_socket, channel, sending_message)
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'type lol ', sending_message)
    else:
        once_check = False

    #print(chat_delay)