# ！/usr/bin/env python 
# -*- coding:utf-8 -*-
# author: peterZhi time:2020/1/6

import turtle
i=0
turtle.hideturtle()
turtle.pensize(2)
turtle.goto(0,0)
turtle.dot(5,"black")

#标注原点(0,0)
turtle.penup()
turtle.goto(8,-15)
turtle.pendown()
turtle.write("O")
turtle.penup()
turtle.goto(0,0)
turtle.pendown()


#x负半轴
while i > -250:
    i-=50
    turtle.goto(i,0)
    turtle.goto(i,5)
    turtle.goto(i,0)
    turtle.penup()
    turtle.goto(i-10,-15) #标线数值摆放位置
    turtle.pendown()
    turtle.write(str(i))
    turtle.penup()
    turtle.goto(i,0)
    turtle.pendown()
else:
    turtle.goto(i-20,0)

#返回至原点
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
i=0

#y负半轴
while i > -250:
    i-=50
    turtle.goto(0,i)
    turtle.goto(5,i)
    turtle.goto(0,i)
    turtle.penup()
    turtle.goto(-20,i-5) #标线数值摆放位置
    turtle.pendown()
    turtle.write(str(i))
    turtle.penup()
    turtle.goto(0,i)
    turtle.pendown()
else:
    turtle.goto(0,i-20)

#返回至原点
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
i=0

#x正半轴
while i < 250:
    i+=50
    turtle.goto(i,0)
    turtle.goto(i,5)
    turtle.goto(i,0)
    turtle.penup()
    turtle.goto(i-5,-15) #标线数值摆放位置
    turtle.pendown()
    turtle.write(str(i))
    turtle.penup()
    turtle.goto(i,0)
    turtle.pendown()
else:
    i+=50
    turtle.goto(i,0)
    turtle.circle(0, -135) ##表示箭头
    turtle.forward(7)
    turtle.penup()
    turtle.goto(i, 0)
    turtle.pendown()
    turtle.circle(0, 270) #注意方向的变化
    turtle.forward(7)
    turtle.penup()
    turtle.goto(i, 0)
    turtle.pendown()
    turtle.circle(0, -135) #转回原始方向(x轴方向)

turtle.penup()
turtle.goto(i, -15)
turtle.pendown()
turtle.pensize(4)
turtle.write("x")
turtle.pensize(2)

#返回至原点
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
i=0

#y正半轴
while i < 250:
    i+=50
    turtle.goto(0,i)
    turtle.goto(5,i)
    turtle.goto(0,i)
    turtle.penup()
    turtle.goto(-20,i-5) #标线数值摆放位置
    turtle.pendown()
    turtle.write(str(i))
    turtle.penup()
    turtle.goto(0,i)
    turtle.pendown()
else:
    i+=50
    turtle.goto(0,i)
    turtle.circle(0,-45) #表示箭头
    turtle.forward(7)
    turtle.penup()
    turtle.goto(0,i)
    turtle.pendown()
    turtle.circle(0, -90)
    turtle.forward(7)
    turtle.penup()
    turtle.goto(0,i)
    turtle.pendown()
    turtle.circle(0, 135)

turtle.penup()
turtle.goto(-3, i+5)
turtle.pendown()
turtle.pensize(4)
turtle.write("y")
turtle.pensize(2)

#返回至原点
turtle.penup()
turtle.goto(0,0)
turtle.pendown()

turtle.done()
