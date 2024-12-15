import os

class utilities:

    def disk_space(self):
        print(os.system("df -h"))

    def show_RAM(self):
        print(os.system("free -h"))

    def show_sys_details(self):
        print(os.uname().sysname)

machine_a = utilities()

machine_a.disk_space()

machine_b = utilities()

machine_b.show_sys_details()