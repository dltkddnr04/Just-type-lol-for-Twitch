import irc.bot
import irc.strings
import datetime
import threading
from function import function

# account auth info
username = 'xenos_enigma'
client_id = '5ayor8kn22hxinl6way2j1ejzi41g2'
token = 'owuggvukn7rjtct59tm6qqd9y7idgi'

chat_log = []

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

        self.repeat_check = False
        self.latter_status = False
        self.final_send_time = datetime.datetime.now()

        # create twitch irc connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        print('Connecting to {} on port {}...'.format(server, port))
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:' + token)], username, username)

    def on_welcome(self, c, e):
        print('Joining {}'.format(self.channel))
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        # get datetime, username, and message
        tags = {tag['key']: tag['value'] for tag in e.tags}
        message_time = datetime.datetime.fromtimestamp(int(tags['tmi-sent-ts'])/1000).strftime('%Y-%m-%d %H:%M:%S')
        username = e.source.split('!')[0]
        message = e.arguments[0]

        current_chat = [message_time, username, message]
        chat_log.append(current_chat)

        # make recent second now time - self.recent_second
        recent_second = datetime.datetime.now() - self.final_send_time
        recent_second = round(int(recent_second.seconds))
        recent_chat = function.get_recent_chat(chat_log, recent_second)

        average_1 = function.count_latter(function.get_recent_chat(recent_chat, 30), 'ㅋ', 'all')
        average_2 = function.count_latter(function.get_recent_chat(recent_chat, 5), 'ㅋ', 'all')
        
        
        if average_1/6 < average_2:
            self.latter_status = True
        else:
            self.latter_status = False
            self.repeat_check = False
            self.final_send_time = datetime.datetime.now()

        if self.latter_status and not self.repeat_check:
            # send message to chat
            echoing_message = "ㅋ" * function.get_latter_average(recent_chat, 'ㅋ')
            if echoing_message != "ㅋ":
                # self.connection.privmsg(self.channel, "echo " + echoing_message)
                print("echo " + echoing_message)
                self.repeat_check = True

        # print(round(average_1/6), average_2, self.latter_status, self.repeat_check)
        # print("[{}] {}: {}".format(message_time, username, message))

def main():
    bot = TwitchBot(username, client_id, token, 'bttolang')
    bot.start()

if __name__ == '__main__':
    main()