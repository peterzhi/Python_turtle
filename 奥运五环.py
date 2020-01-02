# ！/usr/bin/env python 
# -*- coding:utf-8 -*-
# author: peterZhi time:2020/1/2
import turtle
turtle.color("blue")#蓝色
turtle.circle(100)#半径100

turtle.penup()
turtle.goto(-150,0)
turtle.pendown()
turtle.color("red")
turtle.circle(100)#半径100

turtle.penup()
turtle.goto(150,0)
turtle.pendown()
turtle.color("yellow")
turtle.circle(100)#半径100

turtle.penup()
turtle.goto(-75,-150)
turtle.pendown()
turtle.color("black")
turtle.circle(100)#半径100

turtle.penup()
turtle.goto(75,-150)
turtle.pendown()
turtle.color("green")
turtle.circle(100)#半径100

turtle.done()#程序继续运行
