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
import web
import es_appbk
from flow_code import code, code_structure, contracts, transaction, code_info, playground

# import ai_code
#pip3 install web.py
#pip3 install python-dateutil
urls = (
    '/hello','hello',
    '/search','Search',#  代码搜索
    '/code','Code', # 获取代码内容
    '/code_structure','Code_structure', # 获取代码结构
    '/contracts','Contracts', # 代码相关合约
    '/transaction','Transaction',# 代码相关的交易
    '/code_info','Code_info',# 代码属性信息
    '/similar','Similar',  # 相似代码
    '/playground','Playground', # playground链接
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
class Search:
    def GET(self):
        # 设置http header
        web.header('Access-Control-Allow-Origin','*')
        web.header('Content-Type','text/json; charset=utf-8', unique=True)
        web.header('Access-Control-Allow-Credentials', 'true')
        # 获得请求参数
        param = web.input(query="NFT", start="1", limit="10")
        query = param.query  # 获得搜索词
        start = int(param.page_num)  # 获得开始位置
        limit = int(param.page_size)
        contract_type = param.contract_type
        contract_category = param.contract_category
        result_dict= es_appbk.search_es(query, start, limit, contract_type, contract_category)

        if result_dict:
            final_result = {
                "status":0,
                "msg":"success",
                "num":result_dict['num'],
                "results":result_dict['result'],
                "took_time": result_dict['took_time']
            }
        else:
            final_result = {
                "status":200,
                "msg":"fail"
            }
        return json.dumps(final_result)


class Similar:
    def GET(self):
        # 设置http header
        web.header('Access-Control-Allow-Origin','*')
        web.header('Content-Type','text/json; charset=utf-8', unique=True)
        web.header('Access-Control-Allow-Credentials', 'true')
        # 获得请求参数
        param = web.input(word="NFT", start="1", limit="10")
        contract_address = param.contract_address
        contract_name = param.contract_name

        result= es_appbk.get_similar_code(contract_address,contract_name)
        final_result = {
            "status":0,
            "msg":"success",
            "results":result
        }

        return json.dumps(final_result)

class Code:
    def GET(self):
        # 设置http header
        web.header('Access-Control-Allow-Origin','*')
        web.header('Content-Type','text/json; charset=utf-8', unique=True)
        web.header('Access-Control-Allow-Credentials', 'true')
        # 获得请求参数
        param = web.input()
        contract_address = param.contract_address  #  合约地址
        contract_name =  param.contract_name  #  合约名称
        result_dict = code(contract_address,contract_name)
        if result_dict:
            final_result = {
                "status": 0,
                "msg": "success",
                "id": result_dict['id'],
                "contract_name": result_dict['contract_name'],
                "contract_address": result_dict['contract_address'],
                "contract_code": result_dict['contract_code'],
                "contract_type": result_dict['contract_type'],
                "contract_category": result_dict['contract_category']
            }
        else:
            final_result = {
                "status":200,
                "msg":"fail"
            }
        return json.dumps(final_result)

class Code_structure:
    def GET(self):
        # 设置http header
        web.header('Access-Control-Allow-Origin','*')
        web.header('Content-Type','text/json; charset=utf-8', unique=True)
        web.header('Access-Control-Allow-Credentials', 'true')
        # 获得请求参数
        param = web.input()
        contract_address = param.contract_address  #  合约地址
        contract_name =  param.contract_name  #  合约名称
        result_dict = code_structure(contract_address,contract_name)
        if result_dict:
            final_result = {
                "status": 0,
                "msg": "success",
                "data": result_dict['data']
            }
        else:
            final_result = {
                "status":200,
                "msg":"fail"
            }
        return json.dumps(final_result)

class Contracts:
    def GET(self):
        # 设置http header
        web.header('Access-Control-Allow-Origin','*')
        web.header('Content-Type','text/json; charset=utf-8', unique=True)
        web.header('Access-Control-Allow-Credentials', 'true')
        # 获得请求参数
        param = web.input()
        contract_address = param.contract_address  #  合约地址
        contract_name =  param.contract_name  #  合约名称
        result_dict = contracts(contract_address,contract_name)
        if result_dict:
            final_result = {
                "status": 0,
                "msg": "success",
                "data": result_dict['data']
            }
        else:
            final_result = {
                "status":200,
                "msg":"fail"
            }
        return json.dumps(final_result)

# class Contracts:
#     def GET(self):
#         # 设置http header
#         web.header('Access-Control-Allow-Origin','*')
#         web.header('Content-Type','text/json; charset=utf-8', unique=True)
#         web.header('Access-Control-Allow-Credentials', 'true')
#         # 获得请求参数
#         param = web.input()
#         contract_address = param.contract_address  #  合约地址
#         contract_name =  param.contract_name  #  合约名称
#         result_dict = contracts(contract_address,contract_name)
#         if result_dict:
#             final_result = {
#                 "status": 0,
#                 "msg": "success",
#                 "id": result_dict['id'],
#                 "related_contract_name": result_dict['related_contract_name'],
#                 "related_contract_address": result_dict['related_contract_address']
#             }
#         else:
#             final_result = {
#                 "status":200,
#                 "msg":"fail"
#             }
#         return json.dumps(final_result)
class Transaction:
    def GET(self):
        # 设置http header
        web.header('Access-Control-Allow-Origin','*')
        web.header('Content-Type','text/json; charset=utf-8', unique=True)
        web.header('Access-Control-Allow-Credentials', 'true')
        # 获得请求参数
        param = web.input()
        contract_address = param.contract_address  #  合约地址
        contract_name =  param.contract_name  #  合约名称
        result_dict =  transaction(contract_address,contract_name)
        if result_dict:
            final_result = {
                "status": 0,
                "msg": "success",
                "data": result_dict['data']
            }
        else:
            final_result = {
                "status": 200,
                "msg": "fail"
            }
        return json.dumps(final_result)


class Code_info:
    def GET(self):
        # 设置http header
        web.header('Access-Control-Allow-Origin','*')
        web.header('Content-Type','text/json; charset=utf-8', unique=True)
        web.header('Access-Control-Allow-Credentials', 'true')
        # 获得请求参数
        param = web.input()
        contract_address = param.contract_address  #  合约地址
        contract_name =  param.contract_name  #  合约名称
        result_dict = code_info(contract_address,contract_name)
        if result_dict:
            final_result = {
                "status": 0,
                "msg": "success",
                "contract_type":result_dict["contract_type"],
                "contract_address":result_dict["contract_address"],
                "contract_name":result_dict["contract_name"],
                "call_in_month":result_dict["call_in_month"]
            }
        else:
            final_result = {
                "status": 200,
                "msg": "fail"
            }
        return json.dumps(final_result)


class Playground:
    def GET(self):
        # 设置http header
        web.header('Access-Control-Allow-Origin','*')
        web.header('Content-Type','text/json; charset=utf-8', unique=True)
        web.header('Access-Control-Allow-Credentials', 'true')
        # 获得请求参数
        param = web.input()
        contract_address = param.contract_address  #  合约地址
        contract_name =  param.contract_name  #  合约名称
        result_dict = playground(contract_address,contract_name)
        if result_dict:
            final_result = {
                "status": 0,
                "msg": "success",
                "id": result_dict['id'],
                "contract_address": result_dict['contract_address'],
                "contract_name": result_dict['contract_name'],
                "playground_url": result_dict['playground_url'],
            }
        else:
            final_result = {
                "status": 200,
                "msg": "fail"
            }
        return json.dumps(final_result)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

