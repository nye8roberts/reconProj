#!/bin/python3
import re, subprocess

def curl(ip):
	y = subprocess.run(['curl', '-V', '--url', ip])
	curlOut = y.stdout
	curlOut = str(curlOut)
	print(curlOut)
	return(curlOut)
