"""
# 1、多个装饰器装饰同一个函数

# 2、Python中类里面三个内置的类装饰器

#  3、用类实现装饰器

"""
import time


def count():
    pass


def count_functime(func):
    def cost_time(*args, **kwargs):
        start_time = time.time()
        # print(start_time)
        func(*args, **kwargs)
        end_time = time.time()
        print('函数的运行时间为:{:.5f}'.format(end_time - start_time))

    return cost_time


with open("user.txt") as f:
    users = eval(f.read())


def login_check(func):
    def fun(*args, **kwargs):
        while not users['token']:
            username = input('请输入账号：')
            password = input('请输入账号：')

            if username == users["user"] and password == users["pwd"]:
                print(users["token"])
                users["token"] = True
                print(users["token"])

                func(*args, **kwargs)
        else:
            func()

    return fun


@login_check
@count_functime
def funcbais():
    time.sleep(3)
    print('这是需要被装饰的函数')


# funcbais()    #  从下往上装饰，从上往下运行


class MyTest(object):

    def __init__(self, name):
        self.name = name

    @classmethod  # 被classmethod装饰了之后，该方法就是一个类方法
    def add(cls):  # cls 代表的是类本身
        print("add")
        print(cls)

    @staticmethod
    def static():  # 静态方法不需要传参数,实例和类都可以调用
        print('这是个静态方法')

    @property  # 设定只读属性
    def read_attr(self):
        print('这个装饰器装饰完了之后，该方法可以像属性一样被调用')
        return '18岁'

    def sub(self):  # 代表的是实例本身
        print(self)


# t = MyTest('bais')
# t.name = 'didi'
# print(t.name)
# t.add()
# t.sub()
# MyTest.add()   # 被类方法装饰后，可以直接调用
# MyTest.static()
# t.static()
# print(t.read_attr)


# 魔术方法
class MyClass(object):
    def __init__(self, name):
        self.name = name
        print('这是init方法')

    def __new__(cls, *args, **kwargs):
        print("这个是new方法")
        # return super().__new__(cls)
        return object.__new__(cls)


# m = MyClass('bais')
# print(m.name)


# 单例模式

class MyTest01(object):
    __instance = None  # 设置一个类属性用来记录该类有没有创建过对象

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance


t1 = MyTest01()
t1.name = 'bais'

t2 = MyTest01()
print(t2.name)
print(id(t1))
print(id(t2))  # 两个对象的内存地址是一样的

# 装饰器实现单例模式
"""
第1行，创建外层函数singleton，可以传入类
第2行，创建一个instances字典用来保存单例
第3行，创建一个内层函数来获得单例
第4，5，6行， 判断instances字典中是否含有单例，如果没有就创建单例并保存到instances字典中，然后返回该单例
第7行， 返回内层函数get_instance
"""


def singleton(cls, *args, **kwargs):
    instance = {}

    def get_instances(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return get_instances


@singleton
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


"""
__str__方法和__repr__方法   重写这两个方法必须写return,是字符串
"""


class Bais(object):
    def __init__(self, name):
        self.name = name
        print("这是初始化方法")

    def __str__(self):
        print('---str---触发了')
        return 'hahaha'

    def __repr__(self):
        print('---repr---触发了')
        return '---字符串---'

    def __call__(self, *args, **kwargs):
        # 对象像函数一样调用的时候触发
        print('----call----')


# s = Bais('bais')
# print(s)
# str(s)
# format(s)
# repr(s)

# 通过类来实现装饰器  __call__

class Decorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('这个是装饰器里面的功能')
        self.func()


@Decorator  # test_01 = Decorator(test_01)
def test_01():
    print('原来的功能函数')


test_01()
