#檔名：1120_clock
#載入模組
import turtle,time,datetime

def number(num):
    t0.penup()
    t0.forward(200)
    t0.write(num)
    t0.back(200)
    t0.pendown()

#創建turtle
turtle.setup(600,600)

t0 = turtle.Turtle()
t0.speed(10)
t0.seth(90)

#step1 時鐘刻度
for i in range(1,13):
    t0.right(30)
    number(i)
    
#step2 時針、分針、秒針
#控制時針分針
update = True
#控制秒針
updateSecond = True

while True:
    #取得現在時間
    now = datetime.datetime.now()
    h = now.hour % 12
    m = now.minute
    s = now.second
    
    if update:
        #畫時針
        hour = turtle.Turtle()
        #朝上
        hour.seth(90)
        #一圈12小時(30度/小時)
          #分鐘也會影響時針，每60分鐘影響30度(0.5度/分鐘)
        hour.right(h*30+m*0.5)
        hour.forward(140)
        
        #畫分針
        minute = turtle.Turtle()
        minute.seth(90)
        #6度/分鐘
        minute.right(m*6)
        minute.forward(200)
        
        update = False
    
    if updateSecond:
        #畫秒針
        second = turtle.Turtle()
        second.seth(90)
        #6度/秒鐘
        second.right(s*6)
        second.forward(220)
        updateSecond = False
        
    #step3 讓秒針一直轉，指針會依據現在時間移動到正確位置
    time.sleep(1)
    now = datetime.datetime.now()
    mnew = now.minute
    
    updateSecond = True
    second.clear()#清除
    second.reset()#重畫
    
    if mnew != m :
        update = True
        hour.clear()
        hour.reset()
        minute.clear()
        minute.reset()
    
    
turtle.done()
turtle.exitonclick()
