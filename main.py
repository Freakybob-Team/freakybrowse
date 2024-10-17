from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://search.freakybob.site/"))
        # please dont use the new tab page unless u are actually theming it around a new tab <3
        # its hard to remember to update both pages
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

       
        back_btn = QAction("Back", self)
        back_btn.setStatusTip("Go back")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        
        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Go forward")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

       
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload the page")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)  
        navtb.addAction(home_btn)

        navtb.addSeparator()

        
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading the page")
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        self.show()

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle(f"{title} - FreakyBrowse, by the Freakybob Team.")
        self.update_urlbar(self.browser.url())

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://search.freakybob.site/"))

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("https")  
        self.browser.setUrl(q)

    def update_urlbar(self, q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("FreakyBrowse, by the Freakybob Team")
    window = MainWindow()
    app.exec_()
