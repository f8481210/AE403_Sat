# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 23:24:36 2018

@author: Eric
"""

import turtle
tur = turtle.Turtle()

#設置畫面大小
turtle.setup(850,850)

#定義畫矩形&著色函式
def rectangle():
    tur.begin_fill()
    tur.forward(800)
    tur.right(90)
    tur.forward(200)
    tur.right(90)
    tur.forward(800)
    tur.right(90)
    tur.forward(200)
    tur.right(90)
    tur.end_fill()

def myGoto(x,y):
    tur.penup()
    tur.goto(x,y)
    tur.pendown()

#上面黑色部分
myGoto(-400,400)
tur.fillcolor(0,0,0)
rectangle()

#中間紅色部分
myGoto(-400,200)
tur.fillcolor(1,0,0)
rectangle()


#下面黃色部分
myGoto(-400,0)
tur.fillcolor(1,1,0)
rectangle()

#完成程式
turtle.done()
turtle.exitonclick()

