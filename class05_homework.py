#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 12:45 下午
# @Author  : Bais
# @File    : class05_homework.py


"""
实现布尔类型描述器

"""


class BoolFiled(object):

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, bool):
            self.value = value
        else:
            raise TypeError("need a bool")

    def __delete__(self, instance):
        self.value = None


class Model(object):
    a = BoolFiled()


m = Model()
m.age = [8888]
print(m.age)
