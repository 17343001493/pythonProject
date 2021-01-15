#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 4:00 下午
# @Author  : Bais
# @File    : class03_homework.py

import pymysql

# 通过上下文管理器实现数据库连接

DATA_CONF = dict(
    host='localhost',
    user='root',
    password='123456',
    database='test',
    port=3306,
    charset='utf8'
)


class ConnectDB(object):

    def __init__(self, data_conf):
        # 连接数据库
        self.conn = pymysql.connect(**data_conf)
        # 创建游标对象
        self.cur = self.conn.cursor()

    def __enter__(self):
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.conn.close()


# with ConnectDB(DATA_CONF) as cur:
#     cur.execute('select * from Students')
#     print(cur.fetchone())

# 2.描述__slots__属性的作用，优化读取Excel
class Case:
    __slots__ = ['case_id', 'title', 'url', 'data', 'excepted']

    def __init__(self):
        self.case_id = None
        self.title = None
        self.url = None
        self.data = None
        self.excepted = None

# 3.面向对象的三大特征，多态是什么
# 4.私有属性怎么定义，不同的定义方式有什么区别
