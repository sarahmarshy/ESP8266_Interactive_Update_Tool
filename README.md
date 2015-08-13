# ESP8266_Interactive_Update_Tool
A companion tool to [this repository](https://github.com/themadinventor/esptool) for updating the firmware of ESP8266.
It is intended to execute in the same directory as esptool.py.

##update_gui.py 
An interactive GUI for updating the firmware.

*If you want to use the GUI version on linux, install tkinter with:* sudo apt-get install python-tk. *Tkinter works natively on Windows.*

##update.py 
A command line tool. Use ```python update.py --help``` for usage. 


Follow the instructions outlined [here](https://developer.mbed.org/teams/ESP8266/wiki/Firmware-Update).

When you get to the section about running esptool commands, stop there, and launch this script in the same directory as esptool.py.

In both programs, you will need to know the root directory for the firmware binaries, as well as the serial port where your device is connected. The root directory of the firmware means the parent directory of the "bin" and "at" directories. 
Its struture should look like:

```
Root Directory
|
|---->at
|       makefile
|       gen_misc.*
|------->driver 
|------->include
|------->user
|
|---->bin
|       blank.bin
|       boot_v1.1.bin
|       esp_init_data_default.bin
|------->newest
|------->v0.20
```


In addition, the esptool writes binaries to flash to upgrade the firmware. Between each write, the device will need to be *power cycled*. Power cycle means a **complete** detachment from the device's power source, *not* just a processor reset. The program will prompt you multiple times to do this between each flash write, so beware that this program requires some user input while executing.
