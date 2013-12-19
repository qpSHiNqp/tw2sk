#!/usr/bin/env python
# -*- coding: utf-8 -*-
# utils.py
#
# OAuth and some twitter action

import tweepy

class twitter:
  def __init__(self, tokens):
      self.auth = tweepy.OAuthHandler(
          tokens['consumer_key'],
          tokens['consumer_secret']
          )
      self.auth.set_access_token(
          tokens['access_token'],
          tokens['access_secret']
          )

  def api(self):
      return tweepy.API(self.auth)

  def stream(self, listener):
      return tweepy.Stream(self.auth, listener, secure=True)
