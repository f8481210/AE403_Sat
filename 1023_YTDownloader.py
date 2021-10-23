#1023_YTDownloader
#匯入pytube模組內的YouTube
from pytube import YouTube

#定義全域變數，儲存目前下載進度
progress = 0    

def showProgress(stream,chunk,bytes_remaining):
        #總檔案大小
        size = stream.filesize
        #上次執行showProgress的進度
        global progress
        preProgress = progress
        #目前下載進度(總大小-剩餘大小)除總大小 = 已下載百分比
        #全部大小 - 剩餘大小 = 已經下載多少 *100/總大小
        currentProgress = (size - bytes_remaining)*100 // size
        progress = currentProgress

        if progress == 100:
            print("下載完成！")
        
        elif preProgress != progress:
            print("目前進度： " + str(progress) + "%")
    
   
#建立YouTube物件，並指定on_progress_callback函式
yt = YouTube("https://www.youtube.com/watch?v=1zUNR6m1c20",
             on_progress_callback=showProgress)

#從yt內的所有串流中，篩選出只有音樂的串流，並從此串流抓出第一個串流
stream = yt.streams.first()

#下載串流，並選擇資料夾及檔案名稱
stream.download()

