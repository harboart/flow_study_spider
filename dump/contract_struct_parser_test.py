import json
import re
from flow_study_spider import sql_appbk
import requests

"""
功能：解析原始数据代码，获得数据格式
输入：parsed_info_list go服务获得的
返回：
"""
def parse_code(code_info):
    struct_info =code_info['program']['Declarations'][0]
    if struct_info['Identifiers']:
        struct_name = struct_info['Identifiers'][0]['Identifier']
    else:
        struct_name= struct_info['Identifier']['Identifier']
    start_pos= struct_info['StartPos']['Line']
    end_pos= struct_info['EndPos']['Line']

    if struct_info['Type'] == "FunctionDeclaration":
        struct_type = "fun"
    elif struct_info['Type'] == "CompositeDeclaration" and struct_info['CompositeKind'] == "CompositeKindResource":
        struct_type = "resource"
    elif struct_info['CompositeKind'] == "CompositeKindEvent":
        struct_type = "event"
    result_dic = {}
    result_dic["struct_type"] = struct_type
    result_dic["struct_name"] = struct_name
    result_dic["start_pos"] = start_pos
    result_dic["end_pos"] = end_pos
    return result_dic






"""
功能：从Go中获取原始数据
输入：code_text，原始代码
返回：code_info，go中获取的json格式原始数据，需要load
"""
def get_code_info(code_text):
    url =  "http://127.0.0.1:8080/parse"
    code_info = requests.post(url,data=code_text).text
    code_info_json =  json.loads(code_info)
    return code_info_json


"""
功能：解析代码，go语言服务获取的json格式代码结构,主函数
输入：code_text，原始代码,
返回：parsed_info_list，代码结构，[{"struct_type":"resource","struct_name":"NFT","start_pos":"2","end_pos":"6" },{...} ]
"""
def code_et():
    sql = """
    SELECT contract_address,contract_name,contract_code FROM `flow_code` WHERE contract_type = "contract" and is_structed=0 limit 2
    """
    flow_code  = sql_appbk.mysql_com(sql)
    # print(code_text)
    for item in flow_code:
        code_text_single = item['contract_code']
    # step1，E extract，所有东西都是etl，获得原始解析数据，从GO的服务中获取
        code_info  = get_code_info(code_text_single)

    # step2 T transform 解析原始数据代码，获得需要的数据结构信息
        result_dic  = parse_code(code_info)
        sql_insert = """
        INSERT INTO flow_code_struct (contract_address,contract_name,struct_type,struct_name,start_pos,end_pos) VALUES("{}","{}","{}","{}",{},{})
        """.format(item['contract_address'],item['contract_name'],result_dic['struct_type'],result_dic['struct_name'],result_dic['start_pos'],result_dic['end_pos'])
        insert_struct = sql_appbk.mysql_com(sql_insert)





if __name__ == '__main__':
    code1 = """ // Declare the NFT resource type
    pub resource NFT {
        // The unique ID that differentiates each NFT
        pub let id: UInt64

        // Initialize both fields in the init function
        init(initID: UInt64) {
            self.id = initID
        }
    }"""

    code2 ="""
            pub fun idExists(id: UInt64): Bool {
            return self.ownedNFTs[id] != nil
        }
    """
    code3="""
     pub event PriceChanged(id: UInt64, newPrice: UFix64, owner: Address?)

    """
    # ret = get_code_info(code3)
    #
    # ret2=parse_code(ret)
    # print(ret2)
    code_et()