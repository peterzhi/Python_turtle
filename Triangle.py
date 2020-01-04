#输入3个点，画出三角形并标注角度
import turtle
import math
x1,y1=eval(input("第一个顶点坐标:"))
x2,y2=eval(input("第二个顶点坐标:"))
x3,y3=eval(input("第三个顶点坐标:"))
a=((x3-x2)**2+ (y3-y2)**2)**0.5
b=((x3-x1)**2+ (y3-y1)**2)**0.5
c=((x1-x2)**2+ (y1-y2)**2)**0.5
A=math.degrees(math.acos((b*b+ c*c- a*a) / (2*b*c)))
B=math.degrees(math.acos((a*a+ c*c- b*b) / (2*a*c)))
C=math.degrees(math.acos((b*b+ a*a- c*c) / (2*a*b)))

turtle.showturtle()
turtle.hideturtle()
turtle.pensize(2)

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()

turtle.goto(x2,y2)
turtle.write("("+ str(x2)+ ","+ str(y2)+ ")"+ str(int(B))+ "°")
turtle.goto(x3,y3)
turtle.write("("+ str(x3)+ ","+ str(y3)+ ")"+ str(int(C))+ "°")
turtle.goto(x1,y1)
turtle.write("("+ str(x1)+ ","+ str(y1)+ ")"+ str(int(A))+ "°")
turtle.done()
