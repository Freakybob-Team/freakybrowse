import os
import requests

def versions_menu():
    print("These are all of the versions that you can install!!! You can also use this to update!")
    print("2.3\n2.2\n2.1\n2\n1.9\n1.8\n1.7\n1.6\n1.5\n1.4\n1.3\n1.2\n1.1\n1.0\n")
    choice = input()

    urls = {
        "2.3": "https://github.com/Freakybob-Team/freakybrowse/releases/download/V.2.3/FreakyBrowse.2.3.zip",
        "2.2": "https://github.com/Freakybob-Team/freakybrowse/releases/download/v2.2/2.2.zip",
        "2.1": "https://github.com/Freakybob-Team/freakybrowse/releases/download/V.2.1/2.1.zip",
        "2": "https://github.com/Freakybob-Team/freakybrowse/releases/download/V.2.0/FreakyBrowse2.exe",
        "1.9": "https://github.com/Freakybob-Team/freakybrowse/releases/download/V.1.9/FreakyBrowse.1.9.exe",
        "1.8": "https://github.com/Freakybob-Team/freakybrowse/releases/download/V.1.8/FreakyBrowse.1.8.exe",
        "1.7": "https://github.com/Freakybob-Team/freakybrowse/releases/download/V.1.7/FreakyBrowse.1.7.exe",
        "1.6": "https://github.com/Freakybob-Team/freakybrowse/releases/download/V.1.6/FreakyBrowse.1.6.exe",
        "1.5": "https://github.com/Freakybob-Team/freakybrowse/releases/download/V.1.5/FreakyBrowse.1.5.exe",
        "1.4": "https://github.com/Freakybob-Team/freakybrowse/releases/download/V.1.4/FreakyBrowse.1.4.exe",
        "1.3": "https://github.com/Freakybob-Team/freakybrowse/releases/download/V.1.3/FreakyBrowse.1.3.exe",
        "1.2": "https://github.com/Freakybob-Team/freakybrowse/releases/download/V.1.2/FreakyBrowse.exe",
        "1.1": "https://github.com/Freakybob-Team/freakybrowse/releases/download/V.1.1/Freakybrowse.exe",
        "1.0": "https://github.com/Freakybob-Team/freakybrowse/releases/download/V.1.0/Freakybrowse.exe"
    }

    if choice in urls:
        sure = input("Are you sure you want to install this? (y/n)\n")
        if sure.lower() == "y":
            file_name = urls[choice].split("/")[-1]
            try:
                response = requests.get(urls[choice], stream=True)
                with open(file_name, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print("Downloaded successfully!")
            except Exception as e:
                print(f"Error downloading file: {e}")
        else:
            versions_menu()
    else:
        print("Invalid version. Try again.")
        versions_menu()

def uninstall():
    print("Here you'll be able to uninstall any version of FreakyBrowse that you have!")
    print("Here's all the versions!\n")
    print("2.3\n2.2 (STYLES DON'T SAVE)\n2.1\n2\n1.9\n1.8\n1.7\n1.6\n1.5\n1.4\n1.3\n1.2\n1.1\n1.0\n")
    choice = input()
    files = {
        "2.3": "2.3.zip",
        "2.2": "2.2.zip",
        "2.1": "2.1.zip",
        "2": "FreakyBrowse2.exe",
        "1.9": "FreakyBrowse.1.9.exe",
        "1.8": "FreakyBrowse.1.8.exe",
        "1.7": "FreakyBrowse.1.7.exe",
        "1.6": "FreakyBrowse.1.6.exe",
        "1.5": "FreakyBrowse.1.5.exe",
        "1.4": "FreakyBrowse.1.4.exe",
        "1.3": "FreakyBrowse.1.3.exe",
        "1.2": "FreakyBrowse.1.2.exe",
        "1.1": "Freakybrowse.exe",
        "1.0": "Freakybrowse.exe"
    }

    if choice in files:
        try:
            os.remove(files[choice])
            print("File deleted successfully!")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"Error deleting file: {e}")
    else:
        print("Invalid version. Try again")
        uninstall()

def help_menu():
    print("Commands:\nversions - View and install versions\nuninstall - Uninstall versions\nhelp - Show this menu\nexit - Exit the installer")

def main():
    print("Welcome to the FreakyBrowse Installer!\nYou'll be able to install or update any version of FreakyBrowse here!")
    print("To see all the commands, type 'help' !!\n")

    while True:
        choice = input().lower()
        if choice == "versions":
            versions_menu()
        elif choice == "help":
            help_menu()
        elif choice in ["uninstall", "delete"]:
            uninstall()
        elif choice == "exit":
            exit()
        else:
            print("That command doesn't exist! Try 'versions'!")

main()
