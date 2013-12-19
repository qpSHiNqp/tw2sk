#!/usr/bin/env python
# -*- coding: utf-8 -*-
# config.py
#
# Config loader

import yaml

def load(conffile):
    string = open(conffile).read()
    string = string.decode('utf8')
    return yaml.load(string)
