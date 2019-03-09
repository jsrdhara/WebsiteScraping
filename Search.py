
# coding: utf-8
from google import search
def geturl(input_list):
    query_result=[]
    for i in input_list:
        inner_list=[]
        for j in search(i, tld="com", num=1, stop=1, pause=2): 
            inner_list.append(j)
        query_result.append(inner_list[0])
    return query_result
