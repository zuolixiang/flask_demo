#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
@AUTHER:   hailiyang
@DATE:     2023/10/31 22:44
@FILENAME: analyse_bp
"""

from flask import Blueprint, request
import logging

# 日志
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

# 配置规划分析
analyse = Blueprint('analyse', __name__)


@analyse.route('/EIMS/analyse/get_result', methods=['POST'])
def test():
    uuid = request.form['uuid']
    return 'uuid: ' + uuid

