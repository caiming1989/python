# -*- coding:utf-8 -*-
def list_solution(this_list):
    for element in this_list:
        if isinstance(this_list,list):
             list_solution(element)
        else:
            print element,


