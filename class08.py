#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 2:59 下午
# @Author  : Bais
# @File    : class08.py

import threading
import time
import queue


"""
死锁
"""
a = 100
# def func3():
#     global a
#     for i in range(1000000):
#         meta_A.acquire()  # 上锁
#         meta_B.acquire()  # 上锁
#         print('------1111--------')
#         # a = 100 暂停了切换到任务2
#         a += 1
#         meta_A.release()   # 释放锁
#         meta_B.release()
#     print('线程1修改完a:',a)
#
#
# def func4():
#     global a
#     for i in range(1000000):
#         meta_B.acquire()  # 上锁
#         meta_A.acquire()
#         a += 1
#         meta_B.release()   # 释放锁
#         meta_A.release()
#     print('线程2修改完a:',a)
#
# # 创建锁
# meta_A = threading.Lock()
# meta_B = threading.Lock()
#
#
# s_time = time.time()
# t3 = threading.Thread(target=func3)
# t4 = threading.Thread(target=func4)
# t3.start()
# t4.start()
# t3.join()
# t4.join()
# print(a)
# e_time = time.time()
# print('时间：{}'.format((e_time-s_time)))

# 锁

# 全局解释器锁GIL   控制线程运行的

# io密集型，cpu密集型


def func3():
    global a
    for i in range(50):

        a += 2




def func4():
    global a
    for i in range(50):

        a += 2



s_time = time.time()
# t3 = threading.Thread(target=func3)
# t4 = threading.Thread(target=func4)
# t3.start()
# t4.start()
# t3.join()
# t4.join()
# func3()
# func4()
# cpu密集型：多线程相加2000000  多线程 4.45     单线程  3.54
# 网络io密集型：多线程：0.005    单线程  1.3
# ------------------------------------
e_time = time.time()
print('时间：{}'.format((e_time-s_time)))



# 队列
"""
三种
1.先入先出
2.后入先出
3.优先级
"""

'''1.先入先出'''
q = queue.Queue(3)
# 往队列里添加数据
q.put(1)
q.put(11)
# q.put(12)
# q.put(122,block=False)  # 往队列中添加数据不等待，队列已满会报错
# q.put_nowait(22)    # 往队列中添加数据不等待，队列已满会报错

# 获取队列中的数据
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get(block=False))  # 从队列中获取数据(不等待)，队列为空，会报错
# print(q.get_nowait())   # 从队列中获取数据(不等待)，队列为空，会报错

# 获取队列中的任务数
# print(q.qsize())
# q.put(12)
# print(q.qsize())

# 判断队列是否已满
# print(q.full())

# 判断队列是否为空
# print(q.empty())
# q.task_done()
# q.task_done()
# q.task_done()


# join: 判断队列中的任务是否执行完毕
# q.join()


'''2.后入先出'''
q2 = queue.LifoQueue()
q2.put(15)
q2.put(16)
q2.put(17)
print(q2.get())
print(q2.get())
print(q2.get())

'''3.优先级'''
q3 = queue.PriorityQueue()
q3.put((1,'haha1'))
q3.put((599,'haha599'))
q3.put((188,'haha188'))
print(q3.get())
print(q3.get())





