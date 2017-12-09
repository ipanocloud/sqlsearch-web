#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/9 21:37
# @author  : zhoubin

import os

basedir = os.path.abspath(os.path.dirname(__file__))


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


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
