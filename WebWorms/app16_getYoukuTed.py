import requests
from bs4 import BeautifulSoup
import pymysql

#Course类
class Course(object):
    course_name = ""  # 课程名
    platform_name = ""  # 平台名
    course_type = ""  # 课程类型
    course_url = ""  # 课程地址

    def __init__(self,courseName,platformName,courseType,courseUrl):
        self.course_name=courseName
        self.platform_name=platformName
        self.course_type=courseType
        self.course_url=courseUrl


#建立连接
def get_Conn():
    conn=pymysql.connect(host="127.0.0.1",user="root",password="root",db="course")
    cursor=conn.cursor()
    return conn, cursor

def close_conn(conn, cursor):
    if conn:
        conn.close()
    if cursor:
        cursor.close()




def getInfoFromTedForChina():

    courseItem = []

    # urls = ["https://www.imooc.com/course/list?c=photo" + "&page={}".format(str(i)) for i in range(1, num)]
    url="https://www.ted.com/topics/china"
    res=requests.get(url)
    soup=BeautifulSoup(res.text,"html.parser")
    # print(soup.select(".row")[0].select("a")[0]["href"])
    colContent=soup.select(".col")
    # print(colContent[0])

    for item in colContent:
        if len(item)==0:
            continue
        else :
            #"https://www.ted.com/"
            tedHref=item.find_all("a")
            if len(tedHref)!=0:
                tedHrefContent="https://www.ted.com/"+tedHref[0]["href"]

            tedTopic=item.select(".media__message")
            if len(tedTopic)!=0:
                tedTopicContent=tedTopic[0].select("a")[0].text
            course=Course(tedHrefContent,"Ted","lecture",tedHrefContent)
            # print(tedHrefContent,tedTopicContent)
            courseItem.append(course)


    # conn,cursor= get_Conn() #连接数据库

     #此处添加可添加SQL代码
    # close_conn()

    return courseItem




# print(getInfoFromIMoocForDesign())   #测试输出结果
# print(getInfoFromTedForChina())
# print(getInfoFromTedForChina())