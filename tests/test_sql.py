#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @create  : 2017/12/13 14:19
# @author  : zhoubin

import unittest
import asyncio


class SQLTESTCase(unittest.TestCase):
    """
    sqlhelper单元测试用例
    """

    def setUp(self):
        # self.loop = asyncio.new_event_loop()
        self.loop = asyncio.get_event_loop_policy().new_event_loop()
        asyncio.set_event_loop(None)
        print('this is setup')


