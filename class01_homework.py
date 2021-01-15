import time
# 作业

# one:  满足闭包函数的三个条件
# 1、函数嵌套函数
# 2、内层嵌套函数中引用外层非全局变量
# 3、外层函数中返回内层嵌套函数名


# two: 计算函数的运行时间

# def func():
#     pass
#
# def count_functime():
#     start_time = time.time()
#     print(start_time)
#     func()
#     end_time = time.time()
#     return (f'函数的运行时间为{end_time-start_time}')
#
# res = count_functime()
# print(res)



# 编写装饰器，为多个函数加上认证的功能(用户的账号密码来源于文件)，要求登录成功一次，后续函数都不需要登录

with open("user.txt") as f:
    users = eval(f.read())

print(users)

def login_check(func):
    def fun():
        while not users['token']:
            username = input('请输入账号：')
            password = input('请输入账号：')

            if username == users["user"] and password == users["pwd"]:
                print(users["token"])
                users["token"] = True
                print(users["token"])

                func()
        else:
            func()


    return fun

@login_check
def index():
    print('这是登录的首页')
@login_check
def index1():
    print('这是登录的首页1')
@login_check
def index2():
    print('这是登录的首页2')


if __name__ == '__main__':
    index()
    index1()



