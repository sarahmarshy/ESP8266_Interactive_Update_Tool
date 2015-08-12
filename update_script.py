#Update script
#Intended to be run in the same directory as https://github.com/themadinventor/esptool
#Author: Sarah Marsh

import subprocess
import sys
import os
from Tkinter import *
import Tkinter
from tkMessageBox import askyesno, showwarning, showerror

class mainWindow(object):
    def __init__(self,master):
        fileFrame = Frame(master)
        fileFrame.pack()

        comPortFrame = Frame(master)
        comPortFrame.pack()

        labelText=StringVar()
        labelText.set("Root directory of firmware")
        labelDir=Label(fileFrame, textvariable=labelText, justify = LEFT)
        labelDir.pack(side = LEFT)

        self.fileEntry = Entry(fileFrame, width = 50)
        self.fileEntry.pack(side = LEFT)

        browseButton = Button(fileFrame, text = "Browse", command = self.browse_dirs)
        browseButton.pack(side = LEFT)

        labelText=StringVar()
        labelText.set("Port of mbed (COMX or dev/sda/..)")
        labelDir=Label(comPortFrame, textvariable=labelText, justify = LEFT)
        labelDir.pack(side = LEFT)

        self.comEntry= Entry(comPortFrame, width = 10)
        self.comEntry.pack(side = LEFT)

        updateButton = Button(master, text = "Update Firmware", command = self.update)
        updateButton.pack()

    def browse_dirs(self):
        from tkFileDialog import askdirectory
        self.bin_dir = askdirectory()
        self.fileEntry.delete(0,END)
        self.fileEntry.insert(0,self.bin_dir)

    def update(self):
        com = self.comEntry.get()
        dir = self.fileEntry.get()
        user1_file = os.path.join("newest","user1.bin")
        files = [os.path.join(dir, "bin",file) for file in ["boot_v1.1.bin", user1_file, "blank.bin", "blank.bin"]]
        if any(not(os.path.exists(file)) for file in files):
            list = "\n".join(files)
            showerror("Fatal Error", "One of these files does not exist:\n%s"%list)
            return

        commands = []
        commands.append(self.format_command(com, "0x00000", files[0]))
        commands.append(self.format_command(com, "0x01000", files[1]))
        commands.append(self.format_command(com, "0x7C000", files[2]))
        commands.append(self.format_command(com, "0x7E000", files[3]))

        for c in commands:
            success = False
            while not success:
                print("calling: "+" ".join(c))
                p = subprocess.Popen(c, stdout=subprocess.PIPE, bufsize=1)
                for line in iter(p.stdout.readline, b''):
                    print line,
                p.stdout.close()
                p.wait()
                if p.poll()!=0:
                    askyesno("Warning", "Failed to connect.\nAre you sure your board is connected to the specified port?\n"
                                           "If so, try power cycling.")
                else:
                    askyesno("Power Cycle", "Success. Power cycle your board to continue.")
                    success = True

    def format_command(self,com, hex, file):
        return ["python", "esptool.py", "-p", com, "-b", "9600", "write_flash", hex, file]

root = Tk()
window=mainWindow(root)
root.mainloop()