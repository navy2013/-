#！/usr/bin/env python
# -*-encoding:utf-8-*-
# author: navy
# 2022/1/7 9:34

import yaml

f = open('./config.yml')
y = yaml.load(f) # 生成一个对象
print(y)
# {'name': 'Tom Smith', 'age': 37, 'spouse': {'name': 'Jane Smith', 'age': 25}, 'children': [{'name': 'Jimmy Smith', 'age': 15}, {'name1': 'Jenny Smith', 'age1': 12}]}


