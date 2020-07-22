from selenium.webdriver import Chrome, ChromeOptions, ActionChains
import time

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


#构造浏览器对象
broswer = Chrome()

url="https://www.youtube.com/results?search_query=python"
#滚动页面方法
js="var q =document.documentElement.scrollTop=1000"
js2='window.scrollTo(0, document.body.scrollHeight)'

broswer.get(url)

# print(broswer.page_source)
#滚动页面参数。range值越大，滚得越多
for i in range(3):
    broswer.execute_script(js2)
    time.sleep(5)

#单个视频类型
xpath='//*[@id="video-title"]'
#列表清单的视频类型path
xpathList='//*[@id="content"]/a'

#获取html中视频信息
contentV=broswer.find_elements_by_xpath(xpath)
contentVList=broswer.find_elements_by_xpath(xpathList)
# print(content[0].get_attribute("href"))

def getInfoFromYoutebeForPython():
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