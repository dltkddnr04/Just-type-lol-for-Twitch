import datetime
import random
import math

watchlist = ['ㅋ', 'ㄹㅇㅋㅋ', 'ㅎㄷㄷ']

def count_alphabet(data):
    # watchlist에 있는 단어들의 수를 각각 세서 리턴하는 함수
    count_list = []
    for word in watchlist:
        count_list.append(data.count(word))

    return count_list

def get_average_data(list, time1, time2, alphabet):
    average_1 = 0
    average_2 = 0
    for i in range(len(list)):
        if (datetime.datetime.now() - list[i][0]).seconds < time1:
            average_1 += list[i][1].count(alphabet)
        if (datetime.datetime.now() - list[i][0]).seconds < time2:
            average_2 += list[i][1].count(alphabet)

    return average_1/(time1/time2), average_2

def get_alphabet_average(list, alphabet):
    average = 0
    for i in range(len(list)):
        average += list[i][1].count(alphabet)

    return average/len(list)

def plus_minus(number):
    useless_value = math.ceil(number * 0.2)
    return number + random.randint(-useless_value, useless_value)