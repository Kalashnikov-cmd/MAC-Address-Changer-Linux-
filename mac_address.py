#! /usr/bin/env python

import subprocess

print("Available interfaces and its corresponding MAC addresses:\n")
subprocess.call("ifconfig | sed -En -rn '/^[^[:space:]]/p; /ether/p'", shell=True)
print("")

interface = input("Enter the interface:")
mac = input("Enter new MAC Address:")

subprocess.call("sudo ifconfig " + interface + " down", shell=True)
subprocess.call("sudo ifconfig " + interface + " hw ether " + mac, shell=True)
subprocess.call("sudo ifconfig " + interface + " up", shell=True)
