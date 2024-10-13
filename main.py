from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


        self.browser = QWebEngineView()

        self.browser.setUrl(QUrl("https://search.freakybob.site"))

        self.browser.loadFinished.connect(self.update_title)

        self.setCentralWidget(self.browser)

        self.status = QStatusBar()

        self.setStatusBar(self.status)

        navtb = QToolBar("Navigation")

        self.addToolBar(navtb)

        back_btn = QAction("Back", self)

        back_btn.setStatusTip("Go back!11!1")

        back_btn.triggered.connect(self.browser.back)

        navtb.addAction(back_btn)

        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Go forward!11!!")

        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload!111!!")

        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home :3")
        navtb.addAction(home_btn)

        navtb.addSeparator

        self.urlbar = QLineEdit()

        self.urlbar.returnPressed.connect(self.navigate_to_url)

        navtb.addWidget(self.urlbar)

        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop Loading!111!")

        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        self.show()


    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - FreakyBrowse, by the Freakybob Team." % title)


    def navigate_home(self):

        self.browser.setUrl(QUrl("https://search.freakybob.site"))


    def navigate_to_url(self):

        q = QUrl(self.urlbar.text())

        if q.scheme() == "":
            q.setScheme("https")
            self.browser.setUrl(q)

def update_urlbar(self, q):

    self.urlbar.setText(q.toString())

    self.urlbar.setCursorPosition(0)


app = QApplication(sys.argv)

app.setApplicationName("FreakyBrowse, by the Freakybob Team")

window = MainWindow()

app.exec_()
