# 1.请求对象的定制
# 2.获取网页源码
# 3.下载

# 需求：下载前十页的图片
# 第一页：https://sc.chinaz.com/tupian/touxiangtupian.html
# 第二页：https://sc.chinaz.com/tupian/touxiangtupian_2.html
# 第三页：https://sc.chinaz.com/tupian/touxiangtupian_3.html
# 第n页：https://sc.chinaz.com/tupian/touxiangtupian_page.html
import urllib.request
from lxml import etree
# 站长素材图片爬取下载器

def create_request(page,url):
    # 对不同页面采用不同策略
    if (page==1):
        url_end = url
    else:
        #切割字符串
        url_temp = url[:-5]
        url_end = url_temp+'_'+str(page)+'.html'
    # 如果没有输入url就使用默认的url
    if(url==''):
        url_end = 'https://sc.chinaz.com/tupian/fengjingtupian.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
    }
    request = urllib.request.Request(url = url_end,headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf8')
    return content

def down_load(content):
    # 下载图片
    #urllib.request.urlretrieve('图片名称','文件名字')
    tree = etree.HTML(content)

    # 获取图片姓名    返回的是列表
    img_name = tree.xpath('//div[@id="container"]//a/img/@alt')
    img_add = tree.xpath('//div[@id="container"]//a/img/@src2')

    for i in range(len(img_name)):
        name = img_name[i]
        add = img_add[i]
        # 对图片下载地址进行定制
        url = 'https:'+add
        # 下载到本地
        urllib.request.urlretrieve(url=url,filename='./imgs/'+name+'.jpg')

if __name__ == '__main__':
    print('该程序为采集站长素材图片')
    url = input("请输入站长素材图片第一页的地址（内置默认为风景图片）")
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page,end_page+1):
        #请求对象的定制
        request = create_request(page,url)
        # 获取网页的源码
        content = get_content(request)
        # 下载
        down_load(content)