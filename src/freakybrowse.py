# Hai there! Welcome to the main file of FreakyBrowse!
# If ya see any issues, plz make an issue on our github!
# Feel free to add anything or fix anything!
# - Freakybob-Team <3

# Comments were done by @5quirre1, you're very welcome gusy

# Known bugs:
# - Closing the tab before a new one will cause an about:blank page
# - oceanic_blue_mode does not work
# - api

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtWidgets import QToolBar, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QAction
from PyQt6.QtCore import QUrl, QSettings
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QTextEdit, QInputDialog, QMessageBox
from PyQt6.QtWidgets import QApplication, QTextEdit, QInputDialog
from PyQt6.QtCore import Qt
from PyQt6.QtNetwork import QNetworkReply
from PyQt6.QtCore import QObject, pyqtSignal, QThread
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineUrlRequestInterceptor, QWebEngineProfile
import requests
import mimetypes
import sys
import os
from pypresence import Presence
from pypresence.exceptions import InvalidPipe
import argparse
from pysafebrowsing import SafeBrowsing
import json
import subprocess

parser = argparse.ArgumentParser(description='Parser for FreakyBrowse')
parser.add_argument('--url', action="store", dest='url', default="https://search.freakybob.site")

key_file = "api_key.json"
sb_key = None
news_key = None
downloadIsCompleted = "False"

if (os.path.exists(key_file)):
    print("Safe Browsing API key found!")
else:
    sb_key = "no key"
if sb_key == "no key":
    print("Warning: No Safe Browsing API key provided. Safe Browsing features will be disabled.")
else:
    try:
        sBrowsing = SafeBrowsing(sb_key)
        print("Safe Browsing initialized successfully.")
    except Exception as e:
        print(f"Error initializing Safe Browsing: {e}")
        sBrowsing = None

# change this when new version release - wish
appname = "FreakyBrowse 2.5"
app = QApplication(sys.argv)
try:
    sBrowsing = SafeBrowsing(sb_key) # type: ignore
except:
    print("debug start sbrowsing 404")
parser.add_argument('--name', action="store", dest='name', default=appname)
try:
    args = parser.parse_args()
except:
    print("No arguments found")
try:
    appname = args.name
    app.setApplicationName(appname)
    print(appname)
except AttributeError:
    print("[debug] no arg given via --name; proceeding with default")
#rpc 
RPC = None
haveDiscord = None
try:
    RPC = Presence("1312584606637101156")
    RPC.connect()
    RPC.update(
        details="Browsing the interwebs!",
        buttons=[{"label": "Get FreakyBrowse", "url": "https://github.com/Freakybob-Team/Freakybrowse/releases/latest"}],
        large_image="icon.png",
        large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
    )
    haveDiscord = "True"
except InvalidPipe:
    print("")
    haveDiscord = "False"
except Exception as e:
    print("")
    haveDiscord = "False"

# hello this does the http request ig - wish
# mwah https://stackoverflow.com/questions/42942295/pyqt-webengine-set-http-headers
# screw that above thread try this https://stackoverflow.com/questions/50786186/qwebengineurlrequestinterceptor-not-working - wish from like 2 months later
# screw that above thread - wish, the same day
# yeah screw this
# please fix later & uncomment

#class NWUrlRequestInterceptor(QWebEngineUrlRequestInterceptor):
#    def __init__(self):
#        super(QWebEngineUrlRequestInterceptor, self).__init__()
#
#    def interceptRequest(self, info):
#        print("I think GPC is on! Try it out here: https://global-privacy-control.glitch.me/")
#        info.setHttpHeader("Sec-GPC", "1")

#gteg
def resource_path(relative_path):
    """No use really since no exe but too lazy to fix everything"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class DownloadManagerWindow(QDialog):
    def __init__(self, parent=None):
        super(DownloadManagerWindow, self).__init__(parent)
        # the normal stuff for the window
        self.setWindowTitle("Download Manager")
        self.download_manager = DownloadManager(self)

        # connect signals from the download manager to right place
        self.download_manager.download_progress.connect(self.update_progress)
        self.download_manager.download_complete.connect(self.download_complete)
        self.download_manager.download_error.connect(self.download_error)

        # set up the window layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # the label and input field for the url
        self.url_label = QLabel("URL:")
        layout.addWidget(self.url_label)
        self.url_input = QLineEdit()
        layout.addWidget(self.url_input)

        # the label and input field for the file name
        self.file_name_label = QLabel("File name and extension (optional):")
        layout.addWidget(self.file_name_label)
        self.file_name_input = QLineEdit()
        layout.addWidget(self.file_name_input)

        # the download button
        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.start_download)
        layout.addWidget(self.download_button)

        # a progress bar to show the progress
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        # a label to show the status
        self.status_label = QLabel("Status:")
        layout.addWidget(self.status_label)
        # inherit the URL
        # try:
        #     self.url_input.setText(iUrl)
        # except:
        #     return
    def update_progress(self, progress):
        # updaye the progress bar
        self.progress_bar.setValue(progress)

    def download_complete(self, file_name):
        # show the download complete message gregd
        self.status_label.setText(f"Download complete: {file_name}")
        downloadIsCompleted = "True"
        self.progress_bar.setValue(100)

    def download_error(self, error_message):
        # error error error error erorr eorro eir
        self.status_label.setText(f"Error: {error_message}")

    def start_download(self):
        # get the url and file name
        url = self.url_input.text()
        file_name = self.file_name_input.text().strip()

        # if no url is provided show an errorgrefgdaa
        if not url:
            self.status_label.setText("Error: URL is required.")
            return

        # if no file name is give it gives a default one
        if not file_name:
            file_name = self.download_manager.get_file_name(url)

        # start the download and restart the progress bar
        self.progress_bar.setValue(0)
        self.status_label.setText("Downloading...")
        self.download_manager.get(url, file_name)


class DownloadManager(QObject):
    # the error, progress, and complete signals
    download_progress = pyqtSignal(int)
    download_complete = pyqtSignal(str)
    download_error = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super(DownloadManager, self).__init__(parent)
        self.parent = parent

    def get(self, url, file_name):
        # create a worker and thread for the download
        self.thread = QThread(self)
        self.worker = DownloadWorker(url, file_name)
        self.worker.moveToThread(self.thread)

        # connect the signals from the worker to the slots in the thread
        self.thread.started.connect(self.worker.start)
        self.worker.download_progress.connect(self.download_progress.emit)
        self.worker.download_complete.connect(self.download_complete.emit)
        self.worker.download_error.connect(self.download_error.emit)

        # connect the signals from the thread to the worker
        self.worker.download_complete.connect(self.thread.quit)
        self.worker.download_complete.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        # start start start start start start start start start start start start start start start start start start 
        self.thread.start()

    def get_file_name(self, url):
        # if no file name, it say downloaded_file
        file_name = os.path.basename(url.split("?")[0])
        if not file_name:
            return "downloaded_file"

        # this fucking sucks
        mime_type, _ = mimetypes.guess_type(file_name)
        if mime_type:
            file_extension = mimetypes.guess_extension(mime_type)
            if file_extension and not file_name.endswith(file_extension):
                file_name += file_extension
        return file_name


class DownloadWorker(QObject):
    # the error, progress, and complete signals again
    download_progress = pyqtSignal(int)
    download_complete = pyqtSignal(str)
    download_error = pyqtSignal(str)

    def __init__(self, url, file_name):
        super(DownloadWorker, self).__init__()
        # ensure that the url is good
        self.url = url if url.startswith("http") else "http://" + url
        self.file_name = file_name

    def start(self):
        try:
            # make the request and download the fileg
            with requests.get(self.url, stream=True) as r:
                r.raise_for_status()  # raise an error if fail

                # get the file size
                total_length = int(r.headers.get('content-length', 0))
                if total_length == 0:
                    self.download_error.emit("Unable to determine file size.")
                    return

                # idk why this is still here, i think it was cause I downloaded a zip and it turned into .pyz and I got mad
                mime_type = r.headers.get('content-type', '')
                if mime_type == 'application/zip' or self.file_name.endswith('.pyz'):
                    self.file_name = self.ensure_zip_extension(self.file_name)

                # download the file
                with open(self.file_name, 'wb') as f:
                    downloaded = 0
                    for chunk in r.iter_content(chunk_size=4096):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            progress = int((downloaded / total_length) * 100)
                            self.download_progress.emit(progress)

            # singal that the download is complete
            self.download_complete.emit(self.file_name)
        except Exception as e:
            # signal gthat ERROR ERORRERORRERORRERORRERORRERORRERORRERORRERORRERORRERORRERORRERORRERORRERORRERORRERORRERORRERORRERORR
            self.download_error.emit(str(e))

    
class MainWindow(QMainWindow):
    #home url
    HOME_URL = "https://search.freakybob.site/"
    try:
        print("HOME_URL ARG FOUND;" + args.url)
        global isArgHome
        isArgHome = "True"
    except IndexError:
        print("HOME_URL config not listed; defaulting to set HOME_URL in FreakyBrowse.")
        isArgHome = "False"
    if (isArgHome == "True"):
        HOME_URL = args.url
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.resize(900, 700)
        # the title
        self.setWindowTitle(appname)
        
        # icon
        try:
            icon_path = resource_path("logo_new.ico")
            self.setWindowIcon(QIcon(icon_path))
        except Exception as e:
            print(f"Error loading icon: {e}")
            #download manager thing
        self.download_manager = DownloadManager(self)

        # the tabs stuff 
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.tabs.currentChanged.connect(self.on_current_tab_changed)
        self.home_url = MainWindow.HOME_URL
        self.setCentralWidget(self.tabs)

        # the status bar???
        self.status = QStatusBar()
        self.setStatusBar(self.status)

        # the toolbar tggreh
        self.navtb = QToolBar("Navigation")
        self.addToolBar(self.navtb)
        
        # back button
        back_btn = QAction(QIcon(resource_path("assets/icons/back.png")), "Back", self)
        back_btn.setStatusTip("Go back")
        back_btn.triggered.connect(lambda: self.current_browser().back())
        self.navtb.addAction(back_btn)

        # forward button
        next_btn = QAction(QIcon(resource_path("assets/icons/forward.png")), "Forward", self)
        next_btn.setStatusTip("Go forward")
        next_btn.triggered.connect(lambda: self.current_browser().forward())
        self.navtb.addAction(next_btn)

        # refresh button
        reload_btn = QAction(QIcon(resource_path("assets/icons/refresh.png")), "Reload", self)
        reload_btn.setStatusTip("Reload the page")
        reload_btn.triggered.connect(lambda: self.current_browser().reload())
        self.navtb.addAction(reload_btn)

        # home button
        home_btn = QAction(QIcon(resource_path("assets/icons/home.png")), "Home", self)
        home_btn.setStatusTip("Go back to home")
        home_btn.triggered.connect(self.navigate_home)
        self.navtb.addAction(home_btn)
        
        # settings button
        settings_btn = QAction(QIcon(resource_path("assets/icons/settings.png")), "Settings", self)
        settings_btn.setStatusTip("Open Settings")
        settings_btn.triggered.connect(self.open_settings)
        self.navtb.addAction(settings_btn)

        # new tab button
        new_tab_btn = QAction(QIcon(resource_path("assets/icons/new_tab.png")), "New Tab", self)
        new_tab_btn.setStatusTip("Open a new tab")
        new_tab_btn.triggered.connect(self.add_new_tab)
        self.navtb.addAction(new_tab_btn)

        # separator
        self.navtb.addSeparator()

        # so you can tpe greg
        self.urlbar = QLineEdit()

        # url stuff
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        self.navtb.addWidget(self.urlbar)
        self.urlbar.setPlaceholderText("Enter URL...")
        logo_action = QAction(QIcon(resource_path("assets/icons/logo.png")), "Logo", self.urlbar)
        self.urlbar.addAction(logo_action, QLineEdit.ActionPosition.LeadingPosition)
        self.urlbar.setClearButtonEnabled(True)

        # pikidiary button
        pikidiary_btn = QAction(QIcon(resource_path("assets/icons/piki.png")), "PikiDiary", self)
        pikidiary_btn.setStatusTip("Go to PikiDiary!")
        pikidiary_btn.triggered.connect(self.pikidiary)
        self.navtb.addAction(pikidiary_btn)

        news_button = QAction(QIcon(resource_path("assets/icons/news.png")), "News (NewsAPI.org)", self)
        news_button.setStatusTip("Read news, right here, right now! (NewsAPI key required)")
        # Added the news popup, the error is useless
        # def news_button_error():
        #     QMessageBox.warning(self, "Not Implemented", "News features have not been implemented (yet!)\n - FreakyBrowse Staff")
        news_button.triggered.connect(self.news)
        self.navtb.addAction(news_button)

        # opens the notes stuff
        notes_button = QAction(QIcon(resource_path("assets/icons/notes1.png")), "Manage Notes", self)
        notes_button.setStatusTip("Manage your notes")
        notes_button.triggered.connect(self.manage_notes)
        self.navtb.addAction(notes_button)

        # vro
        bookmark_btn = QAction(QIcon(resource_path("assets/icons/bookmark.png")), "Bookmark", self)
        bookmark_btn.setStatusTip("Bookmark this page!")
        bookmark_btn.triggered.connect(self.bookmark_page)
        self.navtb.addAction(bookmark_btn)

        # the fuck you think, retard
        view_bookmarks_btn = QAction(QIcon(resource_path("assets/icons/bookmarks.png")), "Bookmarks", self)
        view_bookmarks_btn.setStatusTip("View all bookmarks")
        view_bookmarks_btn.triggered.connect(self.show_bookmarks)
        self.navtb.addAction(view_bookmarks_btn)

        # source button
        view_source_btn = QAction(QIcon(resource_path("assets/icons/source.png")), "View Source", self)
        view_source_btn.setStatusTip("View the source of the current page")
        view_source_btn.triggered.connect(self.view_page_source)
        self.navtb.addAction(view_source_btn)

        # download button
        download_btn = QAction(QIcon(resource_path("assets/icons/download.png")), "Download Manager", self)
        download_btn.setStatusTip("Open Download Manager")
        download_btn.triggered.connect(self.open_download_manager)
        self.navtb.addAction(download_btn)

        # supposed to be for the styles, doesn't fucking work
        self.settings = QSettings("FreakyBrowse", "UserSettings1")
        self.pink_mode_enabled = self.settings.value("pink_mode", False, type=bool)
        self.blue_mode_enabled = self.settings.value("blue_mode", False, type=bool)
        self.green_mode_enabled = self.settings.value("green_mode", False, type=bool)
        self.orange_mode_enabled = self.settings.value("orange_mode", False, type=bool)
        self.red_mode_enabled = self.settings.value("red_mode", False, type=bool)
        self.oceanic_blue_enabled = self.settings.value("oceanic_blue_mode", False, type=bool)
        self.lavender_mode_enabled = self.settings.value("lavender_mode", False, type=bool)
        self.retro_green_mode_enabled = self.settings.value("retro_green_mode", False, type=bool)
        self.purple_mode_enabled = self.settings.value("purple_mode", False, type=bool)

        # rpc stuff greg
        self.settings = QSettings("FreakyBrowse", "RPC4Settings")
        self.rpc_enabled = self.settings.value("rpc_enabled", True, type=bool)
        self.warned_about_rpc = False
        self.update_rpc_state()

       
        self.toggle_mode()

        #tab stuff
        self.add_new_tab(QUrl(self.HOME_URL), "New Tab")
        self.show()

        # bookmarks
        self.bookmarks = self.settings.value("bookmarks", [], type=list)

        
    # adds a new tab 
    def add_new_tab(self, qurl=None, label="New Tab"):
        if qurl is None:
            qurl = QUrl(self.HOME_URL)

        if not isinstance(qurl, QUrl):
            qurl = QUrl(self.HOME_URL)

        browser = QWebEngineView()
        browser.setUrl(qurl)
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)
        browser.urlChanged.connect(lambda qurl, browser=browser: self.update_urlbar(qurl, browser))
        browser.titleChanged.connect(lambda title, browser=browser: self.update_tab_title(title, browser))
        browser.iconChanged.connect(lambda icon, browser=browser: self.update_tab_icon(icon, browser))

        self.tabs.setStyleSheet("""
    QTabBar::tab:selected {
        font-weight: bold
    }
        """)

        if haveDiscord == "True" and self.rpc_enabled:
                try:
                    RPC.update(
                state="Looking at " + str(qurl.toString()),
                buttons=[{"label": "Get FreakyBrowse", "url": "https://github.com/Freakybob-Team/Freakybrowse/releases/latest"}],
                large_image="icon.png",
                large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
                )
                    print("Updated RPC! (New tab)")
                except Exception as e:
                    print(f"Error updating RPC: {e}")
                try:
                    RPC.update(
                    details="Browsing the interwebs!",
                    buttons=[{"label": "Get FreakyBrowse", "url": "https://github.com/Freakybob-Team/Freakybrowse/releases/latest"}],
                    large_image="icon.png",
                    large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
                )
                    print("Fallback RPC update!")
                except Exception as fallback_error:
                    print(f"Error with fallback RPC: {fallback_error}")

    # updates the tab titles greg
    def update_tab_title(self, title, browser):
        index = self.tabs.indexOf(browser)
        tab_bar = self.tabs.tabBar()
    
        max_length = 35
        if len(title) > max_length:
            shortened_title = title[:max_length] + "..."
        else:
            shortened_title = title
    
        self.tabs.setTabText(index, shortened_title)

    # updates the tab icon for the tabs
    def update_tab_icon(self, icon, browser):
        index = self.tabs.indexOf(browser)
        self.tabs.setTabIcon(index, icon)

    # pikidiary...
    def pikidiary(self):
        url = QUrl("https://pikidiary.lol")
        self.add_new_tab(url, "FUCKING PEAK YAYAY")
        if haveDiscord == "True" and self.rpc_enabled:
            try:
                RPC.update(
                    state="Looking at " + str( self.urlbar.text()),
                    buttons=[{"label": "Get FreakyBrowse", "url": "https://github.com/Freakybob-Team/Freakybrowse/releases/latest"}],
                    large_image="icons/piki.png",
                    large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
                )
                print("Updated RPC! (Navigated to URL)")
            except Exception as e:
                print(f"Error updating RPC: {e}")
                if "style" in RPC.state:
                    RPC.update(
                        details="Browsing the interwebs!",
                        buttons=[{"label": "Get FreakyBrowse", "url": "https://github.com/Freakybob-Team/Freakybrowse/releases/latest"}],
                        large_image="icon.png",
                        large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
                    )

    # changes the tab to home greg
    def navigate_home(self):
        self.current_browser().setUrl(QUrl(self.HOME_URL))

    # navigating to urls greg
    def navigate_to_url(self):
        # help
        q = QUrl(self.urlbar.text())
        cleanedUrl = self.urlbar.text().strip("PyQt6.QtCore.QUrl()")

# this currently IGNORES Safe Browsing preferences, add LATER

#         if cleanedUrl.endswith(".png"):
#             questionUrl = QMessageBox.question(self, "Alert", "This is a downloadable URL! Do you want to download " + cleanedUrl + "?\n We are not liable for any downloads FreakyBrowse is used for.", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
# QMessageBox.StandardButton.No)
#             if (questionUrl == QMessageBox.StandardButton.No):
#                 return
#             elif (questionUrl == QMessageBox.StandardButton.Yes):
#                 global iUrl
#                 iUrl = cleanedUrl
#                 print("Created Inherit URL " + str(iUrl))
#                 self.open_download_manager()
#                 print("Opened Download Manager")
#                 if (downloadIsCompleted == "True"):
#                     iUrl = None

        if sb_key != "no key":
            try:
                if (cleanedUrl.endswith(".htm")):
                    cleanedUrl = cleanedUrl + "l"
                safeResult = subprocess.getoutput("safebrowsing url " + cleanedUrl)
                print(safeResult)
                print("executed safebrowsing url " + cleanedUrl)
                if "Malicious: Yes" in safeResult:
                    unsafeCause = safeResult.strip("Malicious: Yes\nPlatforms: ANY_PLATFORM\n Threats: ")
                    hUnsafeCause = "FreakyBrowse was unable to find a human-readable warning. Code: " + unsafeCause
                    if (unsafeCause == "SOCIAL_ENGINEERING"):
                        hUnsafeCause = "This website may try to trick you into giving away gift cards or other information. Code: " + unsafeCause
                    elif (unsafeCause == "UNWANTED_SOFTWARE"):
                        hUnsafeCause = "This website may try to get you to install software you did not intend/want to install. Code: " + unsafeCause
                    elif (unsafeCause == "WARE"):
                        hUnsafeCause = "This website may try to get you to install malware or other types of bad programs. (ex: Adware, Ransomware, Spyware) Code: " + unsafeCause
                    elif (unsafeCause == "MALWARE"):
                        hUnsafeCause = "This website may try to get you to install malware or other types of bad programs. (ex: Adware, Ransomware, Spyware) Code: " + unsafeCause
                    QMessageBox.warning(self, "Site Unsafe", "The website you are navigating to is marked as unsafe by Google Safe Browsing and we have stopped the connection.\nDetails: " + hUnsafeCause +"\nIssues? Remove your API key from FreakyBrowse.")
                    self.current_browser().setUrl(QUrl(self.HOME_URL))
                    return
                else:
                    print(cleanedUrl + " is not malicious!")
            except:
                QMessageBox.warning(self, "Safe Browsing Error", "This URL was unable to be checked by Safe Browsing. Try restarting FreakyBrowse or updating to a new version.")
                self.current_browser().setUrl(QUrl(self.HOME_URL))
                return

        if q.scheme() == "":
            q.setScheme("https")

        if q.isValid():
            if q.scheme() == "freak":
                freak_path = q.path().lstrip('/')
                if freak_path == "changelog":
                    self.current_browser().load(QUrl("https://freakybrowse.freakybob.site/freak/changelog"))
                else:
                    QMessageBox.warning(self, "Invalid URL", "Unknown freak:/ URL")
            else:
                self.current_browser().setUrl(q)

            if haveDiscord == "True" and self.rpc_enabled:
                try:
                    RPC.update(
                        state="Looking at " + str(self.urlbar.text()),
                        buttons=[{"label": "Get FreakyBrowse", "url": "https://github.com/Freakybob-Team/Freakybrowse/releases/latest"}],
                        large_image="icon.png",
                        large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
                    )
                    print("Updated RPC! (Navigated to URL)")
                except Exception as e:
                    print(f"Error updating RPC: {e}")
        else:
            QMessageBox.warning(self, "Invalid URL", "Please enter a valid URL.")



            # holy fuck, this is all the random ass rpc
        if haveDiscord == "True" and self.rpc_enabled and "chrome" in str(self.urlbar.text()):
            try:
                RPC.update(
                    details="Commiting a sin",
                    buttons=[{"label": "Get FreakyBrowse", "url": "https://github.com/Freakybob-Team/Freakybrowse/releases/latest"}],
                    large_image="icon.png",
                    large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
                )
            except Exception as e:
                print(f"Error updating RPC: {e}")
        if haveDiscord == "True" and self.rpc_enabled and "freakybob.site" in str(self.urlbar.text()):
            try:
                RPC.update(
                    details="Browsing peak, freakybob.site",
                    buttons=[{"label": "Get FreakyBrowse", "url": "https://github.com/Freakybob-Team/Freakybrowse/releases/latest"}],
                    large_image="icon.png",
                    large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
                )
            except Exception as e:
                print(f"Error updating RPC: {e}")
        if haveDiscord == "True" and self.rpc_enabled and "https://rentahitman.com/" in str(self.urlbar.text()):
            try:
                RPC.update(
                    details="Oooohh interesting IP address!",
                    buttons=[{"label": "Get FreakyBrowse", "url": "https://github.com/Freakybob-Team/Freakybrowse/releases/latest"}],
                    large_image="icon.png",
                    large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
                )
            except Exception as e:
                print(f"Error updating RPC: {e}")
        if haveDiscord == "True" and self.rpc_enabled and "pikidiary.lol" and "PikiDiary.lol" in str(self.urlbar.text()):
            try:
                RPC.update(
                    details="This user is peak! Speaking of peak, check out PikiDiary!",
                    buttons=[{"label": "PikiDiary", "url": "https://pikidiary.lol"}],
                    large_image="icon.png",
                    large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
                )
            except Exception as e:
                print(f"Error updating RPC: {e}")
        if haveDiscord == "True" and self.rpc_enabled and "x.com" and "X.com" in str(self.urlbar.text()):
            try:
                RPC.update(
                    details="You know there's always a nearby therapist office",
                    buttons=[{"label": "Get FreakyBrowse", "url": "https://github.com/Freakybob-Team/Freakybrowse/releases/latest"}],
                    large_image="icon.png",
                    large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
                )
            except Exception as e:
                print(f"Error updating RPC: {e}")
        if haveDiscord == "True" and self.rpc_enabled and "reddit.com" and "Reddit" and "reddit" in str(self.urlbar.text()):
            try:
                RPC.update(
                    details="wikihow is always a last resort",
                    buttons=[{"label": "Get FreakyBrowse", "url": "https://github.com/Freakybob-Team/Freakybrowse/releases/latest"}],
                    large_image="icon.png",
                    large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
                )
            except Exception as e:
                print(f"Error updating RPC: {e}")
        if haveDiscord == "True" and self.rpc_enabled and "classroom.google.com" and "Classroom.Google.com" in str(self.urlbar.text()):
            try:
                RPC.update(
                    details="im sorry for you",
                    buttons=[{"label": "Get FreakyBrowse", "url": "https://github.com/Freakybob-Team/Freakybrowse/releases/latest"}],
                    large_image="icon.png",
                    large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
                )
            except Exception as e:
                print(f"Error updating RPC: {e}")
        if haveDiscord == "True" and self.rpc_enabled and "archive.org" in str(self.urlbar.text()):
            try:
                RPC.update(
                    details="This user is either a huge nerd or a pirator. Prob both tbh",
                    buttons=[{"label": "Get FreakyBrowse", "url": "https://github.com/Freakybob-Team/Freakybrowse/releases/latest"}],
                    large_image="icon.png",
                    large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
                )
            except Exception as e:
                print(f"Error updating RPC: {e}")
        if haveDiscord == "True" and self.rpc_enabled and "apple.com" in str(self.urlbar.text()):
            try:
                RPC.update(
                    details="We're more open than them, y'know?",
                    buttons=[{"label": "Get FreakyBrowse", "url": "https://github.com/Freakybob-Team/Freakybrowse/releases/latest"}],
                    large_image="icon.png",
                    large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
                )
            except Exception as e:
                print(f"Error updating RPC: {e}")
        if haveDiscord == "True" and self.rpc_enabled and "match.com" in str(self.urlbar.text()):
            try:
                RPC.update(
                    details="On FreakyBrowse? Really",
                    buttons=[{"label": "Get FreakyBrowse", "url": "https://github.com/Freakybob-Team/Freakybrowse/releases/latest"}],
                    large_image="icon.png",
                    large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
                )
            except Exception as e:
                print(f"Error updating RPC: {e}")
        if haveDiscord == "True" and self.rpc_enabled and "redditforcommunity.com" and "www.reddit.com/r/modhelp/" in str(self.urlbar.text()):
            try:
                RPC.update(
                    details="Weight.. being.. gained..",
                    buttons=[{"label": "Get FreakyBrowse", "url": "https://github.com/Freakybob-Team/Freakybrowse/releases/latest"}],
                    large_image="icon.png",
                    large_text="FreakyBrowse next to a search glass with Freakybob inside of the glass."
                )
            except Exception as e:
                print(f"Error updating RPC: {e}")

    # updates the urlbar
    def update_urlbar(self, q, browser=None):
        if browser != self.current_browser():
            return
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

        index = self.tabs.indexOf(browser)
        icon = self.tabs.tabIcon(index)
        self.tabs.setTabIcon(index, icon)

    # returns the current browser
    def current_browser(self):
        return self.tabs.currentWidget()

    # closes the current tab
    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return
        current_browser = self.current_browser()
        if current_browser:
            current_browser.stop()
            current_browser.setUrl(QUrl())
        self.tabs.removeTab(i)
        if current_browser:
            self.update_urlbar(current_browser.url(), current_browser)
        else:
            self.urlbar.clear()

    # updates the URL bar when the tab changes
    def on_current_tab_changed(self, index):
        browser = self.current_browser()
        if browser:
            self.update_urlbar(browser.url(), browser)
        else:
            self.urlbar.clear()
    
    # loads the styles from the folder
    def load_style_from_file(self, style_name):
        if hasattr(sys, '_MEIPASS'):
            styles_folder = os.path.join(sys._MEIPASS, 'styles')
        else:
            styles_folder = os.path.join(os.path.dirname(__file__), 'assets/styles')

        style_path = os.path.join(styles_folder, f"{style_name}.qss")

        if os.path.exists(style_path):
            with open(style_path, "r") as style_file:
                style = style_file.read()
                self.setStyleSheet(style)
        else:
            print(f"Style file '{style_name}.qss' not found at {style_path}!")

    # more style code greg
    def toggle_mode(self):
        modes = {
            "pink_mode": self.pink_mode_enabled,
            "blue_mode": self.blue_mode_enabled,
            "green_mode": self.green_mode_enabled,
            "red_mode": self.red_mode_enabled,
            "orange_mode": self.orange_mode_enabled,
            "oceanic_blue_mode": self.oceanic_blue_enabled,
            "lavender_mode": self.lavender_mode_enabled,
            "retro_green_mode": self.retro_green_mode_enabled,
            "purple_mode": self.purple_mode_enabled,
        }
        for mode, enabled in modes.items():
            if enabled:
                self.load_style_from_file(mode)
                break
        else:
            self.load_style_from_file("default_mode")

    # a simplified version of the original style code, don't mess with it if you no understand
    def toggle_mode_enabled(self, mode_name, enabled):
        modes = [
            "pink_mode", "blue_mode", "green_mode", "red_mode", "orange_mode", 
            "oceanic_blue_mode", "lavender_mode", "retro_green_mode", "purple_mode"
        ]
        for mode in modes:
            setattr(self, f"{mode}_enabled", False)
        setattr(self, f"{mode_name}_enabled", enabled)
        self.settings.setValue(f"{mode_name}", enabled)
        for mode in modes:
            self.settings.setValue(f"{mode}", getattr(self, f"{mode}_enabled"))
        self.toggle_mode()


    # style settings
    def open_style_settings(self):
        style_dialog = QDialog(self)
        style_dialog.setWindowTitle("Style Settings")
        style_dialog.setFixedSize(400, 400)
        style_dialog.setStyleSheet("""
            background-color: #17786d;
            border-radius: 10px;
        """)

        layout = QVBoxLayout()

        main_label = QLabel("Style Settings")
        main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        main_label.setStyleSheet("color: #333333; margin-bottom: 10px;")
        layout.addWidget(main_label)

        styles = [
            ("Pink Mode", self.pink_mode_enabled, lambda enabled: self.toggle_mode_enabled("pink_mode", enabled)),
            ("Blue Mode", self.blue_mode_enabled, lambda enabled: self.toggle_mode_enabled("blue_mode", enabled)),
            ("Green Mode", self.green_mode_enabled, lambda enabled: self.toggle_mode_enabled("green_mode", enabled)),
            ("Red Mode", self.red_mode_enabled, lambda enabled: self.toggle_mode_enabled("red_mode", enabled)),
            ("Orange Mode", self.orange_mode_enabled, lambda enabled: self.toggle_mode_enabled("orange_mode", enabled)),
            ("Oceanic Blue Mode", self.oceanic_blue_enabled, lambda enabled: self.toggle_mode_enabled("oceanic_blue_mode", enabled)),
            ("Lavender Mode", self.lavender_mode_enabled, lambda enabled: self.toggle_mode_enabled("lavender_mode", enabled)),
            ("Retro Green Mode", self.retro_green_mode_enabled, lambda enabled: self.toggle_mode_enabled("retro_green_mode", enabled)),
            ("Dark Purple", self.purple_mode_enabled, lambda enabled: self.toggle_mode_enabled("purple_mode", enabled)),
        ]

        for label, enabled, toggle_func in styles:
            checkbox = QCheckBox(f"Enable {label}")
            checkbox.setChecked(enabled)
            checkbox.setStyleSheet("font-size: 14px; padding: 5px;")
            checkbox.stateChanged.connect(lambda checked, func=toggle_func: func(checked))
            layout.addWidget(checkbox)

        close_button = QPushButton("Close")
        close_button.setStyleSheet("""
            background-color: #0078d4;
            color: white;
            padding: 4px;
            border-radius: 5px;
            font-size: 14px;
        """)
        close_button.clicked.connect(style_dialog.accept)
        layout.addWidget(close_button)

        style_dialog.setLayout(layout)
        style_dialog.exec()

    # browser settings
    def open_browser_settings(self):
        browser_dialog = QDialog(self)
        browser_dialog.setWindowTitle("Browser Settings")
        browser_dialog.setFixedSize(480, 320)
        browser_dialog.setStyleSheet("""
            background-color: #61a6a0;
            border-radius: 10px;
        """)

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        use_google_checkbox = QCheckBox("Use Google's main page?")
        use_google_checkbox.setChecked(self.home_url == "https://google.com")
        use_google_checkbox.stateChanged.connect(
            lambda state: self.toggle_homepage_url(state, home_url_label)
        )
        layout.addWidget(use_google_checkbox)

        warning_label = QLabel("This only changes the Home button and new tab location.")
        home_url_label = QLabel(f"Current Home URL: {self.home_url}")
        layout.addWidget(warning_label)
        layout.addWidget(home_url_label)

        use_rpc_checkbox = QCheckBox("Use FreakyBrowse's Discord RPC?")
        use_rpc_checkbox.setChecked(self.rpc_enabled)
        use_rpc_checkbox.stateChanged.connect(self.toggle_rpc)
        layout.addWidget(use_rpc_checkbox)

        rpc_warning_label = QLabel("Disabling Discord RPC will require a reinstall or update to re-enable.")
        layout.addWidget(rpc_warning_label)

        close_button = QPushButton("Close")
        close_button.setStyleSheet("""
            background-color: #3498db;
            color: white;
            padding: 10px;
            border-radius: 5px;
            font-size: 14px;
            margin-top: 20px;
        """)
        close_button.clicked.connect(browser_dialog.accept)
        layout.addWidget(close_button)

        browser_dialog.setLayout(layout)
        browser_dialog.exec()

    # giant ass info window
    def open_info_button(self):
        info_dialog = QDialog(self)
        info_dialog.setWindowTitle("FreakyBrowse Info")
        info_dialog.setFixedSize(940, 510)
        info_dialog.setStyleSheet("""
        background-color: #477168;
        """)

        layout = QVBoxLayout()

        title_label = QLabel("𝓯𝓻𝓮𝓪𝓴𝔂Browse Info")
        title_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #333333;")
        layout.addWidget(title_label)

        below_label1 = QLabel("FreakyBrowse, by the Freakybob Team.")
        below_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        below_label1.setFont(QFont("Arial", 11, QFont.Weight.Normal))
        below_label1.setStyleSheet("color:#333333;")
        layout.addWidget(below_label1)

        version_layout = QHBoxLayout()
        version_label = QLabel("Version: 2.5")
        version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        version_label.setFont(QFont("Arial", 11, QFont.Weight.Normal))
        version_label.setStyleSheet("color: white;")
        version_layout.addWidget(version_label)
        layout.addLayout(version_layout)

        title_label2 = QLabel("History")
        title_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label2.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title_label2.setStyleSheet("color: #333333;")
        layout.addWidget(title_label2)

        info_label = QLabel("FreakyBrowse was made on October 13th, 2024. It first started out as code stolen from GeeksForGeeks but was updated to work and look better.\nThe first time we started to try to distribute FreakyBrowse, it was flagged as a trojan. It was a false positive from PyInstaller. It was originally thought to be auto-py-to-exe, but was actually PyInstaller.")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info_label.setFont(QFont("Arial", 10, QFont.Weight.Normal))
        info_label.setStyleSheet("color: white;")
        layout.addWidget(info_label)

        your_info_title = QLabel("Your Info")
        your_info_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        your_info_title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        your_info_title.setStyleSheet("color: #333333;")
        layout.addWidget(your_info_title)

        your_info_label = QLabel("FreakyBrowse does not use your personal info. Every website you visit is your choice or the website's choice to collect information on you.\nYou do have to agree to the Privacy Policy on search.freakybob.site.\nYou can find it by pressing 'here' on search.freakybob.site.\n Some dependencies we use may also use your data. We can't do anything about this.")
        your_info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        your_info_label.setFont(QFont("Arial", 10, QFont.Weight.Normal))
        your_info_label.setStyleSheet("color: white;")
        layout.addWidget(your_info_label)

        gpl_label = QLabel("License?")
        gpl_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        gpl_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        gpl_label.setStyleSheet("color: #333333;")
        layout.addWidget(gpl_label)

        info_label2 = QLabel("Most, if not everything, is GPL-3")
        info_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info_label2.setFont(QFont("Arial", 10, QFont.Weight.Normal))
        info_label2.setStyleSheet("color: white;  ")
        layout.addWidget(info_label2)

        close_button = QPushButton("Close")
        close_button.setStyleSheet("""
        background-color: #0078d4;
        color: white;
        padding: 10px;
        border-radius: 5px;
        font-size: 14px;
        margin-top: 15px;
        """)
        close_button.clicked.connect(info_dialog.accept)
        layout.addWidget(close_button)

        info_dialog.setLayout(layout)
        info_dialog.exec()

        # toggles rpc
    def toggle_rpc(self, state):
        if self.rpc_enabled and not self.warned_about_rpc:
            reply = QMessageBox.question(self, "Warning", 
                                     "Are you sure you want to disable Discord RPC? This action cannot be undone unless you reinstall or update.",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.No:
                self.sender().setChecked(self.rpc_enabled)
                return

            self.warned_about_rpc = True

        self.rpc_enabled = state == Qt.CheckState.Checked
        self.settings.setValue("rpc_enabled", self.rpc_enabled)
        print(f"RPC toggled: {'Enabled' if self.rpc_enabled else 'Disabled'}")
        self.update_rpc_state()

    # basically just says if it was enabled or no
    def update_rpc_state(self):
        if self.rpc_enabled:
            try:
                print("RPC is now enabled.")
            except Exception as e:
                print(f"Error enabling RPC: {e}")
        else:
            try:
                RPC.clear()
                print("RPC is now disabled.")
            except Exception as e:
                print(f"Error disabling RPC: {e}")
    # useragent thingy
    def useragent_settings(self):
    # ID: 12344
        useragent_dialog = QDialog(self)
        useragent_dialog.setWindowTitle("[Guard] UserAgent Settings")
        useragent_dialog.setFixedSize(400, 230)

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        warning_label = QLabel("WARNING: This may break websites. Use at your own risk.")
        layout.addWidget(warning_label)

        agent_label = QLabel("Enter custom UserAgent string:")
        layout.addWidget(agent_label)

        agent_input = QLineEdit()
        layout.addWidget(agent_input)

        chrome_default_button = QPushButton("Change UserAgent to Chrome 131.0.0.0 (Windows NT 10.0; Win64)")
        layout.addWidget(chrome_default_button)

        submit_button = QPushButton("Change UserAgent")
        layout.addWidget(submit_button)

        def useragent_change():
            global useragent # makes useragent variable accessable
            useragent = agent_input.text().strip()
            web.page().profile().setHttpUserAgent(
                useragent
            ) # set useragent

        def chrome_default():
            global useragent # makes useragent variable accessable
            useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
            web.page().profile().setHttpUserAgent(
                useragent
            ) # set useragent

        submit_button.clicked.connect(useragent_change)
        chrome_default_button.clicked.connect(chrome_default)

        close_button = QPushButton("Close")
        layout.addWidget(close_button)
        close_button.clicked.connect(useragent_dialog.accept)

        useragent_dialog.setLayout(layout)
        useragent_dialog.exec()
    # neews
    def news(self):
        news_dialog = QDialog(self)
        news_dialog.setWindowTitle("Catch⬆")
        news_dialog.setFixedSize(900, 600)

        web_view = QWebEngineView(news_dialog)


        web_view.setUrl(QUrl.fromLocalFile("/pages/news.html"))

        layout = QVBoxLayout()
        layout.addWidget(web_view)
        news_dialog.setLayout(layout)

        news_dialog.exec()

    # api stuff
    def api_settings(self):
        api_dialog = QDialog(self)
        api_dialog.setWindowTitle("API Key Settings")
        api_dialog.setFixedSize(400, 350)

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        warning_label = QLabel(
            "If you do not enter an API key, these services will be disabled.\n"
        )
        warning_label.setWordWrap(True)
        warning_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(warning_label)


        sb_label = QLabel("Google Safe Browsing API Key:")
        sb_key_input = QLineEdit()
        sb_key_input.setPlaceholderText("Enter your Google Safe Browsing API key")
        main_layout.addWidget(sb_label)
        main_layout.addWidget(sb_key_input)


        news_label = QLabel("NewsAPI.org API Key:")
        news_key_input = QLineEdit()
        news_key_input.setPlaceholderText("Enter your NewsAPI.org API key")
        main_layout.addWidget(news_label)
        main_layout.addWidget(news_key_input)


        if os.path.exists(key_file):
            with open(key_file, "r") as file:
                saved_keys = json.load(file)
                sb_key_input.setText(saved_keys.get("sb_key", ""))
                news_key_input.setText(saved_keys.get("news_key", ""))


        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        submit_button = QPushButton("Save Keys")
        delete_button = QPushButton("Delete Keys")
        close_button = QPushButton("Close")

        button_layout.addWidget(submit_button)
        button_layout.addWidget(delete_button)
        button_layout.addWidget(close_button)

        main_layout.addLayout(button_layout)


        def save_keys():
            sb_key = sb_key_input.text().strip()
            news_key = news_key_input.text().strip()
            keys_to_save = {}

            if sb_key:
                keys_to_save["sb_key"] = sb_key
            if news_key:
                keys_to_save["news_key"] = news_key

            if not keys_to_save:
                QMessageBox.warning(api_dialog, "Missing Keys", "At least one API key must be provided.")
                return

            with open(key_file, "w") as file:
                json.dump(keys_to_save, file)

            QMessageBox.information(api_dialog, "Keys Saved", "API keys have been successfully saved.")

        def delete_keys():
            if os.path.exists(key_file):
                os.remove(key_file)
                QMessageBox.information(api_dialog, "Keys Deleted", "API keys have been deleted. Restart the application.")
            else:
                QMessageBox.warning(api_dialog, "No Keys Found", "No keys found to delete.")

        submit_button.clicked.connect(save_keys)
        delete_button.clicked.connect(delete_keys)
        close_button.clicked.connect(api_dialog.accept)

        api_dialog.setLayout(main_layout)
        api_dialog.exec()

    # im extension yabbie dee yabbie die
    def extension_settings(self):
        extensions_dialog = QDialog(self)
        extensions_dialog.setWindowTitle("[Beta] Extensions")
        extensions_dialog.setFixedSize(400, 230)
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)
        warning_label = QLabel("WARNING: This feature is in dev! It does NOT work, and is just UI.")
        layout.addWidget(warning_label)
        extension_button = QPushButton("Select Extension Folder")
        layout.addWidget(extension_button)   
        def filepicker():
            file_picker, _ = QFileDialog.getOpenFileName(self, "Select Extension Folder", "")
        extension_button.clicked.connect(filepicker)
        submit_button = QPushButton("Load Extension")
        layout.addWidget(submit_button)
        close_button = QPushButton("Close")
        layout.addWidget(close_button)
        close_button.clicked.connect(extensions_dialog.accept)
        extensions_dialog.setLayout(layout)
        extensions_dialog.exec()
    # I wonder what /j shortcut stuff
    def shortcut_settings(self):
        shortcut_dialog = QDialog(self)
        shortcut_dialog.setWindowTitle("Shortcuts")
        shortcut_dialog.setFixedSize(400, 230)

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        url_label = QLabel("Enter URL:")
        layout.addWidget(url_label)

        url_input = QLineEdit()
        layout.addWidget(url_input)

        name_label = QLabel("Enter Shortcut Name (optional):")
        layout.addWidget(name_label)

        name_input = QLineEdit()
        layout.addWidget(name_input)

        create_button = QPushButton("Create Shortcut")
        layout.addWidget(create_button)
        
        #makes the shortcut
        def create_shortcut():
            url = url_input.text().strip()
            name = name_input.text().strip()
            shortcut_folder = "Shortcuts"

            if os.path.exists(shortcut_folder + "/" + name + ".bat"):
                QMessageBox.warning(self, "Issue creating shortcut", "Shortcut with the same name already exists.")
                return

            if not url:
                QMessageBox.warning(self, "Warning", "vro. Put the url :sob:")
                return

            if not (url.startswith("http://") or url.startswith("https://")):
                QMessageBox.warning(self, "Warning", "URL must start with http:// or https:// !")
                return

            if '.' not in url:
                QMessageBox.warning(self, "Warning", "URL must contain a '.' (e.g., .com, .net) !")
                return

            if not os.path.exists(shortcut_folder):
                os.makedirs(shortcut_folder)

            count = 1
            while True:
                if not name:
                    generated_name = f"Shortcut{count}.bat"
                else:
                    generated_name = f"{name}.bat"

                file_path = os.path.join(shortcut_folder, generated_name)

                if not os.path.exists(file_path):
                    break

                count += 1

            try:
                with open(file_path, "w") as file:
                    file.write(f"@echo off\nrem make sure to change the name in the bat file if you want to share the batch file!! Don't want your name to get leaked :3\n\ncd /d {os.getcwd()}\npowershell py freakybrowse.py --url {url}\nIF %ERRORLEVEL% NEQ 0 (\necho Error: Failed to launch FreakyBrowse\npause\n)")
                QMessageBox.information(self, "Success", f"Shortcut created: {file_path} !!!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to create shortcut: {str(e)}")

        create_button.clicked.connect(create_shortcut)

        close_button = QPushButton("Close")
        layout.addWidget(close_button)
        close_button.clicked.connect(shortcut_dialog.accept)

        shortcut_dialog.setLayout(layout)
        shortcut_dialog.exec()

    # the settings window
    def open_settings(self):
        settings_dialog = QDialog(self)
        settings_dialog.setWindowTitle("Settings")
        settings_dialog.setFixedSize(600, 470)
        settings_dialog.setStyleSheet("""
            background-color: #a3d8f4;
            border-radius: 10px;
        """)

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        main_label = QLabel("Settings")
        main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        main_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(main_label)

        buttons = [
            ("Style Settings", self.open_style_settings),
            ("Browser Settings", self.open_browser_settings),
            ("Info", self.open_info_button),
            ("Shortcut", self.shortcut_settings),
            ("[Guard] UserAgent", self.useragent_settings),
            ("[Beta] Extensions", self.extension_settings),
            ("[API] Key Settings", self.api_settings)
        ]

        for label, func in buttons:
            button = QPushButton(label)
            button.setStyleSheet("""
                background-color: #3498db;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            """)
            button.clicked.connect(func)
            layout.addWidget(button)

        close_button = QPushButton("Close")
        close_button.setStyleSheet("""
            background-color: #1abc9c;
            color: white;
            padding: 10px;
            border-radius: 5px;
            font-size: 14px;
        """)
        close_button.clicked.connect(settings_dialog.accept)
        layout.addWidget(close_button)

        settings_dialog.setLayout(layout)
        settings_dialog.exec()

    # toggles the homepage url
    def toggle_homepage_url(self, state, home_url_label):
        if state == 2:
            
            MainWindow.HOME_URL = "https://google.com"
            self.home_url = MainWindow.HOME_URL
        else:
           
            MainWindow.HOME_URL = "https://search.freakybob.site/"
            self.home_url = MainWindow.HOME_URL

        home_url_label.setText(f"Current Home URL: {self.home_url}")
        print(f"Home URL set to: {self.home_url}")

    
    # the main notes window that holds all the buttons and all that
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

        download_note_button = QPushButton("Download Note")
        download_note_button.clicked.connect(lambda: self.download_note_as_txt(notes_list, saved_notes))
        button_layout.addWidget(download_note_button)

        layout.addLayout(button_layout)

        note_viewer = QTextEdit()
        note_viewer.setReadOnly(False)
        layout.addWidget(note_viewer)

        upload_image_button = QPushButton("Insert Image")
        upload_image_button.clicked.connect(lambda: self.insert_image(note_viewer))
        layout.addWidget(upload_image_button)

        # loads note content
        def load_note_content():
            selected_item = notes_list.currentItem()
            if selected_item:
                note_content = saved_notes.get(selected_item.text(), "")
                note_viewer.setHtml(note_content)
            else:
                note_viewer.clear()
        notes_list.itemSelectionChanged.connect(load_note_content)

        # saves note content.
        def save_note_content():
            selected_item = notes_list.currentItem()
            if selected_item:
                saved_notes[selected_item.text()] = note_viewer.toHtml()
                self.settings.setValue("notes", saved_notes)

        note_viewer.textChanged.connect(save_note_content)

        notes_dialog.setLayout(layout)
        notes_dialog.exec()

    # I don't have to explain this.
    def add_note_dialog(self, notes_list, saved_notes):
        text, ok = QInputDialog.getText(self, "Add Note", "Enter note name:")
        if not ok or not text:
            return

        notes_list.addItem(text)
        saved_notes[text] = ""

        self.settings.setValue("notes", saved_notes)

        item = notes_list.findItems(text, Qt.MatchFlag.MatchExactly)[0]
        notes_list.setCurrentItem(item)

        note_viewer = self.findChild(QTextEdit) 
        note_viewer.setHtml("")
        note_viewer.setFocus()

    # I can't tell what this does, ask wish
    def delete_note(self, notes_list, saved_notes):
        if notes_list.count() == 0:
            QMessageBox.warning(self, "No Notes to Delete", "Vro, there are no notes to delete.")
            return

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

    # get's an image from the user prompt and turns that image into html
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
        img_tag = f'<img src="{image_path}" width="{width}" height="{height}" alt="Image">'
        
        if file_extension == "gif":
            img_tag = f'<img src="{image_path}" width="{width}" height="{height}" alt="GIF">'

        note_viewer.insertHtml(img_tag)

    # downloads the note as txt
    def download_note_as_txt(self, notes_list, saved_notes):
        selected_item = notes_list.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "No Note Selected", "Please select a note to download.")
            return

        note_name = selected_item.text()
        note_content = saved_notes.get(note_name, "")

        temp_editor = QTextEdit()
        temp_editor.setHtml(note_content)
        plain_text_content = temp_editor.toPlainText()

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Note As",
            f"{note_name}.txt",
            "Text Files (*.txt)"
        )
        if not file_path:
            return

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(plain_text_content)
            QMessageBox.information(self, "Download Successful", f"'{note_name}' has been downloaded as '{file_path}'.")
        except Exception as e:
            QMessageBox.critical(self, "Error Saving File", f"An error occurred: {e}")



    # it does this thing... it's called bookmarking....
    def bookmark_page(self):
        url = self.current_browser().url().toString()
        if url not in self.bookmarks:
            self.bookmarks.append(url)
            self.settings.setValue("bookmarks", self.bookmarks)
            QMessageBox.information(self, "Bookmark Added", f"{url} has been bookmarked.")
        else:
            QMessageBox.warning(self, "Already Bookmarked", "This page is already in your bookmarks.")

    # shows the bookmarks window
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


    # wouldn't take a genius to figure this out
    def delete_bookmark(self, url, dialog):
        if url in self.bookmarks:
            self.bookmarks.remove(url)
            self.settings.setValue("bookmarks", self.bookmarks)
            dialog.accept()
            self.show_bookmarks()

    # retrieves the html of the current page
    def view_page_source(self):        
        current_browser = self.current_browser()
        current_browser.page().toHtml(lambda html: self.show_html(html))

    # shows the html dumbass
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

    # shows the download window
    def open_download_manager(self):
        self.download_manager_window = DownloadManagerWindow(self)
        self.download_manager_window.show()
    
    # the code that used to be here was for the status bar, we no use status bar


if __name__ == "__main__":
    global web
    web = QWebEngineView()
    # interceptor = QWebEngineUrlRequestInterceptor()
    # global profile
    # profile = QWebEngineProfile()
    # profile.setRequestInterceptor(interceptor)
    # set user agent
    try:
        web.page().profile().setHttpUserAgent(
            useragent
        )
    except:
        print("No custom user-agent found; using default")
    # end set user agent
    try:
        if (appname != args.name):
            app.setApplicationName(appname)
            print(appname)
    except:
        app.setApplicationName(appname)
        print(appname)
    app.setWindowIcon(QIcon("logo_new.ico")) 
    
    window = MainWindow()
    app.exec() # app.exec_() is deprecated in PyQt6
#I am steve :33333 GREG GREG GREG I HATE YOU !!!!VFYUGEIHLJ:K:D<MNFKGILEHQODJLK:A?<
# freakbob
