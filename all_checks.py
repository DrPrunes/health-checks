#!/usr/bin/python3
import os
import sys

def check_reboot():
	''' Returns True if theres na pending reboot '''
	return os.path.exist("/run/reboot-required")
def main():
	if check_reboot():
		print("Pending Reboot")
		sys.exit(1)

main()
