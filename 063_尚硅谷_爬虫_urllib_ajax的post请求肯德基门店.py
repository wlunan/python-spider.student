# 第一页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10

# 第二页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 2
# pageSize: 10

import urllib.request
import urllib.parse

def creatRequest(page):
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
    }
    data = {
        "cname": "北京",
        "pid": "",
        "pageIndex": page,
        "pageSize": "10"
    }
    data = urllib.parse.urlencode(data).encode("utf-8")
    # 伪装请求
    request = urllib.request.Request(url=url,headers=headers,data=data)
    return request

def responseData(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf8")
    return content

def writeData(page,content):
    with open("kfc"+str(page)+".json","w",encoding="utf8") as fp:
        fp.write(content)


if __name__ == '__main__':
    startPage = input("请输入起始页码")
    endPage = input("请输入结束页码")
    for page in range(int(startPage),int(endPage)+1):
        # 获取请求对象
        request = creatRequest(page)
        # 获取响应数据
        content = responseData(request)
        # 将数据写入文件
        writeData(page,content)
