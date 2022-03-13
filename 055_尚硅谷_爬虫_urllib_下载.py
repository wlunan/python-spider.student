import urllib.request

# 下载网页
url_page = "http://plutos.top"

# url代表的是下载路径，filename文件的名字
# 在python中 可以写变量的名字 也可以写值
# urllib.request.urlretrieve(url_page,"card.html")

# 下载图片
urlImg = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F202004%2F01%2F20200401185207_tdcef.jpg&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1648649245&t=353610753403c143b99511604b224e1e"
urllib.request.urlretrieve(url=urlImg,filename="lisa.jpg")

# 下载视频
urlViedo = "https://vd3.bdstatic.com/mda-nbt03i183jrb0rrz/sc/cae_h264_delogo/1646006817419470843/mda-nbt03i183jrb0rrz.mp4?v_from_s=hkapp-haokan-hna&auth_key=1646059227-0-0-5c5f8d172e9eb7b27db50dcf1c800f67&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=0627462838&vid=8162424948124385284&abtest=100815_1-17451_1-3000220_3&klogid=0627462838"
urllib.request.urlretrieve(urlViedo,"video.mp4")