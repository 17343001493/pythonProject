#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 6:05 下午
# @Author  : Bais
# @File    : class07.py
"""
内存管理
1.对象引用
2.intern机制
3.深浅拷贝
4.垃圾回收和GC模块
"""
import requests
import copy
import time
import threading


# 可变的数据类型： 列表 字典 字典
# 不可变的数据类型：数值、字符串、元祖
# 小整数池--->数值     -5 256  都是提前创建好的，放在小整数池中
# 大整数池————>字符串   intern机制，只储存包含标准字符（数字、字母、下划线）的字符串，包含特殊字符的字符串不会被添加到大整数池中
# 深浅拷贝通常只在列表嵌套列表时讨论
li = [1, 2, 3]
li.copy()  # 浅拷贝
copy.deepcopy(li)  # 深拷贝

# 垃圾回收机制： 引用计数为0时会回收
# 循环引用

"""
并发和性能
1.并发和并行
2.同步和异步
线程

"""

def func1():
    for i in range(5):
        time.sleep(1)
        print('正在做事情1--{}'.format(threading.current_thread()))


def func2():
    for i in range(6):
        time.sleep(1)
        print('正在做事情2--{}'.format(threading.current_thread()))


# s_time = time.time()
# func1()
# func2()
# e_time = time.time()
# print(e_time-s_time)

# def main():
#     # 创建一个线程去执行事情1
#     t1 = threading.Thread(target=func1)
#     # 创建一个线程去执行事情2
#     t2 = threading.Thread(target=func2,name='th_1')
#     s_time = time.time()
#
#     t1.setName('线程1')
#     # 开始执行线程1
#     t1.start()
#     print(t1.getName())
#     print(t1.is_alive())
#     # 开始执行线程2
#     t2.start()
#
#     # 让主线程等待子线程执行完了之后再继续往下执行
#     print(threading.enumerate())  # 当前运行的所有线程对象
#     print(threading.active_count())   # 返回当前执行线程的数量（主线  两个子线程）
#     t1.join(2)
#     t2.join(2)
#
#     e_time = time.time()
#     print(e_time-s_time)
#     print(t1.is_alive())
#


# 通过继承thread类来创建线程
class RequestThread(threading.Thread):
    def __init__(self,url):
        self.url = url
        super().__init__()
    def run(self):
        """
        发送request请求
        :return:
        """
        for i in range(10):
            res = requests.get(self.url)
            print('线程：{}---返回的状态码{}'.format(threading.current_thread(),res.status_code))


# 创建线程发起请求
# s_time = time.time()

# for i in range(5):
#     t = RequestThread('http://www.baidu.com')
#     t.start()
# t.join()
# e_time = time.time()
# print("耗时：",s_time-e_time)

# if __name__ == '__main__':
#     pass



# 多线程全局变量


a = 100
def func3():
    global a
    for i in range(1000000):
        meta.acquire()  # 上锁
        # a = 100 暂停了切换到任务2
        a += 1
        meta.release()   # 释放锁
    print('线程1修改完a:',a)


def func4():
    global a
    for i in range(1000000):
        meta.acquire()  # 上锁
        a += 1
        meta.release()   # 释放锁
    print('线程2修改完a:',a)

# 创建锁
meta = threading.Lock()

s_time = time.time()
t3 = threading.Thread(target=func3)
t4 = threading.Thread(target=func4)
t3.start()
t4.start()
t3.join()
t4.join()
print(a)
e_time = time.time()
print('时间：{}'.format((e_time-s_time)))

# 锁

"""
未上锁：
线程1修改完a:线程2修改完a: 1282550
 1238012
1282550
时间：0.3334941864013672

上锁：
线程1修改完a: 1957882
线程2修改完a: 2000100
2000100
时间：1.035202026367187

"""
