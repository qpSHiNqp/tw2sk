#!/usr/bin/env python
# -*- coidng: utf-8 -*-

from tweepy.streaming import StreamListener
from tweepy import TweepError
from datetime import timedelta
from lib.utils import twitter
import lib.config
import Skype4Py

skype = None
maps = None
chatList = []
chat = None

class MyListener(StreamListener):
    def on_status(self, status):
        if status.author.screen_name in maps:
            #chat = skype.CreateChatWith(maps[status.author.screen_name])
            try:
                chat.SendMessage(status.text)
            except Skype4Py.errors.SkypeError, e:
                logging.info(u"Error while chatting; {error}".format(error=e.message))

            print u"T2S!"
        status.created_at += timedelta(hours=9)
        print(u"{text}".format(text=status.text))
        print(u"{name}({screen}) {created} via {src}\n".format(
            name=status.author.name,
            screen=status.author.screen_name,
            created=status.created_at,
            src=status.source))

if __name__ == '__main__':
    skype = Skype4Py.Skype()
    skype.Attach()

    print u"==== Scanning chat list... ===="
    cc = skype.Chats
    while len(cc) >= 1:
        c = cc.pop()
        print c.Topic
        if c.Topic == u"elab M1":
            chat = c

    print u"==== Loading configs... ===="
    config = lib.config.load("config/tw2sk.yaml")
    maps = config['maps']
    try:
        util = twitter(config['tokens'])
        stream = util.stream(MyListener())
        print u"==== Stream initiated! ===="
        stream.userstream()
    except TweepError, e:
        logging.info(u"Error while authenticating; {error}".format(error=e.message))
