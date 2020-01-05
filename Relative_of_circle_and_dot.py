# ！/usr/bin/env python 
# -*- coding:utf-8 -*-
# author: peterZhi time:2020/1/5
#输入圆心坐标与任意一点，判断其余圆的关系

import turtle
import math
r=100
x1,y1=eval(input("请输入圆心坐标:"))
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write("("+str(x1)+","+str(y1)+")")
turtle.dot(5,"black")

turtle.penup()
turtle.goto(x1,y1-r)
turtle.pendown()
turtle.circle(r)

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()

x2,y2=eval(input("请输入顶点坐标:"))
deg=math.degrees(math.atan( (y2-y1) / (x2-x1) ))
turtle.goto(x2,y2)
turtle.dot(10,"red")
turtle.write("("+str(x2)+","+str(y2)+")")
length=( (x1-x2)**2 + (y1-y2)**2 )**0.5

turtle.penup()
turtle.goto(x1-100,y1-150)
turtle.pendown()

if  length == r:
    turtle.write("点("+str(x2)+","+str(y2)+")在圆上",
                 font=("华文彩云",30,"normal"))
elif  length > r:
    turtle.write("点(" + str(x2) + "," + str(y2) + ")在圆外",
                 font=("华文彩云", 30, "normal"))
else:
    turtle.write("点(" + str(x2) + "," + str(y2) + ")在圆内",
                 font=("华文彩云", 30, "normal"))

turtle.hideturtle()
turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.showturtle()
turtle.circle(0,deg)

turtle.done()
