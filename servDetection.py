#!/bin/python3

import subprocess, re, itertools


def servDectScan(ip, openPorts):
	
	ip = str(ip)
	
	f = open("temp/sv.txt", "w+")
	for p in openPorts:
		
		try:
			
			p = str(p)
			
			y = subprocess.run(["nmap", "{}".format(ip), "-sV", "-oG", "-" ,"-p{}".format(p)], capture_output = True, text = True)
			z = y.stdout
			
			f.write(z)
			print("Scan Complete - Port: {}".format(str(p)))
			
		except:
			print('Scan Failed')
	f.close()
	
	
	
	f = open("temp/sv.txt", "r")
	
	combined = []	
			
	#--------------------------------------------------------------------------------------------------------------------------------------
	
	pattern = ("(?:\/\/\w+\/\/)(.*?)\/")
	pattern2 = ("(.*?)(?:\()")	
	for l in f:
		l = l.strip()
		a = re.findall(pattern, l)
		for s in a:
			s = s.strip()
			if '(' not in s or ')' not in s:
				combined.append(s)
			else:
				last = re.findall(pattern2, s)
				for e in last:
					e = e.strip()
					combined.append(e)
#------------------------------------------------------------------			
			
	
	print("The services on these ports read: \n")
	for s in combined:
		print(str(s))
	
	return combined
