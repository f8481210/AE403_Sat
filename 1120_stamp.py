#檔名：1120_stamp
import turtle
tur = turtle.Turtle()
tur.color('blue')
tur.shape('turtle')

tur.penup()
for i in range(5,100,2):
    tur.stamp()
    tur.forward(i)
    tur.right(10)
    
    
turtle.exitonclick()