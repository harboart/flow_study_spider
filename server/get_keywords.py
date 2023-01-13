#!/usr/bin/env python3
#coding=utf-8
#########################################################################
# Author: @appbk.com
# Created Time: Sun 01 Mar 2020 09:08:42 PM CST
# File Name: index.py
# Description:
######################################################################
import string
string.punctuation
"""
功能：提取一段话的关键词列表
输入：text，一段文本
返回：word_list，文本中的关键词列表
"""


def get_keywords(text):
    text = text.replace('\n', '')
    punctuation_string = string.punctuation
    for i in punctuation_string:
        text = text.replace(i, '')
        word_list = text.split()
        # print(word_list)
    return word_list

if __name__ == '__main__':
    text = """
    Welcome to Cadence! This is one of the simplest programs you can deploy\n on Flow.
    """
    get_keywords(text)
