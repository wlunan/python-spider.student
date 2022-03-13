import json
import jsonpath

obj = json.load(open('073_jsonpath.json','r',encoding='utf8'))

# 书店的所有作者
# temp_list = jsonpath.jsonpath(obj,'$.store.book[*].author')

# 所有的作者
# temp_list = jsonpath.jsonpath(obj,'$..author')

# store的所有元素
# temp_list = jsonpath.jsonpath(obj,'$.store.*')

# store中的所有price
# temp_list = jsonpath.jsonpath(obj,'$.store..price')

# 第三本书
# temp_list = jsonpath.jsonpath(obj,'$.store.book[2]')

# 最后一本书
# temp_list = jsonpath.jsonpath(obj,'$.store.book[(@.length-1)]')

# 前两本书
# temp_list = jsonpath.jsonpath(obj,'$..book[0,1]')
# temp_list = jsonpath.jsonpath(obj,'$.store..[:2]')

# 过滤所有包含isbn的书
# temp_list = jsonpath.jsonpath(obj,'$..book[?(@.isbn)]')

# 过滤出价格低于10的书
# temp_list = jsonpath.jsonpath(obj,'$..book[?(@.price<10)]')

# 所有元素
temp_list = jsonpath.jsonpath(obj,'$..*')
print(temp_list)