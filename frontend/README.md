# 本项目为前后端分离的网页项目
## 前端技术栈
>  Vue3+Typescript+elementPlus+Router+Axios+Pinia

## 后端技术栈
> Python+Flask+pymysql

## 数据库
> Mysql  

## 项目结构
```bash
backend                          #  后端文件夹
├── Utils                        #  公共类
│   └── utils.py                 #  公共方法
├── api                          #  API接口类
│   ├── user.py                  #  用户相关API
│   └── user_data.py             #  用户留言相关API
├── mySQL_config.py              #  数据库配置文件
├── requirements.txt             #  后端依赖
├── run.py                       #  启动文件
├── sql                          #  SQL类
│   ├── user.py                  #  用户SQL方法
│   └── user_data.py             #  用户留言SQL方法
├── sqlTableFiles                #  SQL表文件
│   ├── user.sql                 #  用户表
│   └── user_data.sql            #  用户留言表
└── static                       #  静态文件
frontend                         #  前端文件夹
├── package.json                 #  前端依赖
├── public                       #  公共资源
├── src                            
│   ├── App.vue                  #  根组件
│   ├── assets                   #  资源文件夹
│   ├── components               #  组件文件夹
│   ├── main.ts                  #  入口文件
│   ├── router                   #  路由文件夹
│   ├── stores                   #  状态管理文件夹
│   └── views                    #  视图文件夹
├── tsconfig.json                #  ts配置文件
└── vue.config.js                #  vue配置文件
```
## 项目运行
### 1. 安装**vue，python，mysql**,配置好环境
### 2. 从guihub克隆项目文件
```bash
git clone '' 
```
### 3. 安装依赖
- 安装vue3框架依赖
```bash
cd frontend
npm install
npm run serve
```