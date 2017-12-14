#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/13 13:59
# @author  : zhoubin

import aiomysql
import asyncio
from config import logger


@asyncio.coroutine
def create_pool(loop, **kw):
    """
    创建mysql数据库连接池
    :param loop:
    :param kw:
    :return:
    """
    logger.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['database'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )
    logger.info('connection poo success done...')
    return __pool


@asyncio.coroutine
def select(sql, args, size=None):
    """
    封装select查询语句
    :param sql: select查询sql
    :param args: 参数
    :param size: 查询条数
    :return:
    """
    logger.info(sql, args)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logger.info('rows returned: %s' % len(rs))
        return rs
