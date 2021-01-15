#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 7:46 下午
# @Author  : Bais
# @File    : class04.py
"""
面向对象三大特征： 封装 继承 多态
多态&鸭子类型
"""


# 伪多态的实现


class Animal(object):
    def run(self):
        print('---animai---run')


class Cat(Animal):
    def run(self):
        print('---cat---run')


class Dog(Animal):
    def run(self):
        print('---dog---run')


class Pig(Animal):
    def run(self):
        print('---dog---run')
        print('这是一个幂运算操作')


b_obj = Animal()
c_obj = Cat()
d_obj = Dog()
p_obj = Pig()


# 子类的对象属于父类类型的
# print(isinstance(c_obj,Animal))
# print(isinstance(c_obj,Cat))

# python中函数的参数是没有类型限制的
# 假设func的参数需要Base类型的

def func(base_obj):
    print(base_obj)
    base_obj.run()


# func(d_obj)
# func(p_obj)


# 私有属性

class Test:
    attr1 = 1000  # 公有属性
    # 私有属性
    _attr2 = 3000
    __attr3 = 4000


c = Test()

# 类属性可以通过类和实例对象去访问
# print(Test.attr1)
# print(c.attr1)

# 单下划线开头的私有属性
# print(Test._attr2)
# print(c._attr2)


# 双下划线开头的私有属性
# 双下划线开头的私有属性，对外不能直接访问，为了保护这个变量（对外改了名字）
# print(Test.__attr3)
# 在原有的属性上加了一个_Test
# print(Test._Test__attr3)
# print(c._Test__attr3)

# print(c.__attr2)
print(Test.__dict__)


# 私有属性的继承问题(私有属性也可以被继承)
class A():
    name = 'bais'
    __name = 'mm'


a = A()


# print(a.attr1)
# print(a._attr2)
# print(a._Test__attr3)

# __dict__   类调用时返回属性和方法的字典
# print(Test.__dict__)
# print(A.__dict__)


# __slots__   限制对象的属性
class Base(object):
    # 指定类对象所能绑定的属性
    # 限制属性
    # 节约内存：定义了slots属性之后，那么该对象不会再自动生成__dict__属性
    __slots__ = ['name']


b = Base()
# b.age = 20
# print(b.__dict__)
