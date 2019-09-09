#!/usr/bin/python
import os
Cmd1 = 'speedtest' 
print("1) speedtest")
Cmd2 = 'ping -c 4 google.com'
print("2) Ping Test")
Cmd3 = ('ifconfig')
print("3) IP Address")
Cmd4 = ('exit')
print("4) Exit")
num = input( "Enter Number :" )
Cmd = int(num)
if Cmd == 1:
    os.system(Cmd1)

if Cmd == 2:
    os.system(Cmd2)

if Cmd == 3:
    os.system(Cmd3)

if Cmd == 4:
    os.system(Cmd4)