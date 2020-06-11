#!/bin/python3

import subprocess

def runNikto(ip):
	try:
		y = subprocess.run(['nikto', '--url', ip], capture_output = True, text = True)
		nmapSMBOut = y.stdout
		nmapSMBOut = str(nmapSMBOut)
		print(nmapSMBOut)
		return(nmapSMBOut)
	except:
		print('Failed to run Nikto')



