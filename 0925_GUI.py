# 檔案名稱：0925_GUI
import tkinter as tk
import tkinter.messagebox

def clickMe():
    tkinter.messagebox.showinfo(title = '提示', message = '好痛！')

window = tk.Tk()
#window設定
window.title('NN的GUI')
window.geometry('300x300')

#元件
label = tk.Label(window,text='請輸入文字',bg='#000',fg='#FFF')
label.pack()

entry = tk.Entry(window,width = 30)
entry.pack()

button = tk.Button(window,text = '點我',command = clickMe,bg='#FF0')
button.pack()

#視窗執行
window.mainloop()

'''
#色碼表
RGB
紅色：#F00 #FF0000
綠色：#0F0 #00FF00
藍色：#00F #0000FF

紫色：#FF00FF
黃色：#FFFF00



'''



