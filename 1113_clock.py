#1113_clock
import turtle

tur = turtle.Turtle()

def number(num):
    tur.penup()
    tur.forward(200)
    tur.write(num)
    tur.back(200)
    tur.pendown()
    tur.right(30)
    
#設定turtle方向 0右 90上 180左 270下
tur.seth(90)

number(12)
for i in range(1,12):
    number(i)

#結束
turtle.done()
turtle.exitonclick()