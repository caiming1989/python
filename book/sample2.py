#-*- coding:utf-8 -*-
import  os
print os.getcwd()
os.chdir('../')
print os.getcwd()
data = open('caiming.txt')
print(data.readline())
