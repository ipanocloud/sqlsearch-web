#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/10 15:09
# @author  : zhoubin

from flask import render_template, current_app
from . import main


@main.route('/query')
def query_result():
    limit = current_app.config['SQLSEARCH_COMMENTS_PER_PAGE']
    dbConfig = current_app.config.get('DBCONFIG')
    return "select * from all"


@main.route('/index')
def query_index():
    return render_template('query/index.html')


@main.route('/')
def index():
    return "Hello Python"
