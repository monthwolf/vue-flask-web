#!/usr/bin/python3
# -*- coding:utf-8 -*-

from mySQL_config import func

# 定义用户数据表类
class User_DataTB:
    ''' 用户数据增加、查询、修改'''
    def __init__(self,user,content=None,img=None,create_time=None):
        self.user = user
        self.create_time = create_time
        self.img=img
        self.content = content
    
    # 1.查询所有卡片内容和对应的用户 def getAllCards(self)
    def getAllCards(self):
        sql="select * from user_data"
        result = func(sql)
        return result
    def getMyCards(self):
        sql="select * from user_data where USERNAME='%s'"%(self.user)
        result = func(sql)
        return result
    
    # 2.添加卡片内容和用户（再加上图片，但图片不是必选项） def addCard(self)
    def addCard(self):
        sql="INSERT INTO user_data (USERNAME,CONTENT,IMG) VALUES ('%s','%s','%s')"%(self.user,self.content,self.img)
        result = func(sql)
        return result
    
    # 3.删除卡片（通过本用户名查询他发布的所有卡片，自定义删减）def delCard(self)
    # 这个应该分开写，一个是查询用户写的所有卡片，一个是在用户选定之后删除

    def delCard(self):
       #根据用户名，发布时间，内容查询卡片并删除
       #同时操作两张表，利用user_data里的USERNAM，CONTENT以及user里的content对他进行相应操作
       sql="DELETE FROM user_data WHERE USERNAME = '%s' AND CREATE_TIME = '%s'"%(self.user,self.create_time)
       result = func(sql)
       return result