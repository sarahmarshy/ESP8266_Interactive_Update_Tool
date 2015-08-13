# ESP8266-Interactive-Update-Tool
A companion tool to https://github.com/themadinventor/esptool for updating the firmware of ESP8266.
It is intended to be  run in the same directory as esptool.py.
If on linux, install tkinter with: sudo apt-get install python-tk.

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
