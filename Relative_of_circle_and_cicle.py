# ！/usr/bin/env python 
# -*- coding:utf-8 -*-
# author: peterZhi time:2020/1/5
#判断两个圆的位置关系
#分别输入两个圆心的坐标与半径，在界面中显示他们的位置关系

import turtle
import math
#输入数据
x1,y1,r1=eval(input("请输入第一个点的坐标及半径:"))
x2,y2,r2=eval(input("请输入第二个点的坐标及半径:"))

r=r1+r2 #r为半径和
distance=( (x1-x2)**2 + (y1-y2)**2 )**0.5 #圆心距
aver_x=(x1+x2) / 2;aver_y=(y1+y2) / 2; #圆心中点
max_r=max(r1,r2) #半径较大值
min_r=min(r1,r2) #半径较小值

#对于角度公式分母为0的处理
if math.fabs(x2-x1) == 0:
    deg=0
else:
    deg=math.degrees(math.atan( (y2-y1) / (x2-x1) )) #旋转角度

turtle.pensize(2)
turtle.hideturtle()

#画出第一个圆，标明其坐标
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.dot(5,"black")
turtle.penup()
turtle.goto(x1,y1-15)
turtle.pendown()
turtle.write("R1("+str(x1)+","+str(y1)+")")
turtle.penup()
turtle.goto(x1,y1-r1)
turtle.pendown()
turtle.circle(r1)

#画出第二个圆，标明其坐标
turtle.penup()
turtle.goto(x2,y2)
turtle.pendown()
turtle.write("R2("+str(x2)+","+str(y2)+")")
turtle.dot(5,"black")
turtle.penup()
turtle.goto(x2,y2-r2)
turtle.pendown()
turtle.circle(r2)

#连接圆心
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.circle(0,deg)

turtle.penup()
turtle.goto(min(x1,x2)-2*max_r,min(y1,y2)-50-max_r)
turtle.pendown()


#判断位置关系
if  distance > r:
    turtle.color("red")
    turtle.write("两个圆的位置是相离!",
                 font=("华文彩云", 30, "normal"))
elif  distance == r:
    turtle.color("red")
    turtle.write("两个圆的位置是相切!",
                 font=("华文彩云", 30, "normal"))
elif distance > math.fabs(y2-y1):
    turtle.color("red")
    turtle.write("两个圆的位置是相交!",
                 font=("华文彩云", 30, "normal"))
elif  distance == math.fabs(y2-y1):
    turtle.color("red")
    turtle.write("两个圆的位置是内切!",
                 font=("华文彩云", 30, "normal"))
else:
    turtle.color("red")
    turtle.write("两个圆的位置是内含!",
                 font=("华文彩云", 30, "normal"))

turtle.done()
