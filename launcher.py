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
    os.system(clear)
    os.system(title)
    print('Osmibot Launcher v1.0')
    print('Select an option:')
    print('_____________________')
    print('1. Run Osmibot')
    print('2. Run Osmibot with autorestart in case of errors.')
    print('3. Install dependencies')
    print('4. Configure Bot')
    print('5. Exit')
    print('6. Update/Install Osmibot')
    choice = input('Enter option number and press enter: ')

    if choice == '1':
        import master.osmibot

    if choice == '2':
        if useros == 'Windows':
            print(os.getcwd())
            os.chdir('master')
            os.chdir('bin')
            os.system('autorestart.bat')
            input('enter')
        else:
            print('Currently only supported on Windows.')

    if choice == '3':
        os.system(clear)
        print('WARNING: The following commands will only succesfully run with')
        print('admin privileges. If you are not running in administrator command')
        print('prompt, please close this window and relaunch as such now, unless you are running MacOS, or Linux,')
        print('in which case sudo will be prompted for at certain points in the installation.')
        print('Beginning install in 10 seconds.')
        time.sleep(10)
        os.system(clear)
        print('Installing discord.py and requirements...')
        install('discord.py')
        print('Installed dependencies!')
        time.sleep(3)

    if choice == '4':
        os.system(clear)
        tokendump = input("Enter your bot's token here: ")
        clientdump = input("Enter your bot's client secret here: ")
        data = {
            "token":tokendump,
            "client":clientdump
        }
        os.chdir('master')
        with open('config.json', 'w') as f:
            json.dump(data, f)
        os.chdir('..')
        time.sleep(2)

    if choice == '5':
        sys.exit()

    if choice == '6':
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
