#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
@AUTHER:   hailiyang
@DATE:     2023/10/29 19:56
@FILENAME: app.py
"""

from flask import Flask, request
import redis
from celery import Celery

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379)


def test(data):
    # 在这里执行异步操作，使用传递的参数 data
    # 例如，执行耗时的计算任务或其他操作
    print('result: ', data)


@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.form['data']
    # 将请求参数发布到Redis频道
    redis_client.publish('task_channel', data)
    return 'Request accepted and queued for processing'


def pubsub_subscriber():
    redis_client = redis.Redis(host='localhost', port=6379)
    pubsub = redis_client.pubsub()
    pubsub.subscribe('task_channel')

    for message in pubsub.listen():
        print('message: ', message)
        if message['type'] == 'message':
            data = message['data']
            # 异步执行函数f
            test(data)


if __name__ == '__main__':
    import threading
    thread = threading.Thread(target=pubsub_subscriber)
    thread.start()
    app.run()
