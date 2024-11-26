from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtWidgets import QToolBar, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QUrl, QSettings
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QTextEdit, QInputDialog, QMessageBox
from PyQt6.QtWidgets import QApplication, QTextEdit, QInputDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QFont
import sys
import os
def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and bundled apps """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
class MainWindow(QMainWindow):
    HOME_URL = "https://search.freakybob.site/"
    DARK_MODE_STYLE = """
    QMainWindow {
        background-color: #2b2b2b;
        color: white;
    }
    QToolBar, QLineEdit, QStatusBar {
        background-color: #3c3c3c;
        color: white;
    }
    QLineEdit {
        border: 1px solid #5c5c5c;
        border-radius: 5px;
        padding: 5px;
    }
    QToolButton {
        background-color: #3c3c3c;
        color: white;
        border-radius: 5px;
        padding: 5px;
    }
    QToolButton:hover {
        background-color: #5c5c5c;
    }
    QTabWidget::pane {
        border-top: 1px solid #444;
        background-color: #2b2b2b;
    }
    QTabBar::tab {
        background-color: #3c3c3c;
        color: white;
        padding: 10px;
        border-top-left-radius: 0px;
        border-top-right-radius: 5px;
        border-bottom-right-radius: 5px;
        border-bottom-left-radius: 0px;
    }
    QTabBar::tab:selected {
        background-color: #5c5c5c;
        color: white;
    }
    QTabBar::tab:hover {
        background-color: #4c4c4c;
        color: white;
    }
    QStatusBar {
        border-top: 2px solid #3c3c3c;
    }
    QMenuBar {
        background-color: #3c3c3c;
        color: white;
    }
    QMenuBar::item:selected {
        background-color: #5c5c5c;
    }
    QDockWidget {
        background-color: #3c3c3c;
    }
    """
    PINK_MODE_STYLE = """
    QMainWindow {
        background-color: #ff8ad1;
        color: white;
    }
    QToolBar, QLineEdit, QStatusBar {
        background-color: #ff8ad1;
        color: #2a2a2a;
    }
    QLineEdit {
        border: 1px solid #ff6bc2;
        border-radius: 5px;
        padding: 5px;
    }
    QToolButton {
        background-color: #ff8ad1;
        color: #2a2a2a;
        border-radius: 5px;
        padding: 5px;
    }
    QToolButton:hover {
        background-color: #ff6bc2;
    }
    QTabWidget::pane {
        border: none;
        background-color: #ff8ad1;
    }
    QTabBar::tab {
        background-color: #b61396;
        color: #21f0d7;
        padding: 10px;
        border-top-left-radius: 0px;
        border-top-right-radius: 5px;
        border-bottom-right-radius: 5px;
        border-bottom-left-radius: 0px;
    }
    QTabBar::tab:selected {
        background-color: #923872;
        color: #19eada;
    }
    QTabBar::tab:hover {
        background-color: #b91c81;
        color: #84f4f9;
    }
    QStatusBar {
        border-top: 2px solid #ff8ad1;
    }
    QMenuBar {
        background-color: #ff8ad1;
        color: #2a2a2a;
    }
    QMenuBar::item:selected {
        background-color: #ff6bc2;
    }
    QDockWidget {
        background-color: #ff8ad1;
    }
    """
    BLUE_MODE_STYLE = """
    QMainWindow {
        background-color: #3a4e8f;
        color: white;
    }
    QToolBar, QLineEdit, QStatusBar {
        background-color: #2a3f7a;
        color: white;
    }
    QLineEdit {
        border: 1px solid #6a7d99;
        border-radius: 5px;
        padding: 5px;
    }
    QToolButton {
        background-color: #2a3f7a;
        color: white;
        border-radius: 5px;
        padding: 5px;
    }
    QToolButton:hover {
        background-color: #4a5f8b;
    }
    QTabWidget::pane {
        border-top: 1px solid #3a4e8f;
        background-color: #2a3f7a;
    }
    QTabBar::tab {
        background-color: #1e2a56;
        color: white;
        padding: 10px;
        border-top-left-radius: 0px;
        border-top-right-radius: 5px;
        border-bottom-right-radius: 5px;
        border-bottom-left-radius: 0px;
    }
    QTabBar::tab:selected {
        background-color: #4a5f8b;
        color: white;
    }
    QTabBar::tab:hover {
        background-color: #3a4e8f;
        color: white;
    }
    QStatusBar {
        border-top: 2px solid #2a3f7a;
    }
    QMenuBar {
        background-color: #2a3f7a;
        color: white;
    }
    QMenuBar::item:selected {
        background-color: #4a5f8b;
    }
    QDockWidget {
        background-color: #2a3f7a;
    }
    """
    GREEN_MODE_STYLE = """
    QMainWindow {
        background-color: #2e8b57;
        color: white;
    }
    QToolBar, QLineEdit, QStatusBar {
        background-color: #227a4b;
        color: white;
    }
    QLineEdit {
        border: 1px solid #4caf50;
        border-radius: 5px;
        padding: 5px;
    }
    QToolButton {
        background-color: #227a4b;
        color: white;
        border-radius: 5px;
        padding: 5px;
    }
    QToolButton:hover {
        background-color: #4caf50;
    }
    QTabWidget::pane {
        border-top: 1px solid #2e8b57;
        background-color: #227a4b;
    }
    QTabBar::tab {
        background-color: #1d6f3c;
        color: white;
        padding: 10px;
        border-top-left-radius: 0px;
        border-top-right-radius: 5px;
        border-bottom-right-radius: 5px;
        border-bottom-left-radius: 0px;
    }
    QTabBar::tab:selected {
        background-color: #4caf50;
        color: white;
    }
    QTabBar::tab:hover {
        background-color: #388e3c;
        color: white;
    }
    QStatusBar {
        border-top: 2px solid #227a4b;
    }
    QMenuBar {
        background-color: #227a4b;
        color: white;
    }
    QMenuBar::item:selected {
        background-color: #4caf50;
    }
    QDockWidget {
        background-color: #227a4b;
    }
    """
    RED_MODE_STYLE = """
    QMainWindow {
        background-color: #F44336;
        color: white;
    }
    QToolBar, QLineEdit, QStatusBar {
        background-color: #D32F2F;
        color: white;
    }
    QLineEdit {
        border: 1px solid #E57373;
        border-radius: 5px;
        padding: 5px;
    }
    QToolButton {
        background-color: #D32F2F;
        color: white;
        border-radius: 5px;
        padding: 5px;
    }
    QToolButton:hover {
        background-color: #E57373;
    }
    QTabWidget::pane {
        border-top: 1px solid #F44336;
        background-color: #D32F2F;
    }
    QTabBar::tab {
        background-color: #C62828;
        color: white;
        padding: 10px;
        border-top-left-radius: 0px;
        border-top-right-radius: 5px;
        border-bottom-right-radius: 5px;
        border-bottom-left-radius: 0px;
    }
    QTabBar::tab:selected {
        background-color: #E57373;
        color: white;
    }
    QTabBar::tab:hover {
        background-color: #D32F2F;
        color: white;
    }
    QStatusBar {
        border-top: 2px solid #D32F2F;
    }
    QMenuBar {
        background-color: #D32F2F;
        color: white;
    }
    QMenuBar::item:selected {
        background-color: #E57373;
    }
    QDockWidget {
        background-color: #D32F2F;
    }
    """
    PURPLE_MODE_STYLE = """
    QMainWindow {
        background-color: #9C27B0;
        color: white;
    }
    QToolBar, QLineEdit, QStatusBar {
        background-color: #8E24AA;
        color: white;
    }
    QLineEdit {
        border: 1px solid #BA68C8;
        border-radius: 5px;
        padding: 5px;
    }
    QToolButton {
        background-color: #8E24AA;
        color: white;
        border-radius: 5px;
        padding: 5px;
    }
    QToolButton:hover {
        background-color: #BA68C8;
    }
    QTabWidget::pane {
        border-top: 1px solid #9C27B0;
        background-color: #8E24AA;
    }
    QTabBar::tab {
        background-color: #7B1FA2;
        color: white;
        padding: 10px;
        border-top-left-radius: 0px;
        border-top-right-radius: 5px;
        border-bottom-right-radius: 5px;
        border-bottom-left-radius: 0px;
    }
    QTabBar::tab:selected {
        background-color: #BA68C8;
        color: white;
    }
    QTabBar::tab:hover {
        background-color: #9C27B0;
        color: white;
    }
    QStatusBar {
        border-top: 2px solid #8E24AA;
    }
    QMenuBar {
        background-color: #8E24AA;
        color: white;
    }
    QMenuBar::item:selected {
        background-color: #BA68C8;
    }
    QDockWidget {
        background-color: #8E24AA;
    }
    """
    ORANGE_MODE_STYLE = """
    QMainWindow {
        background-color: #FF9800;
        color: white;
    }
    QToolBar, QLineEdit, QStatusBar {
        background-color: #FB8C00;
        color: white;
    }
    QLineEdit {
        border: 1px solid #FFB74D;
        border-radius: 5px;
        padding: 5px;
    }
    QToolButton {
        background-color: #FB8C00;
        color: white;
        border-radius: 5px;
        padding: 5px;
    }
    QToolButton:hover {
        background-color: #FFB74D;
    }
    QTabWidget::pane {
        border-top: 1px solid #FF9800;
        background-color: #FB8C00;
    }
    QTabBar::tab {
        background-color: #F57C00;
        color: white;
        padding: 10px;
        border-top-left-radius: 0px;
        border-top-right-radius: 5px;
        border-bottom-right-radius: 5px;
        border-bottom-left-radius: 0px;
    }
    QTabBar::tab:selected {
        background-color: #FFB74D;
        color: white;
    }
    QTabBar::tab:hover {
        background-color: #F57C00;
        color: white;
    }
    QStatusBar {
        border-top: 2px solid #FB8C00;
    }
    QMenuBar {
        background-color: #FB8C00;
        color: white;
    }
    QMenuBar::item:selected {
        background-color: #FFB74D;
    }
    QDockWidget {
        background-color: #FB8C00;
    }
    """
    # That's a lot of css :sob:
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        try:
            icon_path = resource_path("icons/logo.ico")
            self.setWindowIcon(QIcon(icon_path))
        except Exception as e:
            print(f"Error loading icon: {e}")

        
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.tabs.currentChanged.connect(self.update_title)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.home_url = MainWindow.HOME_URL
        self.setCentralWidget(self.tabs)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        self.navtb = QToolBar("Navigation")
        self.addToolBar(self.navtb)

        
        back_btn = QAction(QIcon(resource_path("icons/back.png")), "Back", self)
        back_btn.setStatusTip("Go back")
        back_btn.triggered.connect(lambda: self.current_browser().back())
        self.navtb.addAction(back_btn)

        next_btn = QAction(QIcon(resource_path("icons/forward.png")), "Forward", self)
        next_btn.setStatusTip("Go forward")
        next_btn.triggered.connect(lambda: self.current_browser().forward())
        self.navtb.addAction(next_btn)

        reload_btn = QAction(QIcon(resource_path("icons/refresh.png")), "Reload", self)
        reload_btn.setStatusTip("Reload the page")
        reload_btn.triggered.connect(lambda: self.current_browser().reload())
        self.navtb.addAction(reload_btn)

        home_btn = QAction(QIcon(resource_path("icons/home.png")), "Home", self)
        home_btn.setStatusTip("Go back to home")
        home_btn.triggered.connect(self.navigate_home)
        self.navtb.addAction(home_btn)

        self.navtb.addSeparator()


        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        self.navtb.addWidget(self.urlbar)
        self.urlbar.setPlaceholderText("Enter URL...")
        logo_action = QAction(QIcon(resource_path("logo.ico")), "Logo", self.urlbar)
        self.urlbar.addAction(logo_action, QLineEdit.ActionPosition.LeadingPosition)
        self.urlbar.setClearButtonEnabled(True)

        notes_button = QAction(QIcon(resource_path("icons/notes1.png")), "Manage Notes", self)
        notes_button.setStatusTip("Manage your notes")
        notes_button.triggered.connect(self.manage_notes)
        self.navtb.addAction(notes_button)

        settings_btn = QAction(QIcon(resource_path("icons/settings.png")), "Settings", self)
        settings_btn.setStatusTip("Open Settings")
        settings_btn.triggered.connect(self.open_settings)
        self.navtb.addAction(settings_btn)

        bookmark_btn = QAction(QIcon(resource_path("icons/bookmark.png")), "Bookmark", self)
        bookmark_btn.setStatusTip("Bookmark this page!")
        bookmark_btn.triggered.connect(self.bookmark_page)
        self.navtb.addAction(bookmark_btn)

        view_bookmarks_btn = QAction(QIcon(resource_path("icons/bookmarks.png")), "Bookmarks", self)
        view_bookmarks_btn.setStatusTip("View all bookmarks")
        view_bookmarks_btn.triggered.connect(self.show_bookmarks)
        self.navtb.addAction(view_bookmarks_btn)

        view_source_btn = QAction(QIcon(resource_path("icons/source.png")), "View Source", self)
        view_source_btn.setStatusTip("View the source of the current page")
        view_source_btn.triggered.connect(self.view_page_source)
        self.navtb.addAction(view_source_btn)

        save_page_btn = QAction(QIcon(resource_path("icons/download.png")), "Save Page", self)
        save_page_btn.setStatusTip("Save the current page as HTML")
        save_page_btn.triggered.connect(self.save_page)
        self.navtb.addAction(save_page_btn)

        self.settings = QSettings("FreakyBrowse", "UserSettings")
        self.pink_mode_enabled = self.settings.value("pink_mode", False, type=bool)
        self.blue_mode_enabled = self.settings.value("blue_mode", False, type=bool)
        self.green_mode_enabled = self.settings.value("green_mode", False, type=bool)
        self.orange_mode_enabled = self.settings.value("orange_mode", False, type=bool)
        self.red_mode_enabled = self.settings.value("red_mode", False, type=bool)
        self.purple_mode_enabled = self.settings.value("purple_mode", False, type=bool)

       

        self.toggle_mode()

        
        self.add_new_tab(QUrl(self.HOME_URL), "New Tab")
        self.show()

        
        self.bookmarks = self.settings.value("bookmarks", [], type=list)

        self.settings = QSettings("Freakybob", "FreakyBrowse")
        self.home_url = self.settings.value("home_url", MainWindow.HOME_URL)

    def add_new_tab(self, qurl=None, label="New Tab"):
        if qurl is None:
        
            qurl = QUrl(self.home_url)
        browser = QWebEngineView()
        browser.setUrl(qurl)
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)
        browser.urlChanged.connect(lambda qurl, browser=browser: self.update_urlbar(qurl, browser))
        browser.loadFinished.connect(lambda _, i=i, browser=browser: self.tabs.setTabText(i, browser.page().title()))


    def tab_open_doubleclick(self, i):
        if i == -1:
            self.add_new_tab()

    def update_title(self):
        title = self.current_browser().page().title()
        self.setWindowTitle(f"{title} - FreakyBrowse, by the Freakybob Team.")
        self.update_urlbar(self.current_browser().url())

    def navigate_home(self):
        self.current_browser().setUrl(QUrl(self.home_url))

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("https")
        if q.isValid():
            self.current_browser().setUrl(q)
        else:
            QMessageBox.warning(self, "Invalid URL", "Please enter a valid URL.")

    def update_urlbar(self, q, browser=None):
        if browser != self.current_browser():
            return
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def current_browser(self):
        return self.tabs.currentWidget()

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)

    def toggle_mode(self):
        if self.pink_mode_enabled:
            self.setStyleSheet(self.PINK_MODE_STYLE)
        elif self.blue_mode_enabled:
            self.setStyleSheet(self.BLUE_MODE_STYLE)
        elif self.green_mode_enabled:
            self.setStyleSheet(self.GREEN_MODE_STYLE)
        elif self.red_mode_enabled:
            self.setStyleSheet(self.RED_MODE_STYLE)
        elif self.purple_mode_enabled:
            self.setStyleSheet(self.PURPLE_MODE_STYLE)
        elif self.orange_mode_enabled:
            self.setStyleSheet(self.ORANGE_MODE_STYLE)
        else:
            self.setStyleSheet(self.DARK_MODE_STYLE)



    def toggle_pink_mode(self, enabled):
        if enabled:
            self.orange_mode_enabled = False
            self.purple_mode_enabled = False
            self.red_mode_enabled = False
            self.dark_mode_enabled = False
            self.blue_mode_enabled = False
            self.green_mode_enabled = False
            self.pink_mode_enabled = enabled
        self.settings.setValue("pink_mode", enabled)
        self.settings.setValue("orange_mode", self.orange_mode_enabled)
        self.settings.setValue("purple_mode", self.purple_mode_enabled)
        self.settings.setValue("red_mode", self.red_mode_enabled)
        self.settings.setValue("blue_mode", self.blue_mode_enabled)
        self.settings.setValue("green_mode", self.green_mode_enabled)
        self.toggle_mode()

    def toggle_blue_mode(self, enabled):
        if enabled:
            self.orange_mode_enabled = False
            self.purple_mode_enabled = False
            self.red_mode_enabled = False
            self.dark_mode_enabled = False
            self.pink_mode_enabled = False
            self.green_mode_enabled = False
        self.blue_mode_enabled = enabled
        self.settings.setValue("pink_mode", self.pink_mode_enabled)
        self.settings.setValue("orange_mode", self.orange_mode_enabled)
        self.settings.setValue("purple_mode", self.purple_mode_enabled)
        self.settings.setValue("red_mode", self.red_mode_enabled)
        self.settings.setValue("blue_mode", enabled)
        self.settings.setValue("green_mode", self.green_mode_enabled)
        self.toggle_mode()
        

    def toggle_green_mode(self, enabled):
        if enabled:
            self.orange_mode_enabled = False
            self.purple_mode_enabled = False
            self.red_mode_enabled = False
            self.dark_mode_enabled = False
            self.pink_mode_enabled = False
            self.blue_mode_enabled = False
        self.green_mode_enabled = enabled
        self.settings.setValue("pink_mode", self.pink_mode_enabled)
        self.settings.setValue("orange_mode", self.orange_mode_enabled)
        self.settings.setValue("purple_mode", self.purple_mode_enabled)
        self.settings.setValue("red_mode", self.red_mode_enabled)
        self.settings.setValue("blue_mode", self.blue_mode_enabled)
        self.settings.setValue("green_mode", enabled)
        self.toggle_mode()
    def toggle_orange_mode(self, enabled):
        if enabled:
            self.purple_mode_enabled = False
            self.red_mode_enabled = False
            self.dark_mode_enabled = False
            self.pink_mode_enabled = False
            self.blue_mode_enabled = False
            self.green_mode_enabled = False
        self.orange_mode_enabled = enabled
        self.settings.setValue("pink_mode", self.pink_mode_enabled)
        self.settings.setValue("orange_mode", enabled)
        self.settings.setValue("purple_mode", self.purple_mode_enabled)
        self.settings.setValue("red_mode", self.red_mode_enabled)
        self.settings.setValue("blue_mode", self.blue_mode_enabled)
        self.settings.setValue("green_mode", self.green_mode_enabled)
        self.toggle_mode()
    def toggle_purple_mode(self, enabled):
        if enabled:
            self.red_mode_enabled = False
            self.dark_mode_enabled = False
            self.pink_mode_enabled = False
            self.blue_mode_enabled = False
            self.green_mode_enabled = False
            self.orange_mode_enabled = False
        self.purple_mode_enabled = enabled
        self.settings.setValue("pink_mode", self.pink_mode_enabled)
        self.settings.setValue("orange_mode", self.orange_mode_enabled)
        self.settings.setValue("purple_mode", enabled)
        self.settings.setValue("red_mode", self.red_mode_enabled)
        self.settings.setValue("orange_mode", self.orange_mode_enabled)
    def toggle_red_mode(self, enabled):
        if enabled:
            self.dark_mode_enabled = False
            self.pink_mode_enabled = False
            self.blue_mode_enabled = False
            self.green_mode_enabled = False
            self.orange_mode_enabled = False
            self.purple_mode_enabled = False
        self.red_mode_enabled = enabled
        self.settings.setValue("pink_mode", self.pink_mode_enabled)
        self.settings.setValue("orange_mode", self.orange_mode_enabled)
        self.settings.setValue("purple_mode", self.purple_mode_enabled)
        self.settings.setValue("red_mode", enabled)
        self.settings.setValue("blue_mode", self.blue_mode_enabled)
        self.settings.setValue("green_mode", self.green_mode_enabled)
        self.toggle_mode()

    def open_settings(self):
        settings_dialog = QDialog(self)
        settings_dialog.setWindowTitle("Settings")
        
       
        settings_dialog.resize(100, 100)  

        
        layout = QVBoxLayout()

        style_button = QPushButton("Style Settings")
        style_button.clicked.connect(self.open_style_settings)
        layout.addWidget(style_button)

        browser_stg_button = QPushButton("Browser Settings")
        browser_stg_button.clicked.connect(self.open_browser_settings)
        layout.addWidget(browser_stg_button)
        
        info_button = QPushButton("Info")
        info_button.clicked.connect(self.open_info_button)
        layout.addWidget(info_button)
        
        close_button = QPushButton("Close")
        close_button.clicked.connect(settings_dialog.accept)

        layout.addWidget(close_button)

        settings_dialog.setLayout(layout)
        settings_dialog.exec() 
    def open_info_button(self):
        info_dialog = QDialog(self)
        info_dialog.setWindowTitle("FreakyBrowse info\n")
        layout = QVBoxLayout()
        
        title_label = QLabel("FreakyBrowse Info")
        title_font = QFont("Comic Sans", 18, QFont.Weight.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        below_label1 = QLabel("FreakyBrowse, by the Freakybob Team.")
        below_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        below_label2 = QLabel("Version: 1.9")
        below_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        below_label1_font = QFont("Comic Sans", 9, QFont.Weight.DemiBold)
        below_label1.setFont(below_label1_font)
        below_label2_font = QFont("Comic Sans", 9, QFont.Weight.DemiBold)
        below_label2.setFont(below_label2_font)

        title_label2 = QLabel("Sorta History")
        title_label2_font = QFont("Comic Sans", 18, QFont.Weight.Bold)
        title_label2.setFont(title_label2_font)
        title_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info_label = QLabel("FreakyBrowse was made on Oct 13th 2024. It first started out as code stolen from stackoverflow but was updated to work and look better.\nThe first time we started to try to distibrute FreakyBrowse, it was saying it was a trojan. It was a false positive from what wish13yt used to turn the code into an exe.\nWe now use Pyinstaller so you don't get any false positives when downloading FreakyBrowse!")
        info_label_font = QFont("Comic Sans", 9, QFont.Weight.DemiBold)
        info_label.setFont(info_label_font)
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        your_info_title = QLabel("Your Info")
        your_info_title_font = QFont("Comic Sans", 13, QFont.Weight.Bold)
        your_info_title.setFont(your_info_title_font)
        your_info_title.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        your_info_label = QLabel("FreakyBrowse does not use your personal info. Every website you go to is your choice of giving THEM your info. You do have to agree to the Privacy Policy that we have for search.freakybob.site. You can find it by pressing 'here' on search.freakybob.site")
        your_info_label_font = QFont("Comic Sans", 9, QFont.Weight.DemiBold)
        your_info_label.setFont(your_info_label_font)
        your_info_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        gpl_label = QLabel("Rights?")
        gpl_label_font = QFont("Comic Sans", 13, QFont.Weight.Bold)
        gpl_label.setFont(gpl_label_font)
        gpl_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        info_label2 = QLabel("Everything is GPL-3")
        info_label2_font = QFont("Comic Sans", 9, QFont.Weight.DemiBold)
        info_label2.setFont(info_label2_font)
        info_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title_label)
        layout.addWidget(below_label1)
        layout.addWidget(below_label2)
        layout.addWidget(title_label2)
        layout.addWidget(info_label)
        layout.addWidget(your_info_title)
        layout.addWidget(your_info_label)
        layout.addWidget(gpl_label)
        layout.addWidget(info_label2)

        close_button = QPushButton("Close")
        close_button.clicked.connect(info_dialog.accept)
        layout.addWidget(close_button)
        info_dialog.setLayout(layout)
        info_dialog.exec()
    def open_browser_settings(self):
        browser_dialog = QDialog(self)
        browser_dialog.setWindowTitle("Browser Settings")
        layout = QVBoxLayout()

        
        use_google_checkbox = QCheckBox("Use Google's main page?")
        use_google_checkbox.setChecked(self.home_url == "https://google.com")
        use_google_checkbox.stateChanged.connect(
            lambda state: self.toggle_homepage_url(state, home_url_label))
        layout.addWidget(use_google_checkbox)
        warning_label = QLabel("This does not bring you to https://google.com when you start the app. This just changes the Home button location and new tab location :P")
        home_url_label = QLabel(f"Current Home URL: {self.home_url}")
        layout.addWidget(warning_label)
        layout.addWidget(home_url_label)

        close_button = QPushButton("Close")
        close_button.clicked.connect(browser_dialog.accept)
        layout.addWidget(close_button)

        browser_dialog.setLayout(layout)
        browser_dialog.exec()

    def toggle_homepage_url(self, state, home_url_label):
        if state == 2:
            self.home_url = "https://google.com"
        else:
            self.home_url = "https://search.freakybob.site/"

        
        MainWindow.HOME_URL = self.home_url
        home_url_label.setText(f"Current Home URL: {self.home_url}")
        self.settings.setValue("home_url", self.home_url)

    def open_style_settings(self):
        style_dialog = QDialog(self)
        style_dialog.setWindowTitle("Style Settings")
        layout = QVBoxLayout()

        pink_mode_checkbox = QCheckBox("Enable Pink Mode")
        pink_mode_checkbox.setChecked(self.pink_mode_enabled)
        pink_mode_checkbox.stateChanged.connect(lambda: self.toggle_pink_mode(pink_mode_checkbox.isChecked()))
        layout.addWidget(pink_mode_checkbox)

        blue_mode_checkbox = QCheckBox("Enable Blue Mode")
        blue_mode_checkbox.setChecked(self.blue_mode_enabled)
        blue_mode_checkbox.stateChanged.connect(lambda: self.toggle_blue_mode(blue_mode_checkbox.isChecked()))
        layout.addWidget(blue_mode_checkbox)

        green_mode_checkbox = QCheckBox("Enable Green Mode")
        green_mode_checkbox.setChecked(self.green_mode_enabled)
        green_mode_checkbox.stateChanged.connect(lambda: self.toggle_green_mode(green_mode_checkbox.isChecked()))
        layout.addWidget(green_mode_checkbox)

        red_mode_checkbox = QCheckBox("Enable Red Mode")
        red_mode_checkbox.setChecked(self.red_mode_enabled)
        red_mode_checkbox.stateChanged.connect(lambda: self.toggle_red_mode(red_mode_checkbox.isChecked()))
        layout.addWidget(red_mode_checkbox)

        orange_mode_checkbox = QCheckBox("Enable Orange Mode")
        orange_mode_checkbox.setChecked(self.orange_mode_enabled)
        orange_mode_checkbox.stateChanged.connect(lambda: self.toggle_orange_mode(orange_mode_checkbox.isChecked()))
        layout.addWidget(orange_mode_checkbox)

        purple_mode_checkbox = QCheckBox("Enable Purple Mode")
        purple_mode_checkbox.setChecked(self.purple_mode_enabled)
        purple_mode_checkbox.stateChanged.connect(lambda: self.toggle_purple_mode(purple_mode_checkbox.isChecked()))
        layout.addWidget(purple_mode_checkbox)

        close_button = QPushButton("Close")
        close_button.clicked.connect(style_dialog.accept)
        layout.addWidget(close_button)

        style_dialog.setLayout(layout)
        style_dialog.exec()
        
    def manage_notes(self):
        notes_dialog = QDialog(self)
        notes_dialog.setWindowTitle("Notes Manager")
        notes_dialog.setMinimumSize(600, 400)

        layout = QVBoxLayout()

    
        notes_list = QListWidget()
        layout.addWidget(notes_list)

    
        saved_notes = self.settings.value("notes", {}, type=dict)
        for note_name in saved_notes.keys():
            notes_list.addItem(note_name)

    
        button_layout = QHBoxLayout()

    
        add_note_button = QPushButton("Add Note")
    
        add_note_button.clicked.connect(lambda: self.add_note_dialog(notes_list, saved_notes))
        button_layout.addWidget(add_note_button)

    
        delete_note_button = QPushButton("Delete Note")
        delete_note_button.clicked.connect(lambda: self.delete_note(notes_list, saved_notes))
        button_layout.addWidget(delete_note_button)

        layout.addLayout(button_layout)

    
        note_viewer = QTextEdit()
        note_viewer.setReadOnly(False)
        layout.addWidget(note_viewer)

    
        upload_image_button = QPushButton("Insert Image")
        upload_image_button.clicked.connect(lambda: self.insert_image(note_viewer))
        layout.addWidget(upload_image_button)

    
        def load_note_content():
            selected_item = notes_list.currentItem()
            if selected_item:
                note_content = saved_notes.get(selected_item.text(), "")
                note_viewer.setHtml(note_content)
            else:
                note_viewer.clear()
        notes_list.itemSelectionChanged.connect(load_note_content)
          

    
        def save_note_content():
            selected_item = notes_list.currentItem()
            if selected_item:
                saved_notes[selected_item.text()] = note_viewer.toHtml()
                self.settings.setValue("notes", saved_notes)

        note_viewer.textChanged.connect(save_note_content)

        notes_dialog.setLayout(layout)
        notes_dialog.exec()

    def add_note_dialog(self, notes_list, saved_notes):
        text, ok = QInputDialog.getText(self, "Add Note", "Enter note name:")
    
   
        if not ok:
            return

   
        if text:
            notes_list.addItem(text)
        saved_notes[text] = ""

   
        self.settings.setValue("notes", saved_notes)

   
        item = notes_list.findItems(text, Qt.MatchFlag.MatchExactly)[0]
        notes_list.setCurrentItem(item)

   
        note_viewer = self.findChild(QTextEdit) 
        note_viewer.setHtml("")
        note_viewer.setFocus()


    def delete_note(self, notes_list, saved_notes):
        selected_item = notes_list.currentItem()
        if selected_item:
            note_name = selected_item.text()
        confirm = QMessageBox.question(self, "Delete Note", f"Are you sure you want to delete '{note_name}'?", 
                                       QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                       QMessageBox.StandardButton.No)
        
        if confirm == QMessageBox.StandardButton.Yes:
            
            notes_list.takeItem(notes_list.row(selected_item))
            
            
            saved_notes.pop(note_name, None)
            
            
            self.settings.setValue("notes", saved_notes)
    def insert_image(self, note_viewer):
        image_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if not image_path:
            return 
    
        width, ok = QInputDialog.getInt(self, "Image Width", "Enter image width:", 300, 1, 10000, 1)
        if not ok:
            return

        height, ok = QInputDialog.getInt(self, "Image Height", "Enter image height:", 300, 1, 10000, 1)
        if not ok:
            return

    
        file_extension = image_path.split('.')[-1].lower()

        if file_extension == "gif":
        
            note_viewer.insertHtml(f'<img src="{image_path}" width="{width}" height="{height}" alt="GIF">')
        else:
        
            note_viewer.insertHtml(f'<img src="{image_path}" width="{width}" height="{height}">')




    def bookmark_page(self):
        url = self.current_browser().url().toString()
        if url not in self.bookmarks:
            self.bookmarks.append(url)
            self.settings.setValue("bookmarks", self.bookmarks)
            QMessageBox.information(self, "Bookmark Added", f"{url} has been bookmarked.")
        else:
            QMessageBox.warning(self, "Already Bookmarked", "This page is already in your bookmarks.")

    def show_bookmarks(self):
        bookmarks_dialog = QDialog(self)
        bookmarks_dialog.setWindowTitle("Bookmarks")

        layout = QVBoxLayout()

        for url in self.bookmarks:
            bookmark_layout = QHBoxLayout()

            bookmark_label = QLabel(url)
            bookmark_layout.addWidget(bookmark_label)

            open_btn = QPushButton("Open")
            open_btn.clicked.connect(lambda _, url=url: self.add_new_tab(QUrl(url), url))
            bookmark_layout.addWidget(open_btn)

            delete_btn = QPushButton("Delete")
            delete_btn.clicked.connect(lambda _, url=url: self.delete_bookmark(url, bookmarks_dialog))
            bookmark_layout.addWidget(delete_btn)

            layout.addLayout(bookmark_layout)

        close_button = QPushButton("Close")
        close_button.clicked.connect(bookmarks_dialog.accept)
        layout.addWidget(close_button)

        bookmarks_dialog.setLayout(layout)
        bookmarks_dialog.exec() # bookmarks_dialog.exec_() is deprecated in PyQt6

    def delete_bookmark(self, url, dialog):
        if url in self.bookmarks:
            self.bookmarks.remove(url)
            self.settings.setValue("bookmarks", self.bookmarks)
            dialog.accept()
            self.show_bookmarks()

    def view_page_source(self):
     
        current_browser = self.current_browser()
        
       
        current_browser.page().toHtml(lambda html: self.show_html(html))
    def show_html(self, html):
        html_viewer = QDialog(self)
        html_viewer.setWindowTitle("Page Source")
        html_viewer.setMinimumSize(800, 600)
        layout = QVBoxLayout()
        html_text_edit = QTextEdit()
        html_text_edit.setPlainText(html)
        html_text_edit.setReadOnly(True)
        layout.addWidget(html_text_edit)
        close_button = QPushButton("Close")
        close_button.clicked.connect(html_viewer.accept)
        layout.addWidget(close_button)
        html_viewer.setLayout(layout)
        html_viewer.exec() # html_viewer.exec_() is deprecated in PyQt6

    def save_page(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page", "", "HTML Files (*.html)")
        if filename:
            page = self.current_browser().page()
            page.toHtml(lambda html: self.write_to_file(filename, html))

    def write_to_file(self, filename, content):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        QMessageBox.information(self, "Page Saved", f"Page has been saved to {filename}.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("FreakyBrowse")
    app.setWindowIcon(QIcon("logo.ico")) 
    
    window = MainWindow()
    app.exec() # app.exec_() is deprecated in PyQt6
#I am steve :33333 GREG GREG GREG I HATE YOU !!!!VFYUGEIHLJ:K:D<MNFKGILEHQODJLK:A?<
