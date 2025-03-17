from PyQt5.QtWidgets import QApplication                        #Подключение модулей и функций
from PyQt5.QtWidgets import QMainWindow                         #Подключение модулей и функций
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent      #Подключение модулей и функций 
from PyQt5.QtCore import QUrl                                   #Подключение модулей и функций    
from ui import Ui_MainWindow                                    #Подключение модулей и функций
from pathlib import Path                                        #Подключение модулей и функций
#Создание класса
class Widget(QMainWindow):
    def __init__(self,):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.media = QMediaPlayer(self)
        self.media.setVideoOutput(self.ui.video_widget)
    
#Создание окнаp
app=QApplication([])
ex=Widget()
ex.show()

#Создание функций
def get_video_f():
    video=None
    dataa=ex.ui.calendar.selectedDate()
    if dataa:
        video_n=f"{dataa.day()}.avi"
        
        pathname = f"videos\\{video_n}"
        path_obj = Path(pathname)
        
        if path_obj.exists() and path_obj.is_file():
            contentUrl = QUrl.fromLocalFile(pathname)
            video = QMediaContent(contentUrl)
    
    
    return video
    
def stop():
    if get_video_f():
        ex.media.stop()
        

def start_vid_f():
    video=get_video_f()
    if video:
        ex.media.stop()
        ex.media.setMedia(video)
        ex.media.play()
    elif ex.media.currentMedia():
        ex.media.stop()    


def f_data():
    dataa=ex.ui.calendar.selectedDate()
    print(dataa.day())
    if ex.ui.check_start.isChecked():
        start_vid_f()
        
        

def start_btn_f():
    start_vid_f()



def stop_btn_f():
    stop()
#Обраотка кликов
ex.ui.calendar.selectionChanged.connect(f_data)

ex.ui.start_btn.clicked.connect(start_btn_f)

ex.ui.stop_btn.clicked.connect(stop_btn_f)


app.exec_()