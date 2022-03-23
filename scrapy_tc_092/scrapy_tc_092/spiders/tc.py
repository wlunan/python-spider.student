import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字 用于爬虫的时候 使用的值
    name = 'tc'
    # 允许访问的域名
    allowed_domains = ['www.zz.58.com/job/?key=%E5%90%8E%E7%AB%AF&classpolicy=strategy,job_B,uuid_d2df8c64076e46e8b6d5483844530e0a,displocalid_342,from_9224,to_jump,tradeline_job,classify_D&final=1']
    # 起始的url    指的是第一次访问的域名
    # start_urls 是在allowed_domains的前面添加一个http://
    #              在allowed_domains后面添加一个/
    start_urls = ['https://zz.58.com/job/?key=%E5%90%8E%E7%AB%AF&classpolicy=strategy,job_B,uuid_d2df8c64076e46e8b6d5483844530e0a,displocalid_342,from_9224,to_jump,tradeline_job,classify_D&final=1/']


    # 是执行了start_urls后的方法    方法中的response就是返回的那个对象
    # 相当于 response = urllib.request.urlopen()
    #       response = requests.get()
    def parse(self, response):
        content = response.text
        print(content)
        pass
