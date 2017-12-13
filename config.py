#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/9 21:37
# @author  : zhoubin

import os
import logging.config

basedir = os.path.abspath(os.path.dirname(__file__))
logsdir = basedir + '\logs'
if not os.path.exists(logsdir):
    os.mkdir(logsdir)
logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")


class Config:
    SQLSEARCH_POSTS_PER_PAGE = 20
    SQLSEARCH_FOLLOWERS_PER_PAGE = 50
    SQLSEARCH_COMMENTS_PER_PAGE = 30
    SQLSEARCH_SLOW_DB_QUERY_TIME = 0.5

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    DEBUG = True


class DevelopmentConfig(Config):
    DEBUG = True
    HJ_FUND_ORDER = 'mysql + mysqlconnector://user_fund:kGwU7c3h@192.168.36.101:3306/hj_fund_order'


class ProductionConfig(Config):
    DEBUG = False


config = {
    'DEV': DevelopmentConfig,
    'TEST': TestingConfig,
    'PRD': ProductionConfig,

    'default': DevelopmentConfig
}
