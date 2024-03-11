import shutil, os, colorama, threading, time, atexit
from art import *

#from email.message import EmailMessage

src: str = os.environ['USERPROFILE'] + r"\AppData\Local\Google\Chrome\User Data"
srcOut: str = ""
end: bool = False

@atexit.register
def resetColor() -> None:
    print(colorama.Fore.RESET)

def copy() -> None:
    global src, srcOut
    shutil.copytree(src, srcOut) #Copy the chrome folder in the destination folder
    print("\n\nOperation Completed")
    print(colorama.Fore.RESET)
    print("")
    return

def progressBar(progress, total) -> None: #Print the progression bar
    global end
    percent = 100 * (progress / float(total))
    bar = "█" * int(percent) + "-" * (100 - int(percent))
    if progress == total :
        print(colorama.Fore.GREEN + f"\r|{bar}| 100%", end="\r")
        end = True
    elif progress<total :
        print(colorama.Fore.YELLOW + f"\r|{bar}| {percent:.2f}%", end="\r")

def checker():
    global pathIn, src, end
    time.sleep(1)
    inp = pathIn

    while not os.path.exists(fr"{os.getcwd()}\{inp}"):
        print (fr"{os.getcwd()}\{inp}")
        time.sleep(.01)

    while os.path.getsize(src) >= os.path.getsize(fr"{os.getcwd()}\{inp}") and not end:
        progressBar(os.path.getsize(fr"{os.getcwd()}\{inp}\Chrome"), os.path.getsize(src))



print(colorama.Fore.CYAN)
tprint("NapoleChrome")

pathIn = input(f"Insert the output folder name: {colorama.Fore.RESET}")
print("\n")
srcOut = pathIn + r"\Chrome"

print(colorama.Fore.YELLOW + "Copying the files...\n")

t = threading.Thread(target=copy)
t.start()
b = threading.Thread(target=checker)
b.start()
