# ！/usr/bin/env python 
# -*- coding:utf-8 -*-
# author: peterZhi time:2020/1/2

import turtle

turtle.showturtle()
turtle.hideturtle()
turtle.pensize(4)
turtle.goto(200,0)
turtle.goto(200,200)
turtle.goto(0,200)
turtle.goto(0,0)

turtle.penup()
turtle.goto(100,100)
turtle.pendown()

turtle.goto(-100,100)
turtle.goto(-100,-100)
turtle.goto(100,-100)
turtle.goto(100,100)

turtle.goto(200,200)
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.goto(-100,100)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(-100,-100)
turtle.penup()
turtle.goto(100,-100)
turtle.pendown()
turtle.goto(200,0)
turtle.done()
