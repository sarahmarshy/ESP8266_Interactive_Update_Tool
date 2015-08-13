# ESP8266_Interactive_Update_Tool
A companion tool to https://github.com/themadinventor/esptool for updating the firmware of ESP8266.
It is intended to be  run in the same directory as esptool.py.

update_gui.py is, as you might guess, an interactive GUI for updating the firmware.
update.py is a command line tool. Use ```python update.py --help`` for usage. 

If you want to use the GUI version on linux, install tkinter with: sudo apt-get install python-tk. Tkinter works natively on Windows.

Follow the instructions outlined here : https://developer.mbed.org/teams/ESP8266/wiki/Firmware-Update.

When you get to the section about running esptool commands, launch this script in the same directory as esptool.py.

The root directory of the firmware means the parent directory of the "bin" and "at" directories. 
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


In addition, the esptool writes binaries to flash to upgrade the firmware. Between each write, the device will need to be power cycled. Power cycle means a complete detachment from the device's power source, not just a processor reset. The program will prompt you multipe times to do this between each flash write, so beware that this program requires some user input while executing.
