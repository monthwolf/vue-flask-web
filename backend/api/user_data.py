#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 导入flask模块
from flask import Blueprint,Flask,request
# 导入json模块
import json
# 导入自定义模块
from Utils.utils import *
# 导入mySQL_config
from sql.user_data import User_DataTB
from datetime import datetime
# 创建类的实例
cards = Blueprint("cards",__name__)

# 获取用户下所有卡片
# @param {string}   user    用户名
# @param
title=['username','content','img','create_time']
@cards.route("/get",methods=['GET'])
def get_cards():
    if request.method == 'GET':
        param = request.args
        if param.get("user") != None:
            user=User_DataTB(param.get("user"))
            cards = user.getMyCards()
            data=[]
            print(cards,file=open("log.txt","a"))
            if cards == ():
                content = json.dumps(formatres(False,{},"你当前未创建留言！"),ensure_ascii=False)
            else:
                # title=['username','content','img','create_time']
                for card in cards:
                    card=list(card)
                    card[-1] = card[-1].strftime('%Y-%m-%d %H:%M:%S')
                    card=dict(zip(title,card))
                    data.append(card)
                content = json.dumps(formatres(True,data,"您的所有卡片获取成功！"),ensure_ascii=False)
        else:
            content = json.dumps(formatres(False,{},"用户名为空！请检查是否登录！"),ensure_ascii=False)
    else:
        content = json.dumps(formatres(False,{},"101"))
    return content
@cards.route("/all",methods=['GET'])
def get_All():
    if request.method == 'GET':
        param = request.args
        if param.get("user") != None:
            user=User_DataTB(param.get("user"))
            cards = user.getAllCards()
            data=[]
            print(cards,file=open("log.txt","a"))
            if cards == ():
                content = json.dumps(formatres(False,{},"无留言！"),ensure_ascii=False)
            else:
                # title=['username','content','img','create_time']
                for card in cards:
                    card=list(card)
                    card[-1] = card[-1].strftime('%Y-%m-%d %H:%M:%S')
                    card=dict(zip(title,card))
                    data.append(card)
                content = json.dumps(formatres(True,data,"所有卡片获取成功！"),ensure_ascii=False)
        else:
            content = json.dumps(formatres(False,{},"用户名为空！请检查是否登录！"),ensure_ascii=False)
    else:
        content = json.dumps(formatres(False,{},"101"))
    return content
@cards.route("/add",methods=['POST'])
def add_card():
    if request.method == 'POST':
        param = request.form.to_dict()
        if param.get("user") != None and param.get("content") != None:
            if(param.get("img") != None):
                user=User_DataTB(param.get("user"),param.get("content"),param.get("img"))
            else:
                user=User_DataTB(param.get("user"),param.get("content"))
            user.addCard()
            content = json.dumps(formatres(True,{},"添加成功！"),ensure_ascii=False)
        else:
            content = json.dumps(formatres(False,{},"用户名或内容为空！请检查是否登录！"),ensure_ascii=False)
    else:
        content = json.dumps(formatres(False,{},"101"))
    return content
@cards.route("/delete",methods=['POST'])
def del_card():
    if request.method == 'POST':
        param = request.form.to_dict()
        if param.get("user") != None:
            user=User_DataTB(param.get("user"),create_time=param.get("create_time"))
            user.delCard()
            content = json.dumps(formatres(True,{},"删除成功！"),ensure_ascii=False)
        else:
            content = json.dumps(formatres(False,{},"用户名为空！请检查是否登录！"),ensure_ascii=False)
    else:
        content = json.dumps(formatres(False,{},"101"))
    return content