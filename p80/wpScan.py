#!/bin/python3
import subprocess, time
def runWordP(ip, urls):
	scanData = []
	print("Attempting to run scan on {}".format(str(ip)))
	try:
		y = subprocess.run(['wpscan', '--update', '--url', ip, '-e', 'ap', '--api-token', 'BasWQP4ZAaNAeLqMrwtNdnnJG4wiK74vMvssEihqLEY'])
		wpOutput = y.stdout
		print('Scan Data for {}'.format(str(ip)))
		print(wpOutput)
		scanData.append(wpOutput)
		
		if len(urls) > 0:
			print("Running scans on the following URLs: ")
			for x in urls:
				x = str(x)
				print(x)
				time.sleep(4)
			try:
				for x in urls:
					y = subprocess.run(['wpscan', '--update', '--url', x, '-e', 'ap', '--api-token', 'BasWQP4ZAaNAeLqMrwtNdnnJG4wiK74vMvssEihqLEY'])
					wpOutput = y.stdout
					print(wpOutput)
					scanData.append(wpOutput)
				return scanData
			except KeyboardInterrupt:
				print("Cancelled by user. Saving results so far")
				return scanData
			except:
				print("One or more scan failed. Saving any data recorded so far")
				return scanData
	except:
		print("It seems not scans were run. Please report this failed scan attempt")
		return scanData


