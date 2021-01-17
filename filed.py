#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 2:45 下午
# @Author  : Bais
# @File    : filed.py


class BaseFiled(object):
    pass

class CharFiled(BaseFiled):
    def __init__(self, max_lenght=20):
        self.max_lenght = max_lenght

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, str):
            if len(value) <= self.max_lenght:
                self.value = value
            else:
                raise ValueError('字符串长度应该在{}以内'.format(self.max_lenght))
        else:
            raise TypeError("need a str")

    def __delete__(self, instance):
        self.value = None


class IntFiled(BaseFiled):

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, int):
            self.value = value
        else:
            raise TypeError("need a int")

    def __delete__(self, instance):
        self.value = None

class BoolFiled(BaseFiled):

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, bool):
            self.value = value
        else:
            raise TypeError("need a bool")

    def __delete__(self, instance):
        self.value = None
