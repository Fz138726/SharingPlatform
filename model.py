#用戶类




class USER(object):

    username=""
    password=""
    name=""
    age=-1
    detail=""
    def __init__(self,username,password,name,age,detail):
        self.username=username
        self.password=password
        self.age=age
        self.name=name
        self.detail=detail



class Course(object):
    id=-1
    course_name=""#课程名
    platform_name=""#平台名
    course_type=""#课程类型
    course_url=""#课程地址
    def __init__(self,course_name,platform_name,course_type,course_url):
        self.course_name=course_name
        self.course_type=course_type
        self.course_url=course_url
        self.platform_name=platform_name


