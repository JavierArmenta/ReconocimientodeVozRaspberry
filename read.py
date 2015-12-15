#!/usr/bin/python
import os
import time

i=0



while i != 1:
	infile = open('/home/pi/captura.txt','r')

	for line in infile:
		if line.find("GO")!=-1:
			os.system("sudo python comando.py")
			
		if line.find("STOP")!=-1:
			os.system("sudo python comando2.py")
		if line.find("LEFT")!=-1:    
			os.system("sudo python comando3.py")
		if line.find("RIGHT")!=-1:
			os.system("sudo python comando4.py")
		if line.find("AUTOMATIC")!=-1:
			os.system("sudo python comando5.py")
		if line.find("MANUAL")!=-1:
			os.system("sudo python comando6.py")
		if line.find("SHUTDOWN")!=-1:
			os.system("sudo python comando7.py")

	i=1

infile.close()
time.sleep(2)

