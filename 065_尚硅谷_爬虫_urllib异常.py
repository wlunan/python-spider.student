import urllib.request
import urllib.error
# url = "http://plutos.top/s"
url = "https://goudanss.com"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
    }

try:
    # 伪装请求对象
    request = urllib.request.Request(url=url,headers=headers)

    # 发送请求获取响应对象
    response = urllib.request.urlopen(request)

    # 读取数据
    content = response.read().decode("utf-8")
    print(content)
except urllib.error.HTTPError:
    print('系统正在升级')
except urllib.error.URLError:
    print("系统正在降级")