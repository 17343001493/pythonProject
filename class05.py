#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 3:47 下午
# @Author  : Bais
# @File    : class05.py

"""
1.自定义属性访问
2.描述器
3.ORM模型
 O(objects)： 类和对象
 R(relations)： 关系，关系数据库中的表格
 M(mapping)： 映射
"""


class Test:
    def __init__(self):
        self.age = 18

    # def __getattr__(self, item):
    #     # 当我们访问属性的时候，如果属性不存在（出现attrerror），该方法会被触发
    #     print('-----这个是getattr方法-----')
    #     # object.__getattribute__(self, item)
    #     return 100

    # def __getattribute__(self, item):
    #     # 访问属性的时候，第一时间触发该方法查找属性
    #     print('这个是__getarrtbute__')
    #     # return 999
    #     return super().__getattribute__(item)

    # def __setattr__(self, key, value):
    #     # 这个方法在给对象设置属性的时候回触发
    #     if key == 'age':
    #         super().__setattr__(key, 18)
    #     else:
    #         print('设置属性的时候回触发----')
    #         super().__setattr__(key, value)

    def __delattr__(self, item):
        # 这个方法在删除属性的时候会被触发
        if item == 'name':
            pass
        else:
            print('---delattr被调用---')
            return super().__delattr__(item)


t = Test()
t.name = 10
t.age = 18
del t.name


# del t.age
# print(t.name)
# print(t.age)


class Filed(object):
    """
    一个类中，只要出现以下三个方法中的任意一个，那么该类就被称为描述器类
    """

    # def __get__(self, instance, owner):
    #     print('访问属性的时候被触发')
    #     return self.value
    #
    def __set__(self, instance, value):
        print('__set__方法被触发')
        self.value = value
        # print(self)
        # print(instance)
        # print(value)

    # def __delete__(self, instance):
    #     print('删除属性值得时候会被触发')
    #     self.value = None


class Model(object):
    name = 'musen'
    attr = Filed()  # 描述器对象：会覆盖类属性相关操作


m = Model()
# m.name = 'bais'
# print(m.name)
m.attr = 1000
# del m.attr
print(m.attr)



