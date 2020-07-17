import os

from flask import Flask,request,render_template,redirect
from flask_db import db
from model import Course

from initcourse import initcourse,initcoursetypes

app=Flask(__name__)

courses=initcourse()
coursetypes=initcoursetypes()


@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        pass
    else:
        return render_template('index.html',courses=courses,coursetypes=coursetypes)



@app.route('/search_course/<string:course_type>',methods=['POST','GET'])
def search_course(course_type):
    courses = db.select_course_name(course_type)
    return render_template('index.html',courses=courses,coursetypes=coursetypes)

@app.route('/search',methods=['POST','GET'])
def search():
    if request.method=='POST':
        if request.form['type']=='按平台':
            platform_name=request.form['keyword']
            courses=db.select_platform_name(platform_name)
        elif request.form['type']=='按课程':
            course_name = request.form['keyword']
            courses = db.select_platform_name(course_name)
        return render_template('index.html',courses=courses,coursetypes=coursetypes)
    else:
        return render_template('index.html',coursetypes=coursetypes)









if __name__=='__main__':
    app.run(debug=True)