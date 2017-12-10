#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/10 15:09
# @author  : zhoubin

from flask import render_template, redirect, request
from . import main


@main.route('/query')
def query_result():
    return "select * from all"


@main.route('/index')
def query_index():
    return render_template('query/index.html')
