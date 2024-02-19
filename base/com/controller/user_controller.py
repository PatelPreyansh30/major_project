from flask import render_template, redirect, request, flash
from base import app
from base.com.vo.user_vo import UserVO
from base.com.dao.user_dao import UserDAO


@app.route('/')
def user_home():
    try:
        return redirect('/login')
    except:
        return render_template('error.html', error=e)


@app.route('/register', methods=['GET', 'POST'])
def user_register():
    try:
        return render_template('/register.html')
    except Exception as e:
        return render_template('error.html', error=e)


@app.route("/login", methods=['GET', 'POST'])
def user_login():
    try:
        return render_template('login.html')
    except Exception as e:
        return render_template('error.html', error=e)
