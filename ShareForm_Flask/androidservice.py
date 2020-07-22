import os
from datetime import timedelta

import paginate as paginate
from flask import Flask,request,render_template,redirect,url_for, send_from_directory,current_app,flash,session
from flask_db import db
from model import Course
from functools import wraps
from initcourse import *
from page_utils import Pagination
app=Flask(__name__)
app.secret_key='sjk#%#*(1315'#密key
app.permanent_session_lifetime=timedelta(hours=1)#失效时间

inituser()
courses=initcourse()
coursetypes=initcoursetypes()


def wrapper(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if session.get("username"):
            ret=func(*args,**kwargs)
            return ret
        else :
            return redirect("/login")
    return inner

#主页面



@app.route('/',methods=['POST','GET'])
@wrapper
def index():

    if request.method=='POST':

        pass
    else:
        #分贡显示
        parer_obj=Pagination(request.args.get("page",1),len(courses),
                             request.path,request.args,per_page_count=20)
        print(request.path)
        print(request.args)
        index_list=courses[parer_obj.start:parer_obj.end]
        html=parer_obj.page_html()
        return render_template('index.html',index_list=index_list,html=html,coursetypes=coursetypes)


#按类型查找
@app.route('/search_course/<string:course_type>',methods=['POST','GET'])
@wrapper
def search_course(course_type):
    #查找
    courses = db.select_course_type_accuracy(course_type)
    #分页显示
    parer_obj = Pagination(request.args.get("page", 1), len(courses),
                           request.path, request.args, per_page_count=20)
    print(request.path)
    print(request.args)
    index_list = courses[parer_obj.start:parer_obj.end]
    html = parer_obj.page_html()
    return render_template('index.html',index_list=index_list,html=html,coursetypes=coursetypes)

#按平台查找
@app.route('/search',methods=['POST','GET'])
@wrapper
def search():



    if request.method=='POST':
        if request.form['type']=='全平台':
            keyword=request.form['keyword']
            courses=db.select_course_name(keyword)
        else:
            keyword=request.form['keyword']
            platform=request.form['type']
            courses=db.select_platform_course_name(platform,keyword)
            #分页显示
        parer_obj = Pagination(request.args.get("page", 1), len(courses),
                                request.path, request.args, per_page_count=20)
        print(request.path)
        print(request.args)
        index_list = courses[parer_obj.start:parer_obj.end]
        html = parer_obj.page_html()
        return render_template('index.html',index_list=index_list,html=html,coursetypes=coursetypes)
    else:
        # 分页显示
        courses=db.select_all_course()
        parer_obj = Pagination(request.args.get("page", 1), len(courses),
                               request.path, request.args, per_page_count=20)
        print(request.path)
        print(request.args)
        index_list = courses[parer_obj.start:parer_obj.end]
        html = parer_obj.page_html()
        return render_template('index.html', index_list=index_list, html=html, coursetypes=coursetypes)


#登入
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form['userID']
        password=request.form['password']
        if isempty(username,password):
            return render_template('login.html',detail="用戶名或密码不能为空")
        if user_db.select_user_name(username)==None:
            return render_template('login.html',detail="用戶名输入錯误")
        if user_db.select_password(username,password)==None:
            return render_template('login.html',detail="密码输入錯误")
        user=user_db.select_user(username,password)
        session['username']=username
        session['password']=password
        return redirect(url_for('index'))

    else:
        return render_template('login.html',detail="")

#注册
@app.route('/register',methods=['POST','GET'])
def register():
    if request.method=='POST':
        username=request.form['userID']
        password=request.form['password']
        if isempty(username,password):
            return render_template('register.html', detail="用戶名或密码不能为空")
        if user_db.select_user_name(username)==None:
            user_db.insert_user_table(User(username=username,password=password,name="",detail=""))
            return redirect(url_for('login'))
        else:
            return render_template('register.html',detail="用戶名已被注册")

    else:
        return render_template('register.html',detail="")
#登出
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
#判断是否为空
def isempty(username,password):
    if len(username) == 0 or len(password) == 0:
        return True
    if username.isspace() or password.isspace():
        return True
    return False



if __name__=='__main__':
    app.run(debug=True)