#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/10 15:42
# @author  : zhoubin
from flask import Blueprint

main = Blueprint('main', __name__)
from . import views
