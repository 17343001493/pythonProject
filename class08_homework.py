#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 5:50 下午
# @Author  : Bais
# @File    : class08_homework.py

"""
1.用一个队列来存储商品
2.创建一个专门产生商品的线程类，当商品数量小于50时，开始生产商品，每次生产200个商品，每生产完一轮暂停一秒
3.创建一个专门消费商品的线程类，当商品数量大于10就开始消费，循环消费，每次消费3个，商品小于10的时候暂停2秒

"""


import queue
import threading
import time

q = queue.Queue()

class  ProductionGoods(threading.Thread):
    def run(self):
        count = 0

        while True:
            if q.qsize() <50:
                for i in range(200):
                    count += 1
                    goods = '第{}个商品---'.format(count)
                    q.put(goods)
                    print('生产：',goods)
            time.sleep(1)



class ConsumptionGoods(threading.Thread):
    def run(self):

        while True:
            if q.qsize() > 10:
                for i in range(3):
                    print('消费：{}'.format(q.get()))
            else:
                time.sleep(3)

pro = ProductionGoods()
pro.start()
for i in range(5):
    c = ConsumptionGoods()
    c.start()

