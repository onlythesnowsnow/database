#encoding: utf-8

from lxml import etree
import requests

BASE_DOMAIN = 'http://dytt8.net'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '37cs_pidx=1; 37cs_user=37cs74494399712; cscpvrich5041_fidx=1; 37cs_show=253; UM_distinctid=161dbbfbe51365-09eb7f628638b5-d35346d-144000-161dbbfbe52895; CNZZDATA1260535040=944178150-1519808422-%7C1519808422'
}

def get_detail_urls(url):
    response = requests.get(url,headers=headers)

    text = response.text
    html = etree.HTML(text)

    '''
    text = (response.content.decode('gbk')) 存在无法使用gbk编码进行解析的符号
    html = etree.HTML(text)
    '''

    detail_urls = html.xpath("//table[@class = 'tbspan']//a/@href")

    '''
    def abc(url):
        return BASE_DOMAIN+url
    index = 0
    for detail_url in detail_urls
        detail_url = abc(detail_url)
        detail_urls[index] = detail_url
        index += 1
    '''

    detail_urls = map(lambda url:BASE_DOMAIN+url,detail_urls)#匿名函数
    return detail_urls

def parse_detail_page(url):
    movie = {}
    response = requests.get(url , headers = headers)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class = 'title_all']//font[@color='#07519a']/text()")[0]
    #print(title)
    movie['title'] = title
    '''
    for x in title:
        print(etree.tostring(x,encoding='utf-8').decode("utf-8"))
    '''

    zoomE = html.xpath("//div[@id = 'Zoom']")[0]
    imgs  = zoomE.xpath(".//img/@src")
    cover = imgs[0]
    screeshot = imgs[1]
    movie['cover'] = cover
    movie['screenshot'] = screeshot

    #print(cover)

    def parse_info(info,rule):
        return info.replace(rule,"").strip()


    infos = zoomE.xpath(".//text()")
    #print(infos)
    for index,info in enumerate(infos):   #可以找出序号
        '''
        print(info)
        print(index)
        print('='*30)
        '''
        if info.startswith("◎年　　代") :   #以什么开始
            info = parse_info(info,"◎年　　代")
            # print(info)
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parse_info(info,"◎产　　地")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parse_info(info,"◎类　　别")
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info,"◎豆瓣评分")
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info,"◎片　　长")
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info,"◎导　　演")
            movie['director'] = info

        elif info.startswith("◎主　　演"):
            info = parse_info(info,"◎主　　演")
            actors = [info]
            for x in range(index+1,index+5):
                actor = infos[x].strip()
                actors.append(actor)
            #print(actors)

        elif info.startswith("◎简　　介"):
            info = parse_info(info,"◎简　　介")
            for x in range(index+1,len(infos)):
                profile = infos[x].strip()
                if profile.startswith("【下载地址】"):
                    break
                #print (profile)
                movie["profile"] = profile

    download_url = html.xpath("//td[@bgcolor = '#fdfddf']/a/@href")[0]
    #print(download_url)
    movie['down_load'] = download_url
    return movie

def spider():
    base_url = "http://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    movies = []
    for x in range(1,8):
        #用来控制页面数量
        url = base_url.format(x)
        #print(url)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            #用来遍历一页中所有的电影
            #print(detail_url)
            movie = parse_detail_page(detail_url)
            movies.append(movie)
            print(movie)  #获取一个就打印一个
        #print(movies) 打印全部
        with open('ssss', 'a+') as fw:
            fw.seek(0)
            fw.truncate()
            fw.write(str(movies))
            #break
        #break


if __name__ == '__main__':
    spider()