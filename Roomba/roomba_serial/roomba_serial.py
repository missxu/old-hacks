#!/usr/bin/python

import serial
import sys
import time

SERIAL_PORT = "/dev/cu.usbserial-AI02KGID"

port = serial.Serial(SERIAL_PORT, baudrate=115200, timeout=1.0)

if sys.argv[1] == "bytes":
    # Interpret remaining arguments as character values to send
    for arg in range(2, len(sys.argv)):
        char = int(sys.argv[arg])
        port.write("%c" % char)
elif sys.argv[1] == "beep":
    # Commands taken from http://www.robotappstore.com/Knowledge-Base/4-How-to-Send-Commands-to-Roomba/18.html
    port.write("%c%c" % (128, 132))
    time.sleep(0.5)
    # Program song #1
    port.write("%c%c%c%c%c" % (140, 0, 1, 62, 32))
    time.sleep(0.5)
    # Play song #1
    port.write("%c%c" % (141, 0))
elif sys.argv[1] == "song":
    # Commands taken from http://www.robotappstore.com/Knowledge-Base/4-How-to-Send-Commands-to-Roomba/18.html
    port.write("%c%c" % (128, 132))
    time.sleep(0.5)
    # Program song #1
    port.write("%c%c%c%c%c%c%c%c%c" % (140, 0, 3, 55, 32, 62, 32, 48, 32))
    time.sleep(0.5)
    # Play song #1
    port.write("%c%c" % (141, 0))
elif sys.argv[1] == "forward":
    # Commands taken from http://www.robotappstore.com/Knowledge-Base/4-How-to-Send-Commands-to-Roomba/18.html
    port.write("%c%c" % (128, 131))
    time.sleep(0.5)
    # March forward.
    port.write("%c%c%c%c%c" % (137, 0, 100, 128, 0))
elif sys.argv[1] == "backward":
    # Commands taken from http://www.robotappstore.com/Knowledge-Base/4-How-to-Send-Commands-to-Roomba/18.html
    port.write("%c%c" % (128, 131))
    time.sleep(0.5)
    # March forward.
    port.write("%c%c%c%c%c" % (137, 255, 56, 128, 0))
elif sys.argv[1] == "stop":
    # Commands taken from http://www.robotappstore.com/Knowledge-Base/4-How-to-Send-Commands-to-Roomba/18.html
    port.write("%c%c" % (128, 131))
    time.sleep(0.5)
    # March forward.
    port.write("%c%c%c%c%c" % (137, 0, 0, 128, 0))
elif sys.argv[1] == "spin":
    # Commands taken from http://www.robotappstore.com/Knowledge-Base/4-How-to-Send-Commands-to-Roomba/18.html
    port.write("%c%c" % (128, 131))
    time.sleep(0.5)
    # March forward.
    port.write("%c%c%c%c%c" % (137, 0, 20, 0, 20))

