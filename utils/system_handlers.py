import subprocess
from os import getcwd


# opens a new process and runs the script given
def call_script(script_name):
    path = getcwd() + rf"\{script_name}"
    subprocess.Popen([path], shell=True, creationflags=subprocess.SW_HIDE)


