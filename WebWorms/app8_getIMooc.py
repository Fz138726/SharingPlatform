import requests
from bs4 import BeautifulSoup
from ShareForm_Flask.model import Course

#爬取课程与课程的URL
def getInfoFromImmocForPython():

    mylist=[]
    uu=0
    num=3
    url=["https://www.imooc.com/course/list?c=python"+"&page={}".format(str(i)) for i in range(1,num)]#爬取网页从第一页到num-1页
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
