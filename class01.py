# 闭包、偏函数、数据锁定


# def login():
#     print('登录')


def func(num, b):
    print('-----func被调用-----')

    def count_book():
        print(num)
        print(b)
        print('这个是计算买书方式的函数')

    return count_book


res = func([1, 2, 3], 'pytthon')
print(res.__closure__)
res()


# 闭包条件：
# 条件一： 函数中嵌套函数
# 条件二： 外层函数返回内层嵌套函数名
# 条件三：内层嵌套函数有引用外层的一个非全局变量

# 作用  实现数据锁定，提高稳定性


# 装饰器   开放封闭原则


def login(func):
    def fun():
        username = 'python01'
        password = 'lemoban'
        user = input('请输入账号:')
        pwd = input('请输入密码:')
        if user == username and pwd == password:
            func()
        else:
            print('账号密码错误')

    return fun


# @login    #  @login: 语法糖 ———> index = login(index)
# def index():
#     print('这是网站的首页')

# index()

# 带参数的装饰器
# def add(func):
#     def fun(a,b):
#         print('相乘', a*b)
#         print('相除', a/b)
#         func(a,b)
#     return fun

# @add
# def add_num(a,b):
#     # 打印两个数相加
#     print('相加',a+b)
#
# add_num(11,22)

# 通用装饰器
# def add(func):
#     def fun(*args,**kwargs):
#         print('装饰器的功能代码：登录')
#         func(*args,**kwargs)
#     return fun
#
# @add
# def index():
#     print('这是网站的首页')
# @add
# def goods_list(num):
#     print('这是商品列表第{}页'.format(num))


# index()
# print('---------')
# goods_list(2)


# 装饰器装饰类

def add(func):
    def fun(*args, **kwargs):
        print('装饰器的功能代码：登录')
        return func(*args, **kwargs)

    return fun


@add  # MyClass = add(MyClass)
class MyClass:
    def __init__(self):
        pass


m = MyClass()
print('m的值', m)

#  1、用类实现装饰器

# 2、多个装饰器装饰同一个函数

# 3、Python中类里面三个内置的类装饰器
