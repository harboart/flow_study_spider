#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 heyhx, Inc. All Rights Reserved
#
# @Version : 1.0
# @Author  : snaketao
# @Time    : 2021-10-23 15:32
# @FileName: am_goods_info.py
# @Desc    :
import json
import sys
import re
import time
import es_appbk
import web
# import ai_code
#pip install web.py

urls = (
    '/hello', 'hello',
    '/search','search',#搜索
)

'''
测试
'''
class hello:
    def GET(self):
        web.header('Access-Control-Allow-Origin','*')
        web.header('Content-Type','text/json; charset=utf-8', unique=True)
        web.header('Access-Control-Allow-Credentials', 'true')
        return "hello"

'''
代码搜索
'''
class search:
    def GET(self):
        # 设置http header
        web.header('Access-Control-Allow-Origin','*')
        web.header('Content-Type','text/json; charset=utf-8', unique=True)
        web.header('Access-Control-Allow-Credentials', 'true')
        # 获得请求参数
        param = web.input(word="NFT", start="0", limit="10")
        word = param.word  # 获得搜索词
        start = int(param.start)  # 获得开始位置
        limit = int(param.limit)

        num, result= es_appbk.search_es(word, start, limit)
        final_result = {
            "status":0,
            "msg":"success",
            "num":num,
            "results":result
        }
        return json.dumps(final_result)




if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

