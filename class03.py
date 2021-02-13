#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 3:03 下午
# @Author  : Bais
# @File    : class03.py

# 上下文管理器


with open('test.txt', 'w+', encoding='utf8') as f:
    f.write('今天是周二')


# with  后面跟的是一个上下文管理器对象


class MyOpen(object):
    # 文件操作的上下文管理器类
    def __init__(self, filename, open_method, encoding='utf8'):
        self.filename = filename
        self.open_method = open_method
        self.encoding = encoding

    def __enter__(self):
        self.f = open(self.filename, self.open_method, encoding=self.encoding)
        return self.f

    # 默认4个参数   异常类型，异常值，异常追踪
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        self.f.close()


with MyOpen('test.txt', 'r') as f:
    content = f.read()
    # print(name)
    print(content)


# with MyOpen('test.txt','w') as f:
#     print(f)


# 算数运算的实现

class MyStr(object):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

    def __add__(self, other):
        # 加法
        # print('---触发了add方法----')
        # print('self',self)
        # print('other',other)
        return self.data + other.data

    def __sub__(self, other):
        return self.data.replace(other.data, '')


s1 = MyStr('111')
s2 = MyStr('222')
# print(s1 + s2)
s3 = MyStr(s1 + s2)
print(s3 - s2)
