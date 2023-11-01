#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
@AUTHER:   hailiyang
@DATE:     2023/10/29 20:41
@FILENAME: post_query
"""

import requests

url = 'http://localhost:8000/EIMS/analyse/get_result'  # 根据您的Flask应用的端口和地址进行相应更改
for i in range(20):
        uuid = 'hailiyang_' + str(i)
        data = {
                'data': 'hello world',
                'iteration': 100,
                'uuid': uuid
        }  # 替换为您想要发送的数据

        response = requests.post(url, data=data)

        print(response.text)  # 打印服务器的响应
