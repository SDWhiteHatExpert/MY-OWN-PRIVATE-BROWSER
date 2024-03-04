import sys
from PyQt5.QtCore  import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QWidget

#Made by TECHY SDX any customizations you need you can change yourself here #


class MainWindow(QMainWindow):
   def __init__(self, parent: QWidget | None = ..., flags: WindowFlags | WindowType = ...) -> None:
      super().__init__(parent, flags)
      self.browser = QWebEngineView()
      self.browser.setUrl(QUrl('http://www.google.com'))
      self.setCentralWidget(self.browser)
      self.showMaximized()
      # Create a toolbar and add some

      navbar = QToolBar()
      self.addToolBar()


      back_btn = QAction('Back ; self')
      back_btn.triggered.connect(self.browser.back)
      navbar.addAction(back_btn)


      forward_btn = QAction ('Forward' , self)
      forward_btn.triggered.connect(self.browser.forward)
      navbar.addAction(forward_btn)


      reload_btn = QAction('Reload' , self)
      reload_btn.triggered.connect(self.browser.reload)
      navbar.addAction(reload_btn)


      home_btn =  QAction('Home' , self)
      home_btn.triggered.connect(self.navigate_home)
      navbar.addAction(home_btn)


      self.url_bar = QLineEdit()
      self.url_bar.returnPressed.connect(self.load_url)
      navbar.addWidget(self.url_bar)
      

      self.browser.urlChanged.connect(self.update_url)



def navigate_home(self):
   self.browser.urlChanged.connect(self.update_url)
   self.load_url("youtube.com/channel/UC6oiipXum2z05GVKv4VbrZQ")



def navigate_to_url(self):
   url = self.url.bar.text()
   self.browser.setUrl(QUrl(url))


def update_url_bar(self , q):
   self.url_bar.setText(q.toString())
   #self.url_bar.set

app = QApplication(sys.argv)
QApplication.setApplicationName('MY OWN PRIVATE BROWSER ')
window = MainWindow()
app.exec_()



#Enjoy the Browser