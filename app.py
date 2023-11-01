#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
@AUTHER:   hailiyang
@DATE:     2023/10/29 19:56
@FILENAME: app.py
"""

from flask import Flask
import redis
from celery import Celery
import json
from blue_prints.analyse_bp import analyse
import multiprocessing
import gunicorn.app.base


app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379)
app.register_blueprint(analyse)


class GunicornApp(gunicorn.app.base.BaseApplication):
    def __init__(self, app, options=None):
        self.application = app
        self.options = options
        super().__init__()

    def load(self):
        return self.application

    def load_config(self):
        config = {
            key: value for key, value in self.options.items() if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)


def number_of_workers():
    return multiprocessing.cpu_count() * 2 + 1


if __name__ == '__main__':
    options = {
        'workers': number_of_workers()
    }
    GunicornApp(app, options).run()
