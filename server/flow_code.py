import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

import sql_appbk

"""
功能：获得代码内容
输入：contract_address,合约地址
输入：contract_name,合约名称
返回: contract_code 合约代码
"""
def code(contract_address,contract_name):
    # step1 数据库为：flow_code
    sql = """
    SELECT * FROM flow_code WHERE contract_address = '{}' AND contract_name = '{}'
    """.format(contract_address,contract_name)
    result = sql_appbk.mysql_com(sql)
    # return json.dumps(result[0])
    return result[0]

"""
功能：获取代码结构
输入：contract_address,合约地址
输入：contract_name,合约名称
返回: 代码结构struct_type
返回: 代码结构struct_name
返回: 代码结构start_pos
"""
def code_structure(contract_address,contract_name):
    # 数据库 flow_code_struct
    sql = """
    SELECT * FROM flow_code_struct WHERE contract_address = '{}' AND contract_name = '{}'
    """.format(contract_address,contract_name)
    result = sql_appbk.mysql_com(sql)
    result_dict = {}
    result_dict["data"]=result
    # return json.dumps(result_dict)
    return result_dict

"""
功能：获得代码相关合约
输入：contract_address,合约地址
输入：contract_name,合约名称
返回: related_contract_name，相关合约的名称
返回: related_contract_address，相关合约的地址    
"""
def contracts(contract_address,contract_name):
    sql = """
    SELECT * FROM contract_relation WHERE contract_address = '{}' AND contract_name ='{}'
    """.format(contract_address,contract_name)
    result = sql_appbk.mysql_com(sql)
    result_dict = {}
    result_list = []
    for item in result:
        search_dict={}
        search_dict["related_contract_name"] = item["related_contract_name"]
        search_dict["related_contract_address"] = item["related_contract_address"]
        result_list.append(search_dict)
    result_dict["data"] = result_list
    # return json.dumps(result_dict)
    return result_dict

"""
功能：获得代码相关脚本,flow_code_relate_transaction
输入：
输出:
"""
def scripts():
    pass


"""
功能：从表flow_code_relate_transaction中获得代码相关交易，
输入：contract_address,合约地址
输入：contract_name,合约名称
返回: relate_transaction_name，相关交易的名称
返回: relate_transaction_address，相关交易的地址
"""
def transaction(contract_address,contract_name):
    sql = """
    select * from flow_code_relate_transaction where  contract_address = '{}' AND contract_name ='{}'
    """.format(contract_address,contract_name)
    result = sql_appbk.mysql_com(sql)
    result_dict = {}
    result_dict["data"] = result
    return result_dict
    # return json.dumps(result)



# 工具 推算日期
def delay_time(time_str, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
    if type(time_str) == str:
        time_str = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    ret = time_str + relativedelta(years=years, months=months, days=days, hours=hours, minutes=minutes, seconds=seconds)
    return ret

"""
功能：获得代码相关属性
输入：contract_address,合约地
输入：contract_name,合约名称
返回:
"""
def code_info(contract_address,contract_name):
    now_time = datetime.now()
    ret2 = delay_time(now_time, months=-1) # 一个月前日期

    sql = """
    select * from flow_code where contract_address = '{}' AND contract_name ='{}'
    """.format(contract_address,contract_name)
    result = sql_appbk.mysql_com(sql)

    # flow_trans_data 中 contract 对应的trans个数
    call_in_month_num = """
    SELECT count(*) as call_in_num FROM flow_trans_data WHERE contract_address = '{}' and contract_name ='{}'
    """.format(contract_address,contract_name)
    # call_in_month_num = """
    # SELECT count(*) as call_in_num FROM flow_trans_data WHERE contract_address = '{}' and contract_name ='{}'
    #   and fetch_time > '{}'
    # """.format(contract_address,contract_name,ret2)
    call_in = sql_appbk.mysql_com(call_in_month_num)

    result_dict = {}
    result_dict["contract_type"] = result[0]["contract_type"]
    result_dict["contract_address"] =result[0]["contract_address"]
    result_dict["contract_name"] = result[0]["contract_name"]
    result_dict["call_in_month"] = call_in[0]["call_in_num"]

    # return json.dumps(result_dict)
    return result_dict




"""
功能：代码playground链接
输入：
返回:
"""
def playground(contract_address,contract_name):
    sql = """
    select * from playground where contract_address = '{}' AND contract_name ='{}'
    """.format(contract_address,contract_name)
    result = sql_appbk.mysql_com(sql)
    if result:
        return result[0]
    else:
        return result
    # return json.dumps(result[0])



if __name__ == '__main__':
    # contract_name = "NWayUtilityCoin"
    # contract_address = "0x011b6f1425389550"


    # con = code(contract_address,contract_name)
    # con = code_structure(contract_address,contract_name)

    # contract_name = "CharityNFT"
    # contract_address = "0x097bafa4e0b48eef"
    # con = contracts(contract_address,contract_name)
    # con = transaction(contract_address,contract_name)


    # contract_name = "JoyrideAccounts"
    # contract_address = "0xecfad18ba9582d4f"
    contract_name = "NWayUtilityCoin"
    contract_address = "0x011b6f1425389550"
    con = playground(contract_address,contract_name)
    # con = code_info(contract_address,contract_name)
    print(con)
    # get_similar_code(contract_address,contract_name)