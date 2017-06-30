import urllib
import sys
import os
import platform
import pip
import time
import json
import subprocess
import zipfile

useros = platform.system()
var = 1

if useros == 'Windows':
    clear = 'cls'
    title = 'title Osmibot Launcher'
elif useros == 'Linux':
    clear = 'clear'
    title = """PROMPT_COMMAND='echo -en "\033]0;Osmibot Launcher\a"'"""
else:
    clear = 'clear'
    title = 'echo -n -e "\033]0;Osmibot Launcher\007"'

def install(package):
    pip.main(['install', package])

while var == 1:
    os.system(title)
    os.system(clear)
    print('Osmibot Launcher v1.0')
    print('Select an option:')
    print('_____________________')
    print('1. Run Osmibot')
    print('2. Run Osmibot with autorestart in case of errors.')
    print('3. Install basic dependencies (no sound features)')
    print('4. Install all dependencies (recommended)')
    print('5. Configure Bot')
    print('6. Exit')
    print('7. Update/Install Osmibot')
    choice = input('Enter option number and press enter: ')

    if choice == '1':
        try:
            os.chdir('master')
            try:
                os.system('python osmibot.py')
            except Exception:
                os.system('python3 osmibot.py')
            os.chdir('..')
        except Exception:
            print('Bot currently not downloaded. Install dependencies and use option 6.')
            time.sleep(2)

    if choice == '2':
        if useros == 'Windows':
            print(os.getcwd())
            os.chdir('master')
            os.chdir('bin')
            os.system('autorestart.bat')
        else:
            print('Currently only supported on Windows.')

    if choice == '3':
        os.system(clear)
        print('Beginning install in 10 seconds.')
        time.sleep(10)
        os.system(clear)
        print('Installing discord.py and requirements...')
        install('discord.py')
        print('Installed dependencies!')
        time.sleep(3)

    if choice == '4':
        os.system(clear)
        print('Beginning install in 10 seconds.')
        time.sleep(10)
        os.system(clear)
        print('Installing discord.py, PyNaCl and requirements...')
        install('discord.py')
        install('PyNaCl')
        print('Installed dependencies!')
        time.sleep(3)

    if choice == '5':
        os.system(clear)
        tokendump = input("Enter your bot's token here: ")
        os.system(clear)
        clientdump = input("Enter your bot's client secret here: ")
        os.system(clear)
        ownerdump = input("Enter your user id here: ")
        os.system(clear)
        serverdump = input("Enter your server id here: ")
        os.system(clear)
        moddump = input("Enter the name of your mod role here: ")
        os.system(clear)
        admindump = input("Enter the name of your admin role here: ")
        data = {
            "token":tokendump,
            "client":clientdump
        }
        perms = {
            "ownerid":ownerdump,
            "serverid":serverdump,
            "modrole":moddump,
            "adminrole":admindump
        }
        os.chdir('master')
        with open('config.json', 'w') as f:
            json.dump(data, f)
        with open('permissions.json', 'w') as p:
            json.dump(perms, p)
        os.chdir('..')
        time.sleep(1)

    if choice == '6':
        sys.exit()

    if choice == '7':
        install('wget')
        import wget
        wget.download('https://github.com/ANT1H3R0/osmibot/archive/master.zip', 'master.zip')
        print('Downloaded')
        time.sleep(2)
        with zipfile.ZipFile('master.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.rename('osmibot-master', 'master')
        os.remove('master.zip')

    if choice == '1969':
        os.system(clear)
        print('Commencing Countdown, engines on...')
        time.sleep(2)
