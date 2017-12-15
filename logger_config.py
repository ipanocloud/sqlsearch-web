#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/14 19:15
# @author  : zhoubin

import os
import logging
from logging import config

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

LOGGING_CONFIG = {
    'formatters': {
        'brief': {
            'format': '[%(asctime)s][%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'common': {
            'format': '[%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %A %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'common',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'brief',
            'filename': os.path.join(BASE_DIR, 'logs', 'app.log'),
            'maxBytes': 5 * 1024 * 1024,
            'backupCount': 10
        },
        'timedRotatingFormatter': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'common',
            'filename': os.path.join(BASE_DIR, 'logs', 'app.log'),
            'when': 'D',
            'interval': 1,
            'backupCount': 10
        }
    },
    'loggers': {
        'main': {
            'propagate': False,
            'handlers': ['console', 'file'],
            'level': 'INFO'
        },
        'root': {
            'propagate': False,
            'handlers': ['console', 'timedRotatingFormatter'],
            'level': 'INFO'
        }
    },
    'version': 1
}


def get_logger():
    """
    获取日志记录器实例
    :return:
    """
    logsdir = BASE_DIR + '\logs'
    if not os.path.exists(logsdir):
        os.mkdir(logsdir)
    logging.config.dictConfig(LOGGING_CONFIG)
    log = logging.getLogger('root')
    return log
