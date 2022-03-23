from bs4 import BeautifulSoup

# 同过使用bs4解析本地文件进行学习
# 默认打开的文件编码是gbk，在打开文件的时候需要进行编码
# 本地文件生成对象
soup = BeautifulSoup(open('075.html',encoding='utf8'),'lxml')

# 根据标签名查找节点
# 找到的是第一个符合条件的数值
# print(soup.a)
# 获取标签的属性和属性值
# print(soup.a.attrs)

# bs4的一些函数
# 1.find
# 返回的是第一个符合条件的数据
# print(soup.find('a'))

# 根据title的值找到对应的对象
# print(soup.find('a',title='a2'))

# 根据class的值来找到对应的标签对象，注意是class需要添加下划线（关键字冲突）
# print(soup.find('a',class_='c1'))

# 2.find_all    返回的是一个列表 并返回了所有的标签
# print(soup.find_all('a'))

# 如果想要获取多个标签的值，需要以列表的格式输入
# print(soup.find_all(['a','li']))

# limit的作用是限制查找的前几个数据
# print(soup.find_all('li',limit=2))



# 3.select（推荐）
# select返回的是一个列表，并会返回多个数据
# print(soup.select('a'))

# 可以通过.代表class  我们把这种操作叫做类选择器
# print(soup.select('.c1'))
# # 代表id
# print(soup.select('#l1'))

# 属性选择器--通过属性标签来寻找对应的标签
# 查找到li标签中有id的标签
# print(soup.select('li[id]'))

# 查找到li标签中id为l2的标签
# print(soup.select('li[id="l2"]'))

# 层级选择器
# 选取后代结点
# print(soup.select('div li'))

# 选择子代结点 该标签下一级标签
# 注意很多计算机语言中 如果不加空格不会输出内容，但在bs4中不会报错会显示内容
# print(soup.select('div>ul>li'));

# 节点信息  获取节点内容
# obj = soup.select('#d1')[0]
# 如果标签对象中 只有内容 那么string和get_text()都可以使用
# 如果标签对象中 除了内容还有标签 那么string就获取不到数据，而get_text()可以获取到数据
# 我们一般情况下 推荐使用get_text()
# print(obj.string)
# print(obj.get_text())

# 节点的属性
# obj = soup.select('#p1')[0]
# name是标签的名字
# print(obj.name)
# 将属性作为一个字典值返回attrs
# print(obj.attrs)

# 获取节点的属性
obj = soup.select('#p1')[0]
print(obj.attrs.get('class'))
# print(obj.get('class'))
# print(obj['class'])