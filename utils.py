#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    author: xiaobai
    project: spring boot client
    describe: get spring cloud config
"""


import requests
import json
import re
from os import getenv
from string import Template
from flask import make_response
from flask import jsonify

class MyTemplate(Template):
    '''
    继承 string.Template, 添加匹配 . 的支持
    原正则: {(?P<braced>[_a-z][_a-z0-9\-]*)}
    修改后: {(?P<braced>[_a-z][_.a-z0-9\-]*)}
    '''
    pattern = r'''
    \$(?:
      (?P<escaped>\$) |   # Escape sequence of two delimiters
      (?P<named>[_a-z][_a-z0-9]*)      |   # delimiter and a Python identifier
      {(?P<braced>[_a-z][_.a-z0-9\-]*)}   |   # delimiter and a braced identifier
      (?P<invalid>)              # Other ill-formed delimiter exprs
    )
    '''

def EnableAutoConfiguration(app, name, profile, label, config_server):
        '''
        从 spring-cloud configserver 获取配置文件, 并加入应用配置中 app.config
        '''
	properties = requests.get('/'.join((config_server, name, profile, label))).json()
        app_env = EnvInit(properties)
	app.config.update(app_env)
	app.config['__spring_config_keys'] = app_env.keys()
	@app.route("/env")
	def env():
		resp = dict([(k, app.config[k]) for k in app.config['__spring_config_keys']])
		return jsonify(resp)

def EnvInit(property):
    '''
    将从 spring-cloud configserver 获取到的配置文件进行处理, 合并多个配置文件
    '''
    if not isinstance(property, dict):
        return None
    app_env = dict()
    for profile in property["propertySources"]:
        app_env = dict(app_env, **profile["source"])
    template_string = json.dumps(property)
    app_env = PropertyRender(template_string, app_env)
    return app_env

def PropertyRender(template_string, data, count=3):
    '''
    将引用变量的配置进行渲染, 输出最终配置
    正则部分参考 string.Template
    '''
    pattern = r'\${(?P<braced>[_a-z][_a-z0-9.]*)}'
    prog = re.compile(pattern, re.IGNORECASE | re.VERBOSE)
    loop_count = 1
    while prog.search(template_string):
        template_string = MyTemplate(template_string).safe_substitute(data)
        if loop_count > count: break
        loop_count += 1
    app_env = json.loads(template_string)
    return app_env
