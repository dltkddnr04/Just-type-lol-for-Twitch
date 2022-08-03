import datetime

watchlist = ['ㅋ', 'ㄹㅇㅋㅋ', 'ㅎㄷㄷ']

def count_alphabet(data):
    # watchlist에 있는 단어들의 수를 각각 세서 리턴하는 함수
    count_list = []
    for word in watchlist:
        count_list.append(data.count(word))

    return count_list