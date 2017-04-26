# -*-coding: utf-8 -*-

import time
from slackclient import SlackClient
import google
import datetime

def search(what):
   for url in google.search(what, lang='ru',stop=5):
       return (url)
def what_time(what):
    now = datetime.datetime.now()
    moment = now.time()
    return (str(moment)[:8:])


BOT_TOKEN = "token"
CHANNEL_NAME = "chanel"

hello_list = ('привет','добрый день','здарова')
time_list = ('который час','сколько время','время',)
what_list = ('что такое','кто такой','где найти')

Questions = {
    what_list : search,
    hello_list: 'Приветствую!\n',
    time_list: what_time

}





if __name__ == '__main__':
   sc = SlackClient(BOT_TOKEN)

 # присоеденяемся к слаку
   if sc.rtm_connect():
       # шлем приветсвие
       sc.rtm_send_message(CHANNEL_NAME, "Ready for Work!")
   while True:
       # читаем сообщения
       for slack_message in sc.rtm_read():
           message = slack_message.get("text")
           test = 'бот'
           user = slack_message.get("user")
           if message == None or user == None:
               continue
           elif test in message.lower().encode('utf-8'):
               for key,values in Questions.items():
                   for vars in key:
                       if vars in message.lower().encode('utf-8'):
                           print type(values)
                           if type(values) == str:
                               message_to_user = values
                               sc.rtm_send_message(CHANNEL_NAME, ("<@{}> " + message_to_user).format(user))
                           else:
                               message_to_user = values(message[6::].encode('utf-8'))
                               sc.rtm_send_message(CHANNEL_NAME, ("<@{}> "+message_to_user).format(user))

     # спим неного
       time.sleep(0.1)
