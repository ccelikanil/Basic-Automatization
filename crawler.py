#!/usr/bin/python3

# needs a few updates, code is kinda shitty

from __future__ import print_function
import requests, sys, time, json, functools, operator, contextlib

headers = {
		'User-Agent': 'agent_smith',
		'Accept': 'accept_em_all',
		'Accept-Language': 'language',
		'Cookie': 'cookie_monster'
}

timeout = 5

with open(sys.argv[1], 'r') as inputFile:
	lineCount = len(open(sys.argv[1]).readlines( ))
	print("Total number of URLs:", lineCount)

	for line in inputFile:
		URL1 = 'http://' + line
		URL2 = 'https://' + line
		#URL3 = 'http://' + str(line).replace('\n','') + ':8080'
		
		try:		
			r1 = requests.get(URL1.strip(), headers=headers, timeout=timeout)
			r2 = requests.get(URL2.strip(), headers=headers, timeout=timeout)
			#r3 = requests.get(URL3.strip(), headers=headers, timeout=timeout)
		
			if (r1.status_code != 400 or r1.status_code != 404 or r1.status_code != 500) or (r2.status_code != 400 or r2.status_code != 404 or r2.status_code != 500):
				print("[+] ACTIVE:", line)
			#elif (r3.status_code != 400 or r3.status_code != 404 or r3.status_code != 500):
			#	print("[+] ACTIVE:", line)	
		except:
			print("[-] PASSIVE:", line)
