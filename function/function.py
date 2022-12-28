import requests
import json
import datetime

def get_recent_chat(chat_log, time):
    '''
        chat log: 채팅 로그
        time: 최근 몇 초간의 채팅을 가져올지
    '''

    last_minute_chat = []

    for chat in chat_log:
        chat_time = datetime.datetime.strptime(chat[0], '%Y-%m-%d %H:%M:%S')
        if (datetime.datetime.now() - chat_time).seconds <= time:
            last_minute_chat.append(chat)

    return last_minute_chat

def count_latter(chat_log, latter, mode='message'):
    '''
        chat log: 채팅 로그
        latter: 검색할 문자
        mode: all - 문자열의 개수, message(default) - 문자열이 포함된 메시지의 개수
    '''

    count = 0

    if mode == 'all':
        for chat in chat_log:
            count += chat[2].count(latter)
    elif mode == 'message':
        for chat in chat_log:
            if latter in chat[2]:
                count += 1
    
    return count

def get_latter_average(chat_log, latter):
    '''
        chat log: 채팅 로그
        latter: 검색할 문자
    '''

    count = 0
    message_count = 0

    for chat in chat_log:
        count += chat[2].count(latter)
        if latter in chat[2]:
            message_count += 1
    
    return round(count/message_count)