#!/bin/python3
import re, subprocess, pyfiglet, sys, time
sys.path.append('/root/reconProject/p80/')
from nikto import *
from wpScan import *
from urlRecon import *
from servDetection import *
from curl import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    


urls = []
	
def basicScan(ip):
	openPorts = []
	y = subprocess.run(["nmap", "-T4", "-p-", str(ip)], capture_output = True, text = True)
	scanOut = y.stdout
	scanOut = str(scanOut)
	
	pattern = (r"(\d+)(?:[/tcp])")
	x = re.findall(pattern, scanOut)
	for p in x:
		print("Found Open Port: " + str(p))
		openPorts.append(p)
	return openPorts
	
def advancedScan(ports, ip):
	advancedScanData = []
	for p in ports:
		y = subprocess.run(["nmap", "-T4","-A", "-p{}".format(str(p)), str(ip)], capture_output = True, text = True)
		scanOut = y.stdout
		print(scanOut)
		advancedScanData.append(scanOut)
	return advancedScanData
		
			
	

def main(ip):
	print(f"{bcolors.HEADER}Welcome to the Recon Tool. This tool is aimed at the automation of reconaissance and enumeration on the following target:{bcolors.ENDC}")
	ip = str(ip)
	print(ip)
	print('Starting process and beginning Nmap scans:')
	#time.sleep(5)
	p = basicScan(ip)
	
	if len(p) > 0:
		pReport = ('\n'.join(map(str, p)))
		print('Progressing onto Advanced Scan on the ports found: ')
		aS = advancedScan(p, ip)
		print('Scans Complete')
		aReport = ('\n'.join(map(str, aS)))
		
		print('Attempting to extract service data...')
		
		servDectScan(ip, p)
		
		print('Now progressing onto further scanning and enumeration. Depending on the ports listed as open, various scans will be run. This will take some time.')
		
		if '80' in p:
			
			try:
				print('Running Nikto. Please be patient.')
				rN = runNikto(ip)
				rNReport = rN
			except:
				print('Failed to run Nikto')
			try:
				print('Running URL Recon tool')
				urls = urlRecon(ip)
			except:
			
				print('Failed to run URL Recon')
		
			try:
				print('Running WPScan')
				wp = runWordP(ip, urls)
			except:
				print('WPScan Failed')	
			try:
				print('Gathering data with Curl')
				c = curl(ip)
			except:
				print("Curl failed to run")
	else:
		print('No open ports...')
		sys.exit()
	

ip = sys.argv[1]
match = re.findall(r'\d+[.]\d+[.]\d+', ip)

if len(match) == 1:
	print('Target IP: {}'.format(str(ip)))
	main(ip)


elif len(match) == 0:
	print('Please enter an IP address...')
	sys.exit()
	

else:
	print('Unable to recognise input')
	sys.exit()
	

	
	

	

	



	
		
	
	
	
	



