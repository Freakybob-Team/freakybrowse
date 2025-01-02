import requests
from urllib.request import urlretrieve
current_url = "https://github.com/Freakybob-Team/freakybrowse/releases/download/v2.2/2.2.zip"
url = "https://github.com/Freakybob-Team/freakybrowse/newest_release.txt?raw=true"
res = requests.get(url)
if (res.text == current_url):
    print("No new version has been found!")
else:
    urlretrieve(res.text, "updated_freakybrowse.zip")