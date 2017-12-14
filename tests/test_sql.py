#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/13 14:19
# @author  : zhoubin

import asyncio
import unittest
import json

from flask import current_app

from app import sqlhelper, create_app


class SQLTESTCase(unittest.TestCase):
    """
    sqlhelper单元测试用例
    """

    def setUp(self):
        self.app = create_app('DEV')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.loop = asyncio.get_event_loop_policy().new_event_loop()
        asyncio.set_event_loop(None)
        print('\r\nthis is setup')

    def tearDown(self):
        self.app_context.pop()
        # self.loop.close()

    def test_create_pool(self):
        """
        测试创建MySQL连接池
        单元测试测试异步方法 https://stackoverflow.com/questions/23033939/how-to-test-python-3-4-asyncio-code
        :return:
        """
        print('test_createpool start....\r\n')
        dbconfig = current_app.config.get('DBCONFIG')['db0']
        self.__pool = self.loop.run_until_complete(
            sqlhelper.create_pool(self.loop, host=dbconfig['host'], user=dbconfig['user'],
                                  password=dbconfig['password'],
                                  database=dbconfig['database']))
        print('test_createpool end....\r\n')
        result = self.loop.run_until_complete(sqlhelper.select('select * from USER WHERE id < %s', '10', 20))
        print("\r\n"+json.dumps(result))

    def test_select(self):
        """
        测试查询语句
        :return:
        """


if __name__ == '__main__':
    unittest.main()
