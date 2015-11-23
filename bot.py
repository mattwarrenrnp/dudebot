import time
import os

from slackclient import SlackClient

from chatterbot import ChatBot
chatbot = ChatBot("dude")
chatbot.train("biglebowskiscript")

token = os.environ['SLACK_TOKEN']

sc = SlackClient(token)
if sc.rtm_connect():
    my_user_id = sc.server.users.find(sc.server.username).id
    while True:
        messages = sc.rtm_read()
        try:
            for message in messages:
                if message['type'] == 'message':
                    if 'am i wrong?' in message['text'].lower():
                        sc.rtm_send_message(message['channel'], "You're not wrong <@%s>, you're just an asshole." % message['user'])
                    if 'vietnam' in message['text'].lower():
                        response = "God damn you Walter! You f***in' asshole! Everything's a f***in' travesty with you, man! And what was all that shit about Vietnam? What the FUCK, has anything got to do with Vietnam? What the f*** are you talking about?"
                        sc.rtm_send_message(message['channel'], response)
                    if my_user_id in message['text']:
                        response = chatbot.get_response(message['text'])
                        sc.rtm_send_message(message['channel'], response)
        except:
            pass
        time.sleep(1)
else:
    "Connection Failed, invalid token?"
