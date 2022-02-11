#!/usr/bin/python3
# Converts an IPv4 address into decimal or hexadecimal format

import sys

if (len(sys.argv) < 3):
    print("\nMissing argument!")
    print("e.g., D <IP>")
    print("Valid arguments: \n")
    print("-D  Decimal\n")
    print("-H  Hexadecimal\n")
    sys.exit(1)

argument = sys.argv[1]

def long(ip):
    ip = ip.split(".")
    ip = list(map(int, ip))
    longIP = (ip[0] * (2**24)) + (ip[1] * (2**16)) + ip[3]
    return longIP

ip = long(sys.argv[2])

if argument == "D":
    print("\nIP formatted as decimal: %s" % (ip))
    print("\nIP formatted as hexadecimal: %s" % (hex(ip)))
