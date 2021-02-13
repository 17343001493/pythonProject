#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 10:28 下午
# @Author  : Bais
# @File    : class_09.py

"""
进程
多进程之间全局变量不共享
"""
# from queue import Queue
from multiprocessing import Process,Queue
import requests

import time

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = 1


# 多进程
def work1():
    for i in range(10):
        global a
        print('这个是任务1----{}'.format(a))
        a += 1
        time.sleep(0.5)


def work2():
    for i in range(10):
        global a
        print('这个是任务2----{}'.format(a))
        a += 1
        time.sleep(0.5)


# 多进程执行多任务
# 创建2个进程
# if __name__ == '__main__':
# p1 = Process(target=work1)
# p2 = Process(target=work2)
# p1.start()
# p2.start()

# 进程执行的时候，不加if __name__ == '__main__'为什么会报错
# 无限递归


"""
多进程直接的通讯问题
"""




def work3(q):
    while q.qsize() > 0:
        global a
        # 获取任务
        url = q.get()
        # 执行任务
        requests.get(url)
        print(f'work3正在执行任务----{a}')
        a += 1


def work4(q):
    while q.qsize() > 0:
        global a
        # 获取任务
        url = q.get()
        # 执行任务
        requests.get(url)
        print(f'work4正在执行任务----{a}')
        a += 1


if __name__ == '__main__':
    q = Queue()
    for i in range(10):
        q.put('http://127.0.0.1:5000')
    p3 = Process(target=work3,args=(q,))
    p4 = Process(target=work4,args=(q,))
    p3.start()
    p4.start()
