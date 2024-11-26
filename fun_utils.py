import os 

command = "dir"

def cmd(command):
    print(os.system(command))

command = input("ENTER COMMAND: ")

cmd(command)
