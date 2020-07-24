import requests
from bs4 import BeautifulSoup
from ShareForm_Flask.model import Course
import time


def worm_bilibili_python():#爬取bilibili的python关键字的视频并返回标题和链接组成的数据字典
    i=2
    url_0='https://search.bilibili.com/video?keyword=Python'
    resp_0=requests.get(url_0)
    html=resp_0.text
    while i<=50:
        url='https://search.bilibili.com/video?keyword=Python'+'&page=%s'%i
        i=i+1
        time.sleep(0.5)
        resp=requests.get(url)
        html = html+resp.text
    soup=BeautifulSoup(html,'html.parser')
    context=soup.find_all("a",attrs={"class":"title"})

    mylist=[]
    for i in context:
        value_href=i.get('href')
        value_title=i.get('title')
        course = Course(course_name=value_title,course_type="Python",course_url=value_href,platform_name="bilibili")
        mylist.append(course)
    return mylist



def worm_bilibili_java():#爬取bilibili的python关键字的视频并返回标题和链接组成的数据字典
    i=2
    url_0='https://search.bilibili.com/video?keyword=Java'
    resp_0=requests.get(url_0)
    html=resp_0.text
    while i<=50:
        url='https://search.bilibili.com/video?keyword=Java'+'&page=%s'%i
        i=i+1
        time.sleep(0.5)
        resp=requests.get(url)
        html = html+resp.text
    soup=BeautifulSoup(html,'html.parser')
    context=soup.find_all("a",attrs={"class":"title"})

    mylist=[]
    for i in context:
        value_href=i.get('href')
        value_title=i.get('title')
        course = Course(course_name=value_title,course_type="Java",course_url=value_href,platform_name="bilibili")
        mylist.append(course)
    return mylist


def worm_bilibili_C():#爬取bilibili的python关键字的视频并返回标题和链接组成的数据字典
    i=2
    url_0='https://search.bilibili.com/video?keyword=C%E8%AF%AD%E8%A8%80'
    resp_0=requests.get(url_0)
    html=resp_0.text
    while i<=50:
        url='https://search.bilibili.com/video?keyword=C%E8%AF%AD%E8%A8%80'+'&page=%s'%i
        i=i+1
        time.sleep(0.5)
        resp=requests.get(url)
        html = html+resp.text
    soup=BeautifulSoup(html,'html.parser')
    context=soup.find_all("a",attrs={"class":"title"})

    mylist=[]
    for i in context:
        value_href=i.get('href')
        value_title=i.get('title')
        course = Course(course_name=value_title,course_type="C语言",course_url=value_href,platform_name="bilibili")
        mylist.append(course)
    return mylist


def worm_bilibili_Pr():#爬取bilibili的python关键字的视频并返回标题和链接组成的数据字典
    i=2
    url_0='https://search.bilibili.com/video?keyword=Pr%E6%95%99%E7%A8%8B'
    resp_0=requests.get(url_0)
    html=resp_0.text
    while i<=50:
        url='https://search.bilibili.com/video?keyword=Pr%E6%95%99%E7%A8%8B'+'&page=%s'%i
        i=i+1
        time.sleep(0.5)
        resp=requests.get(url)
        html = html+resp.text
    soup=BeautifulSoup(html,'html.parser')
    context=soup.find_all("a",attrs={"class":"title"})

    mylist=[]
    for i in context:
        value_href=i.get('href')
        value_title=i.get('title')
        course = Course(course_name=value_title,course_type="Pr",course_url=value_href,platform_name="bilibili")
        mylist.append(course)
    return mylist


def worm_bilibili_PS():#爬取bilibili的python关键字的视频并返回标题和链接组成的数据字典
    i=2
    url_0='https://search.bilibili.com/video?keyword=PS%E6%95%99%E7%A8%8B'
    resp_0=requests.get(url_0)
    html=resp_0.text
    while i<=50:
        url='https://search.bilibili.com/video?keyword=PS%E6%95%99%E7%A8%8B'+'&page=%s'%i
        i=i+1
        time.sleep(0.5)
        resp=requests.get(url)
        html = html+resp.text
    soup=BeautifulSoup(html,'html.parser')
    context=soup.find_all("a",attrs={"class":"title"})

    mylist=[]
    for i in context:
        value_href=i.get('href')
        value_title=i.get('title')
        course = Course(course_name=value_title,course_type="PS",course_url=value_href,platform_name="bilibili")
        mylist.append(course)
    return mylist



# def updata_tobilibili():
#     conn = pymysql.connect(host="localhost",
#                                   user="root",
#                                   password="123",
#                                   db="bilibili_vedio",
#                                   charset="utf8")
#     cursor=conn.cursor()
#     try:
#         # cursor,conn=get_conn()
#         li=worm_bilibili()
#         sql="insert into bilibiliVedio(title,href) values(%s,%s)"
#         for item in li:
#             cursor.execute(sql, item)
#         conn.commit()
#     except:
#         traceback.print_exc()
#     finally:
#         cursor.close()
#         conn.close()
