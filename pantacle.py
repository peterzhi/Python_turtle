# ！/usr/bin/env python 
# -*- coding:utf-8 -*-
# author: peterZhi time:2020/1/2
import turtle #导入turtle包

turtle.penup() #改变初始位置
turtle.goto(-50,50)
turtle.pendown()
turtle.color('red','red') #设置边框颜色与填充颜色为红色
turtle.hideturtle() #隐藏箭头
turtle.begin_fill() #起笔

count=1 #计时器记录边数
while count<=5: #控制绘制条数
    turtle.forward(100) #向前移动制定距离100
    turtle.right(144) #向右转144°
    count+=1 #下一条

turtle.end_fill() #完成填充

turtle.done()
