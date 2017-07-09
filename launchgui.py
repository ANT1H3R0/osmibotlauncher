import sys
import os
import platform
import pip
import time
import json
import subprocess
import zipfile
from tkinter import *
from tkinter import messagebox
try:
    import wget
except ImportError:
    print('wget currently not installed. Please run option 3 or 4.')
    time.sleep(2)

useros = platform.system()

if useros == 'Windows':
    clear = 'cls'
    os.system('title Input')
elif useros == 'Linux':
    clear = 'clear'
else:
    clear = 'clear'

def install(package):
    pip.main(['install', package])

class Launcher(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('Osmibot Launcher')
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        setup = Menu(menu)
        setup.add_command(label='Configure Settings', command=self.config)
        setup.add_command(label='Download Bot', command=self.download)
        setup.add_command(label='Cog Loader', command=self.cogloader)
        menu.add_cascade(label='Setup', menu=setup)

        deps = Menu(menu)
        deps.add_command(label='Install Basic Dependencies', command=self.basic)
        deps.add_command(label='Install All Dependencies', command=self.alldeps)
        menu.add_cascade(label='Dependencies', menu=deps)


        osmi = Label(self.master, text="Osmibot", font=("Arial", 36))
        osmi.place(x=100, y=75)

        start = Button(self.master, text='Start Bot', command=self.start)
        start.place(x=160, y=150)

    def client_exit(self):
        exit()

    def start(self):
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
        os.system(clear)

    def cogloader(self):
        os.chdir('master')
        if useros == 'Windows':
            os.system('python cogloader.py')
        else:
            os.system('python3 cogloader.py')
        os.chdir('..')

    def config(self):
        messagebox.showinfo('Config', 'Config opened in console.')
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
        os.system(clear)
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
        try:
            os.chdir('master')
        except Exception:
            messagebox.showinfo('Error', 'Master directory does not exist. Download Bot first.')
        with open('config.json', 'w') as f:
            json.dump(data, f)
        with open('permissions.json', 'w') as p:
            json.dump(perms, p)
        os.chdir('..')
        time.sleep(1)
        os.system(clear)

    def basic(self):
        messagebox.showinfo('Basic Dependencies', 'Installing Basic Dependencies in Console')
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
        os.system(clear)

    def alldeps(self):
        messagebox.showinfo('All Dependencies', 'Installing All Dependencies in Console')
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
            messagebox.showinfo('Error', 'Windows installation of FFMPEG must be done manually.')
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
        time.sleep(3)
        os.system(clear)

    def download(self):
        messagebox.showinfo('Downloading Bot', 'Downloading Bot in Console')
        try:
            wget.download('https://github.com/ANT1H3R0/osmibot/archive/master.zip', 'master.zip')
            print('Downloaded')
            time.sleep(2)
            print('Unzipping...')
            with zipfile.ZipFile('master.zip', 'r') as zip_ref:
                zip_ref.extractall()
            os.rename('osmibot-master', 'master')
            os.remove('master.zip')
        except Exception as e:
            print('Error!')
            print(e)
            input('Press enter to continue...')
        os.system(clear)

root = Tk()
root.geometry('400x300')
app = Launcher(root)
root.mainloop()
