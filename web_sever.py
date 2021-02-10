#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 2:37 下午
# @Author  : Bais
# @File    : web_sever.py

import flask
app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'helle python'

if __name__ == '__main__':
    app.run(debug=True)