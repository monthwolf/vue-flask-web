#!/usr/bin/python3
# -*- coding: utf-8 -*-

from mySQL_config import func

# 定义用户表类
class UserTB:  #就是这个类
    ''' 用户增加、查询 '''
    def __init__(self,user,pwd):#首先这里是定义了一个类，把可能用到的参数都定义了一遍，比方说这里就是用户名和密码
        self.user = user
        self.pwd = pwd
    
    # 查询用户名
    def selectUser(self):  #就是这个  下面这个字符串，就是sql语法 这个是查询  select嘛
        sql = "select * from user where USERNAME = '%s'"%self.user #下面几个函数都是操作数据库然后返回结果就行了，其实这里面的函数主要功能就是操作数据库
        result = func(sql)           #我们到api文件来看调用
        return result
    
    # 查询用户名密码
    def selectUserPwd(self): #这个也是
        sql = "select * from user where USERNAME = '%s' and PASSWORD = '%s' limit 1"%(self.user,self.pwd)
        result = func(sql)
        return result
    # 插入
    def insetinto(self): #还有下面这个  这个是插入 insert ，和他们的功能都是对应的
        sql = "INSERT INTO user (USERNAME,PASSWORD) VALUES ('%s','%s')"%(self.user,self.pwd)
        result = func(sql)
        return result

     