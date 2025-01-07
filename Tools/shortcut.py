import os
import winsound
import time
def create():
    while True:
        print("------------------------------------------------------")
        print("Create a shortcut for FreakyBrowse!")
        url = input("Enter the URL: ")

        if not (url.startswith("http://") or url.startswith("https://")):
            print("Error: URL must start with http:// or https://")
        elif "." not in url:
            print("Error: URL must contain a '.' (e.g., .com, .net)")
        else:
            break

    while True:
        name = input("Enter a name for the shortcut (leave blank for default): ")

        if not name.strip():
            name = None
            break
        elif ".bat" in name:
            name = name.replace(".bat", "")
            break
        else:
            break

    create_shortcut(url, name)

def create_shortcut(url, name):
    shortcut_folder = "Shortcuts"
    if not os.path.exists(shortcut_folder):
        os.makedirs(shortcut_folder)

    if name is None:
        name = "Shortcut"
    else:
        name = name.replace(".bat", "")

    count = 1
    file_path = os.path.join(shortcut_folder, f"{name}{count}.bat")

    while os.path.exists(file_path):
        count += 1
        file_path = os.path.join(shortcut_folder, f"{name}{count}.bat")

    try:
        with open(file_path, "w") as file:
            file.write(f"@echo off\nrem make sure to change the name in the bat file if you want to share the batch file!! Don't want your name to get leaked :3\n\ncd /d {os.getcwd()}\npowershell py freakybrowse.py --url {url}\nIF %ERRORLEVEL% NEQ 0 (\necho Error: Failed to launch FreakyBrowse\npause\n)")
        print(f"Shortcut created: {file_path} !")
        winsound.Beep(523, 200)  
        winsound.Beep(659, 200)
        winsound.Beep(784, 400)
    except Exception as e:
        print(f"Failed to create shortcut: {str(e)} :c")
    time.sleep(2)
    print("------------------------------------------------------")
    
def main():
    print("Welcome to the Shortcut maker for FreakyBrowse!")
    print("To Create a new shortcut for FreakyBrowse, type 'create' !!")

    while True:
        choice = input().lower()
        if choice == "create":
            create()
        elif choice == "exit":
            exit()
        else:
            print("That command doesn't exist! Try 'create'!")
        main()

if __name__ == "__main__":
    main()
