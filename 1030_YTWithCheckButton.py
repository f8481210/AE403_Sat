#匯入套件
from pytube import YouTube
import tkinter as tk
import threading

#定義全域變數，儲存目前下載進度
progress = 0     

#定義進度條函式    
def showProgress(stream,chunk,bytes_remaining):
    size = stream.filesize
        
    global progress
    preProgress = progress
        
    currentProgress = (size - bytes_remaining)*100 // size
    progress = currentProgress
        
    if preProgress != progress:
            scale.set(progress)
            window.update()
            print("目前進度： " + str(progress) + "%")
    if progress == 100: 
            print("下載完成！")

#定義下載影片的函式
def onClick():
    
    #定義全域變數
    global var
    #將var的值設成entry中的內容
    var.set(entry.get())
    #點擊之後將button反灰(不能點選)
    button.config(state=tk.DISABLED)
     #例外處理
    try:
        #取得網址及下載
        yt = YouTube(var.get(),
                     on_progress_callback=showProgress)
        
        #確認是否要下載音樂
        if onlyMusic.get():
            stream = yt.streams.filter(only_audio=True).first()
        else:
            stream = yt.streams.first()
        #下載
        stream.download()
        
    #發生例外
    except:
        print("下載失敗")
        
    #按鈕恢復正常
    button.config(state=tk.NORMAL)
        
#定義thread函式，執行onClick
def thread():
    threading.Thread(target=onClick).start()

"""建立基本視窗"""
window = tk.Tk()
window.title("YouTube下載器")
window.geometry("500x150")

#視窗固定，使用者不能拉大小
window.resizable(False,False)

#創建label元件
label = tk.Label(window,text = "請輸入YouTube影片網址")
label.pack()

#建立var變數來存取entry的內容
var = tk.StringVar()

#創建entry元件
entry = tk.Entry(window, width = 50)
entry.pack()

#建立onlyMusic變數來存check的內容
onlyMusic = tk.BooleanVar()

#創建Checkbutton元件
check = tk.Checkbutton(window, text = "只有音樂", variable = onlyMusic,
                       onvalue = True, offvalue = False)
check.pack()

#創建button元件
button = tk.Button(window, text = "下載",command = thread)
button.pack()

#創建scale元件
scale = tk.Scale(window, label='進度條', from_=0, to=100,
             orient=tk.HORIZONTAL,
             length=200, showvalue=False,
             tickinterval=0)
scale.pack()

#開始運行視窗程式
window.mainloop()



