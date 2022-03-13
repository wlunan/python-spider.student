import urllib.request

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
}

#1.请求对象的定制
request = urllib.request.Request(url = url,headers = headers);
#2.获取响应的数据
response = urllib.request.urlopen(request)
#3.读取响应的数据
content = response.read().decode("utf-8")

#4.将数据保存到本地
# open方法默认使用的gbk编码 ，如果我们想要保存汉字，需要则open方法中指定编码格式为utf-8
# encoding = "utf-8"
fp = open("movie01.json","w",encoding="utf-8")
fp.write(content)
fp.close()
