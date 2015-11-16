# -*- coding:utf-8 -*-
def list_solution(this_list,indent=False,level=0):
    for element in this_list:
        if isinstance(element,list):
             list_solution(element,indent,level+1)
        else:
            for num in range(level):
                if indent:
                    print '\t',
            print element


