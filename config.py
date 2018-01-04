#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/9 21:37
# @author  : zhoubin

import os
import logger_config

basedir = os.path.abspath(os.path.dirname(__file__))
logger = logger_config.get_logger()


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
    DBCONFIG = {
        'db0': {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'pwd@123',
            'database': 'jt_cloudstitch'
        },
        'db1': {
            'host': '127.0.0.1'
        }
    }


class ProductionConfig(Config):
    DEBUG = False


config = {
    'DEV': DevelopmentConfig,
    'TEST': TestingConfig,
    'PRD': ProductionConfig,

    'default': DevelopmentConfig
}
