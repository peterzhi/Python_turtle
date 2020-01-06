# ！/usr/bin/env python 
# -*- coding:utf-8 -*-
# author: peterZhi time:2020/1/6
#随机抽取扑克牌,显示出其花色与大小
import random
t_num=random.randint(1,13)
t_sort=random.randint(1,4)
num=sort = "1"

#判断花色类型
if t_sort == 1:
    sort = "方块"
elif t_sort == 2:
    sort = "梅花"
elif t_sort == 3:
    sort = "红桃"
else:
    sort = "黑桃"

#判断扑克数值大小
if t_num == 1:
    num = "1"
elif t_num == 2:
    num = "2"
elif t_num == 3:
    num = "3"
elif t_num == 4:
    num = "4"
elif t_num == 5:
    num = "5"
elif t_num == 6:
    num = "6"
elif t_num == 7:
    num = "7"
elif t_num == 8:
    num = "8"
elif t_num == 9:
    num = "9"
elif t_num == 10:
    num = "10"
elif t_num == 11:
    num = "J"
elif t_num == 12:
    num = "Q"
elif t_num == 13:
    num = "K"
elif t_num == 14:
    num = "A"

print("随机抽取的扑克牌为%s%s"%(sort,num))
