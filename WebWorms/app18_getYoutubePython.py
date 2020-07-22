from selenium.webdriver import Chrome, ChromeOptions, ActionChains
import time
from model import Course
#Course类

# #构造浏览器对象
# broswer = Chrome()
#
# url="https://www.youtube.com/results?search_query=python"
# #滚动页面方法
# js="var q =document.documentElement.scrollTop=1000"
# js2='window.scrollTo(0, document.body.scrollHeight)'
#
# broswer.get(url)
#
# # print(broswer.page_source)
# #滚动页面参数。range值越大，滚得越多
# for i in range(3):
#     broswer.execute_script(js2)
#     time.sleep(5)
#
# #单个视频类型
# xpath='//*[@id="video-title"]'
# #列表清单的视频类型path
# xpathList='//*[@id="content"]/a'
#
# #获取html中视频信息
# contentV=broswer.find_elements_by_xpath(xpath)
# contentVList=broswer.find_elements_by_xpath(xpathList)
# # print(content[0].get_attribute("href"))

def getInfoFromYoutebeForPython():
    # 构造浏览器对象
    broswer = Chrome()

    url = "https://www.youtube.com/results?search_query=python"
    # 滚动页面方法
    js = "var q =document.documentElement.scrollTop=1000"
    js2 = 'window.scrollTo(0, document.body.scrollHeight)'

    broswer.get(url)

    # print(broswer.page_source)
    # 滚动页面参数。range值越大，滚得越多
    for i in range(3):
        broswer.execute_script(js2)
        time.sleep(5)

    # 单个视频类型
    xpath = '//*[@id="video-title"]'
    # 列表清单的视频类型path
    xpathList = '//*[@id="content"]/a'

    # 获取html中视频信息
    contentV = broswer.find_elements_by_xpath(xpath)
    contentVList = broswer.find_elements_by_xpath(xpathList)
    # print(content[0].get_attribute("href"))

    CourseItem=[]

    for item in contentVList:
        # print(item.get_attribute("href"))
        CourseNameL=item.find_element_by_id("video-title").get_attribute("title")
        CourseURLL=item.get_attribute("href")
        #获取视频列表的href
        course=Course(CourseNameL,"Youtube","program",CourseURLL)
        CourseItem.append(course)
        # print(CourseNameL,CourseURLL) #check

    for item2 in contentV:
        CourseName=item2.get_attribute("title")
        CourseURL=item2.get_attribute("href")
        if CourseURL!= None:
            course = Course(CourseName, "Youtube", "program", CourseURL)
            CourseItem.append(course)
            # print(CourseName,CourseURL) #check

    return CourseItem

# print(getInfoFromYoutebeForPython()) #check