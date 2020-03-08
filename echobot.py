from mattermost_bridge.mmost import MMostBot
from mattermost_bridge.mycroft import MycroftConnector
import requests
import subprocess
import threading
import time
import asyncio
import logging

####Mattermost logins
url = "chat.mycroft.ai"
mail = "mail"
pswd = "xxxxxx"
bot = "bot"

rpaid = "partneruser"
channel_name = "bottesting"

####Rasalogin
rhost = "192.168.0.77"
ruser = "rasauser"
rpswd = "xxxx"
rport = "5005"

#test msg
msg = "bist du noch da"



class EchoBot(MMostBot):
    def __init__(self):
        print("init bot")
#        self.bot = MMostBot(mail, pswd, url, tags=["@"+bot])
        self.bot = MMostBot(mail, pswd, url, tags=["@"+bot])


    def listening(self):
        print("listening")
        asyncio.set_event_loop(asyncio.new_event_loop())
        self.bot.listen()
        print("end listening")

    def handle_direct_message(self, message, sender, channel_id):
        self.send_message(channel_id, message)

    def handle_mention(self, message, sender, channel_id):
        message = "@" + sender + " " + message
        self.send_message(channel_id, message)

class mycroftrasa(MycroftConnector):
    def send_msg(self, msg):
        rpaid = msg[0]
        message = msg[1]
        mycroft = MycroftConnector(ruser, rpswd, rhost, rport, rpaid, debug=False)
        mycroft.talk_to_rasa(message)
        print(" message send")

print("init echobot_threaded")
Bot = EchoBot()
threadbot = threading.Thread(target=EchoBot().listening, args=())
threadbot.start()
threadbot.join
message = [rpaid, msg, channel_name]
print("start echobot_threaded")
rasa = mycroftrasa(ruser, rpswd, rhost, rport, rpaid)
rasa.send_msg(message)

print("after")

time.sleep (10)
#thread.start()
# show message
#thread.join()
print("end")


#EchoBot()
#msg = ["ich", "hallo", "hallo"]
