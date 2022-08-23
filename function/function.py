import datetime

def count_alphabet(data, alphabet):
    counted_alphabet = data.count(alphabet)
    chat_length = len(data)
    return counted_alphabet, chat_length

def get_recent_chat(chat_list, time):
    recent_chat = []
    for chat in chat_list:
        if chat[0] > datetime.datetime.now() - datetime.timedelta(seconds=time):
            recent_chat.append(chat)
    return recent_chat

def get_average(chat_list, alphabet):
    chat_length = 0
    chat_average = 0
    for chat in chat_list:
        # if count_alphabet(chat[2], alphabet)[0] == count_alphabet(chat[2], alphabet)[1]:
        if count_alphabet(chat[2], alphabet)[0] > 0:
            chat_length += 1
            chat_average += count_alphabet(chat[2], alphabet)[0]

    if chat_length == 0:
        return 0
    else:
        return chat_average / chat_length

def calc_chat_status(chat_list, alphabet, time1, time2):
    recent_chat1 = get_recent_chat(chat_list, time1)
    recent_chat2 = get_recent_chat(chat_list, time2)
    average1 = get_average(recent_chat1, alphabet)
    average2 = get_average(recent_chat2, alphabet)
    
    leverage = time1 / time2

    if (average1 / leverage) < average2:
        return True
    else:
        return False

def continuity_check(chat_list, alphabet):
    chat_list.reverse()
    continuity = 0
    for chat in chat_list:
        if count_alphabet(chat[2], alphabet)[0] > 0:
            continuity += 1
        else:
            break
    return continuity

def get_current_live_chat_headcount(chat_list):
    chat_user_list = []
    for chat in chat_list:
        if chat[1] not in chat_user_list:
            chat_user_list.append(chat[1])
    return len(chat_user_list)

def get_emoji_count(chat):
    emoji_candidate_list = {}
    emoji_list = {}

    chat = chat.split()
    for word in chat:
        if word not in emoji_candidate_list:
            emoji_candidate_list[word] = 1
        else:
            emoji_candidate_list[word] += 1

    for emoji_candidate in emoji_candidate_list:
        if emoji_candidate_list[emoji_candidate] > 1 and emoji_candidate.isalpha():
            emoji_list[emoji_candidate] = emoji_candidate_list[emoji_candidate]
    return  emoji_list