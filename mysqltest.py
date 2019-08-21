__author__ = 'Administrator'
# !usr/bin/env python

# coding:utf-8

testmysql
#创建一个库 testspider
#创建一张表 t1(id int)
#在表中插入一条记录 id=1
import pymysql
#创建连接对象
db=pymysql.connect("localhost","root","123456",charset="utf8")
#创建游标
cursor=db.cursor()

cursor.execute('create database testspider;')
cursor.execute('use testspider;')
cursor.execute('create tabale t1(id int);')
cursor.execute('insert into t1 values(1);')

db.commit()
cursor.close()
db.close()