import os
import subprocess

def silent_install(command):
   
    subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Installing...")

if os.name == 'posix':
    distro = os.popen('uname -a').read().lower()
    
    if 'ubuntu' in distro or 'debian' in distro:
        silent_install("sudo apt install -y python3-tk")
    elif 'fedora' in distro:
        silent_install("sudo dnf install -y python3-tkinter")
    elif 'arch' in distro:
        silent_install("sudo pacman -S --noconfirm tk")
    elif 'darwin' in distro:  
        silent_install("brew install python-tk")

print("Installation completed. Running main.py")

silent_install("pip install flake8")
silent_install("python main.py")
