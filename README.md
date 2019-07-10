i
### 项目介绍
#### 模块概述
- 用户模块
- CMDB模块
- 发版系统
- 监控模块
- 日志模块
- 工单系统
- 数据库管理平台
- 堡垒机模块

#### 项目安装

首先安装好python基础环境，vue基础环境nodejs
项目开发基础环境：
	1、python == 3.7.1
	2、django == 2.2.3
	3、vue    == 2.9.6

> 安装django
```shell
# 安装虚拟环境
pip install virtualenvwrapper-win
配置环境变量 WORK_HOME=E:\PycharmProjects\Envs
# 启动虚拟环境
mkvirtualenv pxDevops
# 安装django
pip install django
# 初始化项目
进入到新创建的目录下 E:\PycharmProjects\Projects\pxDvops
django-admin startproject pxDevops
进入到创建的项目的目录下，创建一个应用
django-admin startapp users
```
> 安装vue
```shell
# 安装cnpm
npm install -g cnpm --registry=https://registry.npm.taobao.org
# 安装vue
cnpm install -g vue vue-cli
# 初始化vue项目
进去到项目目录下 E:\PycharmProjects\Projects\pxDvops\
vue init webpack pxdevops-front
```
> 生成项目依赖
```shell
# 生成整个环境的依赖
pip freeze > requirements.txt
# 生成整个项目的依赖
pip install pipreqs
pirpreqs ./  # 进入到项目根目录执行
```
#### 项目运行
```shell
进入到项目目录下
# 运行django
python manager.py runserver 0.0.0.0:8000
# 运行vue
npm run dev
```
