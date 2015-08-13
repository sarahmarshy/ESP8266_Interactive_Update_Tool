#Update script
#Intended to be run in the same directory as https://github.com/themadinventor/esptool
#Author: Sarah Marsh
#if on linux, install tkinter with: sudo apt-get install python-tk

import subprocess
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', dest = 'root_dir', help = 'The root directory of ESP8266 firmware')
    parser.add_argument('-port', dest = 'port', help = 'Port of device you are updating in the form of COMX or /dev/sda/..')
    args = parser.parse_args()

    def format_command(com, hex, file):
        return ["python", "esptool.py", "-p", com, "-b", "9600", "write_flash", hex, file]

    def update(com,dir):
        user1_file = os.path.join("newest","user1.bin")
        files = [os.path.join(dir, "bin",file) for file in ["boot_v1.1.bin", user1_file, "esp_init_data_default.bin", "blank.bin"]]
        if any(not(os.path.exists(file)) for file in files):
            list = "\n".join(files)
            raise RuntimeError("Fatal Error! Did you choose the correct root directory?\nOne of these files does not exist:\n%s"%list)

        commands = []
        commands.append(format_command(com, "0x00000", files[0]))
        commands.append(format_command(com, "0x01000", files[1]))
        commands.append(format_command(com, "0x7C000", files[2]))
        commands.append(format_command(com, "0x7E000", files[3]))

        for i,c in enumerate(commands):
            success = False
            while not success:
                print("calling: "+" ".join(c))
                p = subprocess.Popen(c, stdout=subprocess.PIPE, bufsize=1)
                for line in iter(p.stdout.readline, b''):
                    print line,
                p.stdout.close()
                p.wait()
                if p.poll()!=0:
                    if not raw_input("Warning! Failed to connect.\nAre you sure your board is connected to the specified port? (Enter 0 if not)\n"
                                           "If so, try power cycling, then press 1.\n"):
                        return
                else:
                    if(i!=3):
                        raw_input("Success. Power cycle your board and press ENTER to continue.")
                    success = True
        print("Success! Firmware successfully updated!")

    update(args.port, args.root_dir)


if __name__ == '__main__':
    main()
