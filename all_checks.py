#!/usr/bin/python3
import os
import sys
import csv

def check_reboot():
	''' Returns True if theres na pending reboot '''
	return os.path.exists("/run/reboot-required")
def main():
	if check_reboot():
		print("Pending Reboot")
		sys.exit(1)

	print("Everything OK. Continue")
	sys.exit(0)

main()
