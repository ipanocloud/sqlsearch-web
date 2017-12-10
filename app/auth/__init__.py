#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/10 20:33
# @author  : zhoubin

from flask import Blueprint

auth = Blueprint('auth', __name__)
from . import views
