import urllib.request
import json
import jsonpath
import urllib.parse


# 第一页网址：https://api.vvhan.com/api/360wallpaperApi.php?cid=360new&start=0&count=30
# 第二页网址：https://api.vvhan.com/api/360wallpaperApi.php?cid=360new&start=30&count=30
# 第n页网址：https://api.vvhan.com/api/360wallpaperApi.php?cid=360new&start=start&count=page

# start 0    30  60
# page 1   2  3
# count 30
# start=(page-1)*30
# 请求对象的定制

def create_request(page,url):
    # 若输入的url为空就使用默认url
    if(url==''):
        end_url = 'https://api.vvhan.com/api/360wallpaperApi.php?cid=360new&'
    else:
        end_url = url
    # data数据制作
    data = {
        'start':(page-1)*30,
        'count':30
    }
    # 将data数据转换成get请求格式
    data = urllib.parse.urlencode(data)
    # 将data拼接到end_url后面
    end_url = end_url+data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
    }
    request = urllib.request.Request(url=end_url, headers=headers)

    return request

def get_content(request):
    # 发送请求，获取响应数据
    response = urllib.request.urlopen(request)

    content = response.read().decode('utf8')

    return content

def down_load(content):
    # 获取数据保存到本地
    with open('个人网站图片.json','w',encoding='utf8') as fp:
        fp.write(content)

    # 解析JSON数据
    obj = json.load(open('个人网站图片.json','r',encoding='utf8'))
    # 获取图片地址
    imgs_add = jsonpath.jsonpath(obj,'$..url')
    # 获取图片id
    imgs_name = jsonpath.jsonpath(obj,'$..id')
    print(len(imgs_add))
    print(imgs_add)

    # 下载图片
    for i in range(len(imgs_name)):
        name = imgs_name[i]
        add = imgs_add[i]
        urllib.request.urlretrieve(url=add,filename='./4K/'+name+'.jpg')
        # 下载多页图片时出现错误：urllib.error.ContentTooShortError: <urlopen error retrieval incomplete:
        # got only 366683 out of 855014 bytes>

if __name__ == '__main__':
    print('该程序为采集个人主页（http://time.plutos.top/）图片')
    url = input('请输入图片请求的url')
    start_page = int(input('采集起始页码（每页30张图片）'))
    end_start = int(input('采集结束页码'))

    for page in range(start_page,end_start+1):
        # 请求对象的定制
        request = create_request(page,url)
        # 获取响应数据
        content = get_content(request)
        # 下载数据到本地
        down_load(content)
