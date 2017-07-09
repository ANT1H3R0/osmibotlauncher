import sys
import os
import platform
import pip
import time
import json
import subprocess
import zipfile
import requests
try:
    import wget
except ImportError:
    print('wget currently not installed. Please run option 3 or 4.')
    time.sleep(2)

useros = platform.system()
pythonver = sys.version_info[0]
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
    print('2. Become a whale')
    print('3. Install basic dependencies (no sound features)')
    print('4. Install all dependencies (recommended)')
    print('5. Configure Bot')
    print('6. Exit')
    print('7. Update/Install Osmibot')
    print('8. Launch cogloader')
    choice = input('Enter option number and press enter: ')

    if choice == '1':
        try:
            os.chdir('master')
            if useros == 'Windows':
                os.system('python osmibot.py')
            else:
                os.system('python3 osmibot.py')
            os.chdir('..')
        except Exception:
            print('Bot currently not downloaded. Install dependencies and use option 6.')
            time.sleep(2)

    if choice == '2':
        os.system(clear)
        print('What did you expect would happen?')
        time.sleep(2)

    if choice == '3':
        os.system(clear)
        print('The following operations require sudo on linux.')
        print('If the launcher is not being run as sudo, exit now.')
        input('Press enter to continue.')
        os.system(clear)
        print('Installing discord.py, aiofiles, wget and requirements...')
        install('discord.py')
        install('aiofiles')
        install('wget')
        print('Installed dependencies!')
        time.sleep(3)

    if choice == '4':
        os.system(clear)
        print('The following operations require administrator access.')
        print('If you are not running in an administrative terminal/sudo, exit the program now.')
        input('Press enter to continue.')
        os.system(clear)
        print('Installing discord.py, aiofiles, cffi, pycparser, PyNaCl, youtube_dl, wget and requirements...')
        install('discord.py')
        install('aiofiles')
        install('PyNaCl')
        install('youtube_dl')
        install('wget')
        install('cffi')
        install('pycparser')
        print('Installed python dependencies!')
        time.sleep(1)
        print('Installing ffmpeg...')
        if useros == 'Windows':
            if platform.machine().endswith('64'):
                wget.download('https://www.videohelp.com/download/ffmpeg-3.3.2-win64-static.zip')
                ffmpegzip = 'ffmpeg-3.3.2-win64-static.zip'
            else:
                wget.download('https://www.videohelp.com/download/ffmpeg-3.3.2-win32-static.zip')
                ffmpegzip = 'ffmpeg-3.3.2-win32-static.zip'
            with zipfile.ZipFile(ffmpegzip) as zip_ref:
                for file in zip_ref.namelist():
                    if file.startswith('bin'):
                        zip_ref.extract(file, 'master')
            ffmpegpath = os.getcwd() + '\master\bin'
            os.system('setx /M PATH="' + ffmpegpath + ';%PATH%"')
        elif useros == 'Linux':
            os.system('add-apt-repository ppa:mc3man/trusty-media')
            os.system('apt-get update')
            os.system('apt-get install ffmpeg')
            os.system('apt-get install frei0r-plugins')
        elif useros == 'Darwin':
            print('Mac Installation requires that you currently have homebrew installed.')
            print('If homebrew is not installed, please close the program and install it.')
            input('Press enter to continue.')
            os.system('brew install ffmpeg --with-fdk-aac --with-ffplay --with-freetype --with-frei0r --with-libass --with-libvo-aacenc --with-libvorbis --with-libvpx --with-opencore-amr --with-openjpeg --with-opus --with-rtmpdump --with-schroedinger --with-speex --with-theora --with-tools')
        print('Installed all depedencies!')

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
        try:
            wget.download('https://github.com/ANT1H3R0/osmibot/archive/master.zip', 'master.zip')
            print('Downloaded')
            time.sleep(2)
            with zipfile.ZipFile('master.zip', 'r') as zip_ref:
                zip_ref.extractall()
            os.rename('osmibot-master', 'master')
            os.remove('master.zip')
        except Exception as e:
            print('Error!')
            print(e)
            input('Press enter to continue...')

    if choice == '8':
        os.chdir('master')
        if useros == 'Windows':
            os.system('python cogloader.py')
        else:
            os.system('python3 cogloader.py')
        os.chdir('..')

    if choice == '1969':
        os.system(clear)
        print('Commencing Countdown, engines on...')
        time.sleep(2)
