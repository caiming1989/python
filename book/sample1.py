# -*- coding:utf-8 -*-
def list_solution(this_list,level):
    for element in this_list:
        if isinstance(element,list):
             list_solution(element,level+1)
        else:
            for num in range(level):
                print("\t",)
            print element,


