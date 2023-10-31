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
    """
      parameters: []
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                user:
                  type: string
                  description: 用户名
                  example: dog4
                pwd:
                  type: string
                  description: 密码
                  example: test12345
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  data:
                    type: object
                    properties:
                      user:
                        type: string
                    required:
                      - user
                    x-apifox-orders:
                      - user
                    x-apifox-ignore-properties: []
                  msg:
                    type: string
                required:
                  - success
                  - data
                  - msg
                x-apifox-orders:
                  - success
                  - data
                  - msg
                x-apifox-ignore-properties: []
              examples:
                '1':
                  summary: 成功示例
                  value:
                    success: true
                    data:
                      user: dog4
                    msg: 用户创建成功
      x-run-in-apifox: https://www.apifox.cn/web/project/3455002/apis/api-118633935-run
      security: []
    """
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
                        if insetintouser == ():
                            content = json.dumps(formatres(True,{
                            "user":param.get("user"),
                        },"用户创建成功"),ensure_ascii=False)
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

'''
所以实际上在sql文件中的那两个函数，其实目的就是定义接受值  看上面   
然后就是建立函数，写sql语句进行表格查询  插入  删除等操作
上面的我懂了，但是我还想问一下怎么确定两个类之间的关系呀
我们这个不需要做表关联，所以其实这两个类是互不影响的，至于确定是哪个用户发表的内容，
实际上我是靠前端代码实现的，这里我应该要跟你说一下啊，就是这个代码我改了一个地方，这个就是最关键的
所以登录之后会存储在前端，但是那个其实是暂时的，我之后还会改一下代码做本地持久化存储
到时候我请求的时候就会重新从前端读取用户名，传到添加留言的api去，然后你写的数据库操作函数，也就是接收这个作为参数传进去的
能听懂吧？
能，那我们这个有管理员吗
看情况，有余力就弄，这个也不是必须的
'''