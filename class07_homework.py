#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 2:42 下午
# @Author  : Bais
# @File    : class07_homework.py

import threading
import time

import requests
"""
1.描述什么是并发，什么是并行
并发：在不同任务之间快速切换

2.创建一个线程类，每个线程对地址URL = 'http://httpbin.org/post'发送100个请求，开启10个线程对象，同时发送，计算
总的耗时，分析平均每个请求所需要的时间\\]

"""
count = 0
class TheadRequests(threading.Thread):
    def run(self):
        global count
        for i in range(100):
            requests.get("http://127.0.0.1:5000/")
            count += 1
            print(f'Theading{i}---这是第{i}个请求')


def main():
    s_time = time.time()
    # 创建10个线程对象
    th = [TheadRequests() for j in range(10)]
    # 遍历线程对象
    for i in th:
        i.start()
    # 遍历线程对象，让主线程等待子线程结束之后再往下执行
    for i in th:
        i.join()
    e_time = time.time()
    print('平均时间：{}'.format((e_time-s_time)/1000))

main()