# Author: Caleb Carlson
# Date Created: 1/6/2019

import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.fftpack import fft
import os
import struct

RATE = 44100
CHUNK = 1024

def main():
	print("Audio Visualizer (under development)...")

	device_info = {} 
	useloopback = False

	p = pyaudio.PyAudio()

	#Set default to first in list or ask Windows
	try:
		default_device_index = p.get_default_input_device_info()
	except IOError:
		default_device_index = -1

	#Select Device
	print ("Available devices:\n\n")
	for i in range(0, p.get_device_count()):
		info = p.get_device_info_by_index(i)
		print (str(info["index"]) + ": \t %s \n \t %s \n" % (info["name"], p.get_host_api_info_by_index(info["hostApi"])["name"]))

		if default_device_index == -1:
			default_device_index = info["index"]






if __name__ == '__main__':
	main()