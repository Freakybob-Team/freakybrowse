import requests
from urllib.request import urlretrieve
from urllib.error import URLError, HTTPError

current_url = "https://github.com/Freakybob-Team/freakybrowse/releases/download/v2.4.2/FreakyBrowse.2.4.2.zip" # change this upon release
url = "https://github.com/Freakybob-Team/freakybrowse/blob/main/newest_release.txt?raw=true"

try:
    res = requests.get(url)
    res.raise_for_status()
    print("URL from Local: " + current_url)
    print("URL from Cloud: " + res.text.strip())
    if res.text.strip() == current_url.strip():
        print("No new version has been found!")
    else:
        try:
            urlretrieve(res.text.strip(), "updated_freakybrowse.zip")
            print("New version downloaded successfully!")
        except HTTPError as e:
            print(f"HTTP Error: {e.code} - {e.reason}")
        except URLError as e:
            print(f"URL Error: {e.reason}")
        except Exception as e:
            print(f"Unexpected error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Failed to fetch cloud URL: {e}")

input("Press Enter to exit...")
exit()
