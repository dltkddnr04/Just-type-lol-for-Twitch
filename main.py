import irc.bot
import irc.strings
import datetime

chat_log = []

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

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
        
        print('[{}] {}: {}'.format(current_chat[0], current_chat[1], current_chat[2]))

def main():
    # account auth info
    username = ''
    client_id = ''
    token = ''

    # channel to join
    channel = ''

    bot = TwitchBot(username, client_id, token, channel)
    bot.start()

if __name__ == '__main__':
    main()