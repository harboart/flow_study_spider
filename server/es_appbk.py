import sys
from elasticsearch import Elasticsearch
import datetime
import json
import sql_appbk
import time
import platform

#es 搜索
#文档https://elasticsearch-py.readthedocs.io/en/7.9.0/
#pip3 install elasticsearch==7.9.0

#数据库
#带选择数据库功能
node = platform.node()
online_nodes = ["n1.appbk.com","iZj6ccepuz1ebnidz3cwfxZ"] #线上服务器列表
if node in online_nodes: #线上内网
    ES = Elasticsearch(["http://localhost:9200"])
else:
    ES = Elasticsearch(["http://47.242.206.108:9200"])

ES_INDEX = "flow_code"


# 向es插入一条数据,data格式为dict
# 使用时修改es地址，索引名
def search_es(query="NFT", start=0, limit=10):
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
    #print(json.dumps(res))

    result = []
    num = res['hits']['total']['value'] #搜索结果数

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

    return num, result


if __name__ == '__main__':
    # query = "NFT"
    # num, result = search_es(query)
    print(num)
    # print(json.dumps(result))



