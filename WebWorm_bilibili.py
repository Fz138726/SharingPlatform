import requests
from bs4 import BeautifulSoup
import pymysql
import sys
import traceback
from  model import Course
import time
# from selenium.webdriver import Chrome,ChromeOptions
import re


def worm_bilibili():#爬取bilibili的python关键字的视频并返回标题和链接组成的数据字典
    i=2
    url_0='https://search.bilibili.com/video?keyword=Python'
    resp_0=requests.get(url_0)
    html=resp_0.text
    while i<=50:
        url='https://search.bilibili.com/video?keyword=Python'+'&page=%s'%i
        i=i+1
        time.sleep(1)
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
