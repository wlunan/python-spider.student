import urllib.request
import jsonpath
import json
'''
分析星巴克产品图片
图片的url是单独返回的
https://www.starbucks.com.cn/images/products/affogato.jpg
https://www.starbucks.com.cn/images/products/cold-brew-malt.jpg
规律在于末尾产品名不同
1.获取产品名
通过bs4分析界面获取
2.下载图片老套路
'''
def creat_request():
    # 请求对象伪装
    url = 'https://www.starbucks.com.cn/assets/search/menu-source-zh.json'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
    }

    request = urllib.request.Request(url=url, headers=headers)

    # 获取响应数据
    response = urllib.request.urlopen(request)
    return response

def get_name(response):
    content = response.read().decode('utf8')
    # 将获取到的名字JSON数据保存到本地
    with open('076图片名字.json','w',encoding='utf8') as fp:
        fp.write(content)
    # 解析json数据
    obj = json.load(open('076图片名字.json','r',encoding='utf8'))

    # 获取后半端url
    url_list = jsonpath.jsonpath(obj,'$..preview')
    # 获取产品名字
    name_list = jsonpath.jsonpath(obj,'$..title')
    # 拼接下载链接 https://www.starbucks.com.cn/images/products/cappuccino.jpg
    get_down(name_list,url_list)

def get_down(name_list,url_list):
    for i in range(len(name_list)):
        name = name_list[i]
        url = url_list[i]
        # 拼接下载链接
        url = 'https://www.starbucks.com.cn'+url
        # 下载数据到本地
        filename =name
        # 处理不符合的文件名
        sets = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
        for char in filename:
            if char in sets:
                filename = filename.replace(char, '')
        urllib.request.urlretrieve(url=url, filename='./starStuck/'+filename+'.jpg')

if __name__ == '__main__':
    # 请求对象伪装获取
    response = creat_request()
    # 获取产品名字参数
    name_list = get_name(response)
