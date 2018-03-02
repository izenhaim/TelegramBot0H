from telepot import *
from telepot.loop import *
from telepot.namedtuple import *
from pprint import pprint

# initialize bot
bot = Bot('309863224:AAEYLFj19B-GNP-DHWYhkS4b2QrTef9kRbQ')
# ---------------------------------------------------------

# apon resiving messege do:

def handle(msg):
    pprint(msg)
    bot.sendMessage(msg['from']['id'] , msg['text'])

#----------------------------------------------------------





# get messeges and handle:
MessageLoop(bot, handle).run_as_thread()

#keep servre alive
while True:
    time.sleep(10)