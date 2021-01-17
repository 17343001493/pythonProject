#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 1:42 下午
# @Author  : Bais
# @File    : class06.py
"""
元类  Python中的内置元类
1.使用type动态定义类
2.自定义元类
type: 元类，所有的类都是通过type创建的
object：基类，所以类的顶级父类
"""

# from django.db import models
from filed import BaseFiled, CharFiled, BoolFiled, IntFiled


def func(self):
    print('这个是funtion01')


# 空元祖  （）  元祖中只要一个元素  obj
# 利用元类直接创建类
# type创建类需要三个参数
# 第一个：类名--> 字符串类型
# 第二个：继承的父类-->tuple
# 第三个：方法和属性-->字典，键值对的形式表示属性 或者对应的方法
Test = type('Test', (object,), {"attr": 100, "__attr2": 200, "func01": func})
t = Test()


# t.func01()
# print(Test)
# print(Test.__dict__)
# print(Test.__bases__)


class Test1(object):
    attr = 100
    __attr2 = 200


# print(Test1)
# print(Test1.__dict__)


# 自定义元类
# 自定义元类必须继承于type
# type创建类： 三个参数

class MyMetaClass(type):
    """
    自定义元类，将类的所有属性名变成大写"""

    def __new__(cls, name, bases, attr_dict, *args, **kwargs):
        print('最基础的自定义元类')
        for k,v in list(attr_dict.items()):
            # 字典遍历的时候，不允许添加或者修改元素
            attr_dict[k.upper()] = v
            attr_dict.pop(k)
        # attr_dict['__slots__'] = ['name','age','gender']
        return super().__new__(cls, name, bases, attr_dict)


# 通过自定义的元类来创建类
class Test(metaclass=MyMetaClass):
    name = 'bais'
    age = 99
    gender = '男'


# print(type(Test))
# print(Test.name)

# 父类指定元类，子类可以继承父类所指的元类
class MyClass(Test):
    pass


# print(Test.__dict__)
# print(type(MyClass))
#


# 利用元类实现模型类
class FiledMetaClass(type):
    '''新建模型类的元类'''

    def __new__(cls, name, bases, dic, *args, **kwargs):
        if name == 'BaseModel':
            return super().__new__(cls, name, bases, dic)
        else:
            table_name = name.lower()  # 将类名转换为小写，对应数据表的名称
            fields = {}  # 定义一个空字典，用来存放模型类字段和数据表中字段对应的关系
            for k, v in dic.items():
                if isinstance(v, BaseFiled):
                    fields[k] = v
            dic['t_name'] = table_name
            dic['fields'] = fields
            print(dic)
            return super().__new__(cls, name, bases, dic)


class BaseModel(metaclass=FiledMetaClass):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)  # 便利出来的所有关键字参数，并且对对象进行属性设置

    def save(self):
        # 保存一条数据，生产一条对应的sql语句
        # 获取表名
        t_name = self.t_name
        # 获取总段名称
        fields = self.fields
        # 获取对应字段的值
        fields_dict = {}  # 创建一个字典用来储存键值对
        for filed in fields.keys():
            fields_dict[filed] = getattr(self, filed)
        # 生成对应的sql语句
        sql = 'INSERT INTO {} VALUES{};'.format(t_name, tuple(fields_dict.values()))
        print(sql)


class User(BaseModel):
    """用户模型类"""
    username = CharFiled()
    pwd = IntFiled()
    live = BoolFiled()

    # 字段1：字符串类型
    # 字段2：字符串类型
    # 字段3：字符串类型


# print(User.fields)
# print(User.t_name)

class Order(BaseModel):
    id = IntFiled()
    money = IntFiled()


xiaom = User(username='小明', age=18, pwd=123, live=True)
order1 = Order(id=111, money=222)
print(xiaom.username)
print(order1.id)
xiaom.save()
