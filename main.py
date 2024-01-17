import shutil, os, smtplib
#from email.message import EmailMessage

src = os.environ['USERPROFILE'] + r"\AppData\Local\Google\Chrome"
dst = input("Percorso destinazione: ")

shutil.copytree(src, dst + r"\Chrome")
