# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:42:57 2018

@author: Eric
"""

import turtle
tur = turtle.Turtle()

#設置畫面大小
turtle.setup(650,650)

def rectangle():
    tur.begin_fill()
    tur.forward(250)
    tur.right(90)
    tur.forward(600)
    tur.right(90)
    tur.forward(250)
    tur.right(90)
    tur.forward(600)
    tur.right(90)
    tur.end_fill()
    
def myGoto(x,y):
    tur.penup()
    tur.goto(x,y)
    tur.pendown()

#左邊藍色部分
myGoto(-400,400)
tur.fillcolor("#00F")
rectangle()

#中間白色部分
myGoto(-150,400)
tur.fillcolor(1,1,1)
rectangle()


#右邊紅色部分
myGoto(100,400)
tur.fillcolor(1,0,0)
rectangle()

#完成程式
turtle.done()
turtle.exitonclick()