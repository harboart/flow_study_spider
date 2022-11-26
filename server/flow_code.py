import datetime
import json
import sql_appbk
import time
import platform




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
    return result


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
    """
    result = sql_appbk.mysql_com(sql)
    return result

"""
功能：获得代码相关合约
输入：
输出:
"""
def contracts():
    pass

"""
功能：获得代码相关脚本
输入：
输出:
"""
def scripts():
    pass


"""
功能：获得代码相关交易
输入：
输出:
"""
def transaction():
    pass



"""
功能：获得代码相关属性
输入：
输出:
"""
def code_info():
    pass



"""
功能：代码playground链接
输入：
输出:
"""
def playground():
    pass


if __name__ == '__main__':
    contract_name = "NWayUtilityCoin"
    contract_address = "0x011b6f1425389550"
    con = code(contract_address,contract_name)
    print(con)