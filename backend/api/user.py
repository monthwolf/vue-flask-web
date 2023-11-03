#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 导入flask模块
from flask import Blueprint,Flask,request
# 导入json模块
import json
# 导入自定义模块
from Utils.utils import *
# 导入mySQL_config
from sql.user import UserTB
# 创建类的实例
user = Blueprint('user',__name__)
 
# 登录
# @param：{string}     user         用户名
# @param：{string}     pwd          密码
# @returns：{json}
@user.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':    #主要的操作都是api处理，像一些传参，格式化，以及最后的返回值
        # POST、GET:
        # request.form获得所有post参数放在一个类似dict类中,to_dict()是字典化  
        # 单个参数可以通过request.form.to_dict().get("xxx","")获得
        param = request.form.to_dict()      #这里的request会从前端获取参数，你看我上次给你的api文档就知道，前端会传递用户名和密码过来
        if param.get("user") != None and param.get("pwd") != None:  #在这里就会被转化为字典（dictionary）{username:xxx,pwd:xxx},然后在下面进行读取
            if param.get("user") != "" and len(param.get("user")) < 15 and param.get("pwd") != "" and len(param.get("pwd")) < 20:
                user = UserTB(param.get("user"),param.get("pwd"))  #这里就用到了在数据库处理代码里面的那个类
                user = user.selectUser()  #在这里就用到了UserTB类中的函数  查询用户  然后会返回查询结果，我们就可以通过user接受返回值，然后再在下面进行进一步判断
                if user == ():
                    content = json.dumps(formatres(False,{},"用户名不存在"),ensure_ascii=False)
                else:
                    userPwd = UserTB(param.get("user"),param.get("pwd"))
                    userPwd = userPwd.selectUserPwd()
                    if userPwd == ():
                        content = json.dumps(formatres(False,{},"用户名或密码不正确"),ensure_ascii=False)
                    else:
                        content = json.dumps(formatres(True,{
                            "user":param.get("user"),
                        },"登录成功"),ensure_ascii=False)#在这里，其实之前原作者写的返回是(True,{},"登录成功")不会向前端返回数据信息
            else:       #但是我在这里返回了用户名，前端读取，存在了一个对象里面，可以给你看看
                content = json.dumps(formatres(False,{},"用户名密码为空或者过长"),ensure_ascii=False)
        else:
             content = json.dumps(formatres(False,{},"请检查参数"),ensure_ascii=False)
    else:
        content = json.dumps(formatres(False,{},"101"))
    resp = Response_headers(content)
    return resp

# 注册
# @param：{string}     user         用户名
# @param：{string}     pwd          密码
# @returns：{json}
@user.route('/reg',methods=['post'])
def reg():
    if request.method == 'POST':
        param = request.form.to_dict()  
        if param.get("user") != None and param.get("pwd") != None:
            if param.get("user") != "" and len(param.get("user")) < 8 and param.get("pwd") != "" and len(param.get("pwd")) < 20:
                user = UserTB(param.get("user"),param.get("pwd"))  #UserTB只需要接受user和pwd，就是用户名和密码
                user = user.selectUser() 
                if user != ():
                    content = json.dumps(formatres(False,{},"用户名已存在"),ensure_ascii=False)
                else:
                    try:
                        insetintouser = UserTB(param.get("user"),param.get("pwd"))
                        insetintouser = insetintouser.insetinto()
                        if insetintouser != ():
                            content = json.dumps(formatres(True,{
                            "user":param.get("user")},"用户创建成功"),ensure_ascii=False)
                        else:
                            content = json.dumps(formatres(False,{},"用户创建失败"),ensure_ascii=False)
                    except:
                        content = json.dumps(formatres(False,{},"用户创建失败，可能用户名过长"),ensure_ascii=False)
            else:
                content = json.dumps(formatres(False,{},"用户名密码为空或者过长"),ensure_ascii=False)
        else:
             content = json.dumps(formatres(False,{},"请检查参数"),ensure_ascii=False)
    else:
        content = json.dumps(formatres(False,{},"101"))
    resp = Response_headers(content)
    return resp
