import requests
from urllib.request import urlretrieve
current_url = "https://github.com/Freakybob-Team/freakybrowse/releases/download/v2.2/2.2.zip" # change this upon release
url = "https://github.com/Freakybob-Team/freakybrowse/blob/main/newest_release.txt?raw=true"
res = requests.get(url)
print("URL from Local: " + current_url)
print("URL from Cloud: " + res.text)
if (res.text == current_url):
    print("No new version has been found!")
else:
    urlretrieve(res.text, "updated_freakybrowse.zip")