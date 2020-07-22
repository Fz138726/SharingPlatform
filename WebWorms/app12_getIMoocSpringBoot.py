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




def getInfoFromIMoocForSpringBoot():
    courseItem = []

    # urls = ["https://www.imooc.com/course/list?c=csharp" + "&page={}".format(str(i)) for i in range(1, num)]
    urls="https://www.imooc.com/course/list?c=springboot"
    res=requests.get(urls)
    soup=BeautifulSoup(res.text,"html.parser")
    courseCardContain=soup.select(".course-card-container")
    # print(courseCardContain)

    # conn,cursor= get_Conn() #连接数据库
    for item in courseCardContain:
        CourseName=item.select(".course-card-name")[0].text
        CourseURL="https://www.imooc.com"+item.select("a")[0]["href"] #https://www.imooc.com/learn/1238
        course=Course(CourseName,"iMooc","program",CourseURL)
        courseItem.append(course)
        # print(CourseName,CourseURL) #测试



        #此处添加可添加SQL代码
        """...."""
        # close_conn()

    return courseItem




print(getInfoFromIMoocForSpringBoot())   #测试输出结果
# # getInfoFromIMoocForSpringBoot()