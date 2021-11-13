#檔名；1113_turtlecircle
import turtle
#生成烏龜
tur = turtle.Turtle()
t2 = turtle.Turtle()
'''

我想要同時有三隻烏龜
一隻畫三角形
一隻畫五邊形
一隻畫十邊形
但是 我不要他們重疊
'''
#tur.shape("square")
#tur.circle(100,360,3)

#畫筆形狀
#'arrow', 'turtle', 'circle', 'square',
#'triangle', 'classic'
t2.shape("turtle")
#畫筆顏色
t2.pencolor('red')
#畫筆粗細
t2.pensize(10)
#t2.circle(150,360,5)
#印出字串
t2.write('安安你好',font=(20))

#結束
turtle.done()
turtle.exitonclick()