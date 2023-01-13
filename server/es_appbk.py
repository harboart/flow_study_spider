import json
import platform

from elasticsearch import Elasticsearch

import sql_appbk
# 数据库
# 带选择数据库功能
from get_keywords import get_keywords

# es 搜索
# 文档https://elasticsearch-py.readthedocs.io/en/7.9.0/
# pip3 install elasticsearch==7.9.0

node = platform.node()
online_nodes = ["n1.appbk.com","iZj6ccepuz1ebnidz3cwfxZ"] #线上服务器列表
if node in online_nodes: #线上内网
    ES = Elasticsearch(["http://localhost:9230"])
else:
    ES = Elasticsearch(["http://8.218.127.18:9230"])
    # ES = Elasticsearch(["http://47.242.206.108:9200"])
#     9230 port

ES_INDEX = "flow_code"

#start = (pagenum-1)*pagesize
#limit = pagesize
# 向es插入一条数据,data格式为dict
# 使用时修改es地址，索引名
def search_es(query, start, limit, contract_type, contract_category):
# def search_es(query, start, limit,contract_type, contract_category):
    # dsl = {"query": {
    #                 "query_string": {
    #                     "fields": ["contract_name", "contract_code"],
    #                     "query": query
    #                 }
    #         },
    #  "()"
    # query = "(contract_name:("+query+"))OR(contract_code:("+query+"))"
    # contract_category = None
    if contract_type and contract_category:
        query = "(contract_name:("+query+"))OR(contract_code:("+query+"))AND(contract_type:("+contract_type+"))AND(contract_category:("+contract_category+"))"
    elif contract_category and contract_type is None:
        query = "(contract_name:("+query+"))OR(contract_code:("+query+"))AND(contract_category:("+contract_category+"))"
    elif contract_type and contract_category is None:
        query = "(contract_name:("+query+"))OR(contract_code:("+query+"))AND(contract_type:("+contract_type+"))"
    else:
        query = "(contract_name:("+query+"))OR(contract_code:("+query+"))"
    # query = "(contract_name:("+query+"))OR(contract_code:("+query+"))"
    # query = "(contract_name:("+query+"))OR(contract_code:("+query+"))AND(contract_type:("+contract_type+"))"
    # print("321321"+query)
    dsl = {"query": {
               "query_string": {
                   # "fields": ["contract_name", "contract_code"],
                   "query": query
               }
       },
       "highlight": {
           "fields": {
               "contract_name": {},
               "contract_code": {}
           }
       },
      "from": start,
      "size": limit
      }

    res = ES.search(index=ES_INDEX, body=dsl)
    # print('es 搜索出的数据'+json.dumps(res))

    result = []
    num = res['hits']['total']['value'] #搜索结果数
    took_time = res['took'] # 搜索使用时间

    for item in res['hits']['hits']:
        score = item["_score"] #文档得分
        data = item["_source"]
        data["_score"] = score #es得分
        data["url"] = "https://flow-view-source.com/mainnet/account/{}/contract/{}".format(data["contract_address"], data["contract_name"])

        #飘红
        contract_name = item["_source"]["contract_name"] # 默认使用原来的标题
        if "contract_name" in item["highlight"]:#如果有, 则用高亮的
            contract_name = "|".join(item["highlight"]["contract_name"])


        contract_code = item["_source"]["contract_code"] # 默认使用原来的正文
        if "contract_code" in item["highlight"]:#如果有, 则用高亮的
            contract_code = "|".join(item["highlight"]["contract_code"])

        data["contract_name"] = contract_name
        data["contract_code"] = contract_code

        result.append(data)
    result_dict={}
    result_dict["num"] = num
    result_dict["result"] = result
    result_dict["took_time"] = took_time
    return result_dict



"""
功能：获取相关代码，contract_name，contract_address作为代码唯一标识，或取合约代码，提取代码关键词，搜索相关代码
输入： 
输出:相关代码
"""
def get_similar(query, start=1, limit=10):

    dsl = {"query": {
                    "query_string": {
                        "fields": ["contract_name", "contract_code"],
                        "query": query
                    }
            },
            "highlight": {
                "fields": {
                    "contract_name": {},
                    "contract_code": {}
                }
            },
           "from": start,
           "size": limit,
           }
    res = ES.search(index=ES_INDEX, body=dsl)

    result = res['hits']['hits']
    # num = res['hits']['total']['value'] #搜索结果数
    # print(result)
    return result


"""
功能：获取相关代码
输入：
返回:
"""
def get_similar_code(contract_address,contract_name):
    sql = """
    select * from flow_code where contract_address = '{}' AND contract_name ='{}' limit 1
    """.format(contract_address,contract_name)
    result = sql_appbk.mysql_com(sql)

    contract_code = result[0]["contract_code"]
    word_list =get_keywords(contract_code)
    result = {}
    if len(word_list)>50:
        query = word_list[0:50]
        query_a = " ".join(query)
        es_result = get_similar(query_a)
        # print("=======")
        # print(es_result)
    else:
        query_a = " ".join(word_list)
        es_result = get_similar(query_a)
    result["data"] = es_result
    # return json.dumps(result)
    return result


if __name__ == '__main__':
    contract_type = None
    # contract_type = "contract"
    contract_category = "token"
    query = "NFTStorefrontInitialized"
    # query = "nft"
    result_dict = search_es(query,1, 2, contract_type,contract_category)
    print(result_dict)
    print(json.dumps(result_dict))
    # search_es()

    # get_similar("NFT")
    # get_similar("import FungibleToken // {")
    # contract_name = "NWayUtilityCoin"
    # contract_address = "0x011b6f1425389550"
    # sc = get_similar_code(contract_address,contract_name)
    # print(sc)


