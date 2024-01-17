import shutil, os, smtplib, colorama, threading, time
#from email.message import EmailMessage

src = os.environ['USERPROFILE'] + r"\AppData\Local\Google\Chrome\User Data"
srcOut = ""

def copy() :
    shutil.copytree(src, srcOut)

def progressBar(progress, total):
    percent = 100 * (progress / float(total))
    bar = "█" * int(percent) + "-" * (100 - int(percent))
    if progress == total :
        print(colorama.Fore.GREEN + f"\r|{bar}| 100%", end="\r")
    elif progress<total :
        print(colorama.Fore.YELLOW + f"\r|{bar}| {percent:.2f}%", end="\r")

def checker(source_path, destination_path):
    time.sleep(1)

    while not os.path.exists(destination_path):
        print (colorama.Fore.RED + "Not Exists")
        time.sleep(.01)

    while os.path.getsize(source_path) >= os.path.getsize(destination_path):
        progressBar(os.path.getsize(srcOut), os.path.getsize(src))

    print("\n\nOperation Completed")
    print(colorama.Fore.RESET)
    print("")

print(colorama.Fore.CYAN + '''

 _   _                   _      _____ _                              
| \ | |                 | |    /  __ \ |                             
|  \| | __ _ _ __   ___ | | ___| /  \/ |__  _ __ ___  _ __ ___   ___ 
| . ` |/ _` | '_ \ / _ \| |/ _ \ |   | '_ \| '__/ _ \| '_ ` _ \ / _ \\
| |\  | (_| | |_) | (_) | |  __/ \__/\ | | | | | (_) | | | | | |  __/
\_| \_/\__,_| .__/ \___/|_|\___|\____/_| |_|_|  \___/|_| |_| |_|\___|
            | |                                                      
            |_|                                                      

''')

pathIn = input("Insert the path: ")
srcOut = pathIn + r"\Chrome"

print(colorama.Fore.YELLOW + "Copying the files...\n")

t = threading.Thread(target=copy)
t.start()
b = threading.Thread(target=checker , args=(src, srcOut))
b.start()


