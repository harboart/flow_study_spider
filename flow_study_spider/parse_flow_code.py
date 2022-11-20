import json
import re
from flow_study_spider import sql_appbk
"""
功能：根据代码contract_code，判断代码的contact_type类型,contract_category分类。
"""



"""
功能；根据代码判断标签
输入：contract_code 
输出：标签 contract_type
"""
def get_code_type(contract_code):
    p = re.compile('pub contract.*|access\(all\) contract.*')  # 引用的正则
    i = re.compile('pub contract interface.*')
    if i.findall(contract_code):
        contract_type = "interface"
    elif p.findall(contract_code):  # 包含回车
        contract_type = "contract"
    else:
        contract_type = "transaction"
    return contract_type



"""
功能；根据代码判断标签
输入：contract_code
输出：标签 contract_category
"""
def get_code_category():
    sql = """
    select contract_name,id from flow_code where contract_type = "contract" and contract_category is null limit 1
    """
    ret = sql_appbk.mysql_com(sql)
    # print(contract_name)
    for item in ret:
        contract_name = item["contract_name"]
        id = item["id"]
        tgt_nft = "nft"
        tgt_token = "token"
        name_formate = contract_name.lower()
        code_category = ""
        if name_formate.find(tgt_nft):
            code_category = "nft"
        elif name_formate.find(tgt_token):
            code_category = "token"
        else:
            code_category = "other"
        sql_update = """
        update flow_code set contract_category = '{}' where id={}
        """.format(code_category,id)
        result = sql_appbk.mysql_com(sql_update)





"""
功能；读取sql中 contract_code，调用方法，打标签
输入： 
输出： 
"""
def process():
    sql_select = "select * from flow_code where contract_type is null "
    # sql_select = "select * from flow_code where id =2"
    ret = sql_appbk.mysql_com(sql_select)
    for item in ret:
        id = item["id"]
        code = item["contract_code"]
        contract_type = get_code_type(code)
        sql = """
        UPDATE flow_code SET contract_type = '{}' where id = {}
        """.format(contract_type,id)
        result = sql_appbk.mysql_com(sql)


if __name__ == '__main__':
    contract_code = """
with a central ledger smart contract. To send tokens to another user,
a user would simply withdraw the tokens from their Vault, then call
the deposit function on another user's Vault to complete the transfer.

*/
/// FungibleToken
// Follow the "Hello, World!" tutorial to learn more: https://developers.flow.com/cadence/tutorial/02-hello-world
pub contract HelloWorld {
    // Declare a public field of type String.
    //
    // All fields must be initialized in the init() function.
    pub let greeting: String

    /// TokensInitialized
    ///
    """
    # process()

    # cate_type= get_code_type(contract_code)
    # print(cate_type)
    get_code_category()