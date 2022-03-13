# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&
# start=0&limit=20

# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&
# start=20&limit=20

# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&
# start=40&limit=20

# 请求url的规律
# start :0  20  40...
# page：1    2   3   4...
# limit:20
# start =(page-1)*20

# 下载豆瓣电影前10页
# 1.请求对象的定制
# 2.获取响应的数据
# 3.下载数据

import urllib.request
import urllib.parse


def creatRequest(page):
    baseUrl = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&"
    data = {
        "start": (page - 1) * 20,
        "limit": 20
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
    }
    # 将data转换成get请求格式
    data = urllib.parse.urlencode(data)
    # 将data拼接到url末尾
    url = baseUrl + data
    # 伪装请求
    request = urllib.request.Request(url=url, headers=headers)
    return request


def responseData(request):
    # 获取响应
    responsee = urllib.request.urlopen(request)
    # 将响应数据写入文件
    content = responsee.read().decode("utf8")
    return content


def writeData(content,page):
    with open("movie" + str(page) + ".json", "w", encoding="utf8") as fp:
        fp.write(content)


# 程序的入口
if __name__ == '__main__':
    startPage = input("请输入起始的页码")
    endPage = input("请输入结束的页码")
    for page in range(int(startPage), int(endPage)+1):
        # 请求对象的伪装
        request = creatRequest(page)
        # 发送请求获取响应
        content = responseData(request)
        # 写入文件
        writeData(content,page)
