from model import Course
from selenium.webdriver import Chrome,ChromeOptions
def aiqiyi_Python():
    option=ChromeOptions()
    option.add_argument("--headless")
    browser=Chrome(options=option)
    browser.get('https://so.iqiyi.com/so/q_Python?source=input&sr=1088234053533')
    page=1
    mylist=[]
    while page<=30:
        i=1
        while i<=10:
            xpath='//*[@id="__layout"]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div/ul/li[%s]/div/div[1]/a'%i
            c=browser.find_element_by_xpath(xpath)
            course=Course(course_name=c.get_attribute('title'),course_type='Python',course_url=c.get_attribute('href'),platform_name='爱奇艺')
            mylist.append(course)
            i=i+1
        but=browser.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div/a')
        but.click()
        page=page+1
    return mylist
