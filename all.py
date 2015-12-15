#!/usr/bin/python
import os 
import subprocess,time

while 1:
	os.system("rm captura.txt")
	
	
	
	os.system("sudo /home/pi/pocketsphinx-0.8/src/programs/pocketsphinx_continuous -lm /home/pi/comandos/1891.lm -dict /home/pi/comandos/1891.dic > captura.txt -samprate 16000/8000/48000")
	
	
	
	os.system("./read.py")
