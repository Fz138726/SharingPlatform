import requests
from bs4 import BeautifulSoup
import pymysql
from model import Course
#连接数据库
# def get_conn():
#     conn = pymysql.connect(host="127.0.0.1", user="root", password="root", db="course")
#     cursor = conn.cursor()
#     return conn, cursor
#
# #关闭数据库
# def close_conn(conn,cursor):
#     if conn:
#         conn.close()
#     if cursor:
#         cursor.close()

#爬取课程与课程的URL
def getInfoFromImmocForPython():
    # conn=None
    # cursor=None
    # #连接数据库
    # conn,cursor=get_conn()
    #一个数组保存多个网页
    mylist=[]
    uu=0
    num=3
    url=["https://www.imooc.com/course/list?c=python"+"&page={}".format(str(i)) for i in range(1,num)]#爬取网页从第一页到num-1页
    # url="https://www.imooc.com/course/list?c=python"

    # print(url[1])

    #爬虫基本配置
    while uu<=num-2:
        req2=requests.get(url[uu])
        soup2=BeautifulSoup(req2.text,"html.parser")
        cardContainer=soup2.select(".course-card-container")

        #记录
        uu=uu+1

        #记录

        for i in cardContainer:
            courseName=i.select("h3")[0].text
            courseURL="https://www.imooc.com"+i.select("a")[0]["href"] #获得每个课程的后缀，需要自行添加网页前缀，如https://www.imooc.com/learn/1240
            course=Course(course_name=courseName,course_type="Python",course_url=courseURL,platform_name="IMOOC")
            mylist.append(course)

    return mylist
            #为数据库增加数据
            # sqlAdd = "insert into courseinfo values(%s,%s)"
            # cursor.execute(sqlAdd,(courseName,courseURL)) #上传到数据库
            # conn.commit()

    # close_conn(conn,cursor)

# getInfoFromImmocForPython()

# #输出数据库数据(测试)
# conn, cursor=get_conn()
#
# #SQL语句
# sqlSearch="select * from courseinfo"
# sqlDelete="delete from courseinfo"
# cursor.execute(sqlDelete)
# result=cursor.fetchall()
# print(result)
#
# close_conn(conn,cursor)




#获取课程名
# courseName=cardContainer[0].select("h3")
# print(courseName)


#
# cursor.close()
# conn.close()






#以下为试验
# while uu<=(num-2):
#     req=requests.get(url[uu])
#     # print(req.text)
#     soup=BeautifulSoup(req.text,"html.parser")
#     pysearchItem=soup.select(".course-card-container")
#     print(pysearchItem)
    # pysearchItem=soup.find_all("a",)
    # print(pysearchItem)

    # for i in pysearchItem:
    #     alink=i.select("a")
    #     print(alink[0]["href"])
    # uu=uu+1
