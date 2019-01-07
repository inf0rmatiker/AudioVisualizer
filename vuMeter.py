# Author: Caleb Carlson
# Date Created: 1/6/2019
# Last Edited: 1/7/2019

import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.fftpack import fft
import os
import struct
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

class AudioVisualizer(object):

	def __init__(self):

		# constants
		self.RATE = 44100
		self.CHUNK = 2048
		self.CHANNELS = 2
		self.DATA_TYPE = np.int16
		self.useloopback = True
		self.deviceIndex = 7

		# members
		self.p = pyaudio.PyAudio()
		self.stream = self.p.open(format = pyaudio.paInt16,
                    channels = self.CHANNELS,
                    rate = self.RATE,
                    input = True,
                    frames_per_buffer = self.CHUNK,
                    input_device_index = self.deviceIndex,
                    as_loopback = self.useloopback)

		self.startLoopbackStreaming("wave")


	def startLoopbackStreaming(self, graphType="wave"):
		data = np.frombuffer(self.stream.read(self.CHUNK), dtype=self.DATA_TYPE)
		data = [element/2**15. for element in data[:len(data)//2]] # normalize between -1 and 1 and cut list in half

		# Plot the raw data
		plt.plot(data)
		plt.show()
		plt.pause(5)
	
		plt.close()
		self.stream.stop_stream()
		self.stream.close()
		self.p.terminate()



def main():
	av = AudioVisualizer()

	


def chooseDevice():
	print("Audio Visualizer (under development)...")

	device_info = {} 
	useloopback = True

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

	#Get input or default
	device_id = 7

	#Get device info
	try:
		device_info = p.get_device_info_by_index(device_id)
	except IOError:
		device_info = p.get_device_info_by_index(default_device_index)
		print ("Selection not available, using default.")

	print("Chosen device index: " + str(device_id))
	
	




if __name__ == '__main__':
	main()