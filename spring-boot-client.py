#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    author: xiaobai
    project: spring boot client
    describe: get spring cloud config
"""

from os import getenv
from flask import Flask
from utils import EnableAutoConfiguration

app = Flask(__name__)
EnableAutoConfiguration(app, name="Kefu", \
    profile="Webapp-47.3", label="master", \
    config_server="http://127.0.0.1:18888")

@app.route("/")
def hello_world():
    return "hello, world"

if __name__ == '__main__':
	app.debug = True
	app.run()
