#1016_radiobutton
#匯入tkinter模組
import tkinter as tk
"""創建基本視窗"""
window = tk.Tk()

window.title("單選按鈕")
window.geometry('200x200')
#創建可變動的tk字串變數
string = tk.StringVar()
string1 = tk.StringVar()
"""顯示所選擇的文字"""
def selection():
    label.config(text="我是" + string1.get() + "，我喜歡" + string.get())

#創建label元件
label = tk.Label(window, bg='#f00', text='尚未選擇')
label.pack()

#創建Radiobutton元件
radio1 = tk.Radiobutton(window,
                    text='Minecraft Python',
                    variable=string, value='Minecraft Python',
                    command=selection)
radio1.pack()

#創建Radiobutton元件
radio2 = tk.Radiobutton(window,
                    text='Pygame',
                    variable=string, value='Pygame',
                    command=selection)
radio2.pack()

#創建Radiobutton元件
radio3 = tk.Radiobutton(window,
                    text='Tkinter',
                    variable=string, value='Tkinter',
                    command=selection)
radio3.pack()

radio4 = tk.Radiobutton(window,
                    text='男生',
                    variable=string1, value='男生',
                    command=selection)
radio4.pack()

radio5 = tk.Radiobutton(window,
                    text='女生',
                    variable=string1, value='女生',
                    command=selection)
radio5.pack()

#開始跑視窗
window.mainloop()


