# 使用方式
# 1.本地使用
# 2.服务器响应的数据 response.read().decode("utf-8")

from lxml import etree
# 解析本地文件
tree = etree.parse('xpath基本使用.html')
# print(tree)

# tree.xpath("xpath路径")

# 查找ul下的li
# liList =  tree.xpath('//ul/li')
# print(liList)

# 查找ul下所有id属性的标签
# /text() 获取标签中的内容
# liList = tree.xpath('//ul/li[@id]/text()')

# 找到id为l1的标签    id后面的内容要用引号（记得单引号双引号交替使用）
# liList = tree.xpath('//ul/li[@id="l1"]/text()')

# 查询到id为l1标签的class的属性值
# liList = tree.xpath('//ul/li[@id="l1"]/@class')

# 查找id中包含l的li标签
# liList = tree.xpath('//ul/li[contains(@id,"l")]/text()')

# 查找id中以c开头的li标签
# liList = tree.xpath('//ul/li[starts-with(@id,"c")]/text()')

# 查找id为l1并且class值为c1的li标签
# liList = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')

# 查询id为l2或者为l3的li标签
liList = tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l3"]/text()')
print(len(liList))
print(liList)

