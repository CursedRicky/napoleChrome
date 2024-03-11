import shutil, os, colorama, threading, time
from art import *
#from email.message import EmailMessage

src = os.environ['USERPROFILE'] + r"\AppData\Local\Google\Chrome\User Data"
srcOut = ""

def copy() :
    shutil.copytree(src, srcOut) #Copy the chrome folder in the destination folder

def progressBar(progress, total): #Print the progression bar
    percent = 100 * (progress / float(total))
    bar = "█" * int(percent) + "-" * (100 - int(percent))
    if progress == total :
        print(colorama.Fore.GREEN + f"\r|{bar}| 100%", end="\r")
    elif progress<total :
        print(colorama.Fore.YELLOW + f"\r|{bar}| {percent:.2f}%", end="\r")

def checker(source_path, inp):
    time.sleep(1)

    while not os.path.exists(fr"{os.getcwd()}\{inp}"):
        print (fr"{os.getcwd()}\{inp}")
        time.sleep(.01)

    while os.path.getsize(source_path) >= os.path.getsize(fr"{os.getcwd()}\{inp}"):
        progressBar(os.path.getsize(fr"{os.getcwd()}\{inp}\Chrome"), os.path.getsize(src))

    print("\n\nOperation Completed")
    print(colorama.Fore.RESET)
    print("")

print(colorama.Fore.CYAN)
tprint("NapoleChrome")

pathIn = input("Insert the path: ")
print("\n")
srcOut = pathIn + r"\Chrome"

print(colorama.Fore.YELLOW + "Copying the files...\n")

t = threading.Thread(target=copy)
t.start()
b = threading.Thread(target=checker , args=(src, pathIn))
b.start()
