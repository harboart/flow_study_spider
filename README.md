# flow_study_spider
Build a development and learning platform for Flow developers. The project includes 3 modules, a code download module, a search module, and a display module. The flow study system is mainly used as an effective tool and development platform for learning flow.


using gephi to build the user contract network
https://gephi.org/

## get_block.py

Get the height of the latest block and insert it into the flow_block table

## update_trans_multi.py
Read the code and name of the unprocessed block from flow_block,
call get_trans, insert flow_trans_data

## get_trans.py

Parse the trans script, get the referenced contract address, and insert it into the database flow_trans_data

## update_contract.py
In the flow_trans_data table, the contract address is obtained every hour and inserted into flow_contract_address

## get_contract.py

Get unprocessed contract_address from flow_contract_address table, insert into flow_code table

## parse_flow_code.py
获得合约代码的类型和分类

## contract_struct_parser2
分析代码结构，结构在代码中的位置
