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
import sys
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

class AudioVisualizer(object):

	def __init__(self, device_index, pyaudio_object):

		# pyqtgraph stuff
		pg.setConfigOptions(antialias=True)
		self.traces = dict()
		self.app = QtGui.QApplication(sys.argv)
		self.win = pg.GraphicsWindow(title='Audio Visualizer')
		self.win.setWindowTitle('Audio Visualizer')
		self.win.setGeometry(5, 115, 1910, 1070)

		wf_xlabels = [(0, '0'), (2048, '2048'), (4096, '4096')]
		wf_xaxis = pg.AxisItem(orientation='bottom')
		wf_xaxis.setTicks([wf_xlabels])

		wf_ylabels = [(-1, '-1'), (0, '0'), (1, '1')]
		wf_yaxis = pg.AxisItem(orientation='left')
		wf_yaxis.setTicks([wf_ylabels])


		self.waveform = self.win.addPlot(
			title='WAVEFORM', row=1, col=1, axisItems={'bottom': wf_xaxis, 'left': wf_yaxis},
		)

		# constants
		self.RATE = 44100
		self.CHUNK = 2048
		self.CHANNELS = 2
		self.DATA_TYPE = np.int16
		self.useloopback = True
		self.deviceIndex = device_index

		# members
		self.p = pyaudio_object
		self.stream = self.p.open(format = pyaudio.paInt16,
                    channels = self.CHANNELS,
                    rate = self.RATE,
                    input = True,
                    frames_per_buffer = self.CHUNK,
                    input_device_index = self.deviceIndex,
                    as_loopback = self.useloopback)

		self.x = np.arange(0, 2 * self.CHUNK, 2)

	def start(self):
		if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
			QtGui.QApplication.instance().exec_()

	def set_plotdata(self, name, data_x, data_y):
		if name in self.traces:
			self.traces[name].setData(data_x, data_y)
		else:
			if name == 'waveform':
				self.traces[name] = self.waveform.plot(pen='b', width=3)
				self.waveform.setYRange(-1.5, 1.5, padding=0)
				self.waveform.setXRange(0, 2 * self.CHUNK, padding=0.005)

	def startLoopbackStreaming(self, graphType="wave"):
		data = np.frombuffer(self.stream.read(self.CHUNK), dtype=self.DATA_TYPE)
		data = [element/2**15. for element in data[:len(data)//2]] # normalize between -1 and 1 and cut list in half

		self.set_plotdata(name='waveform', data_x=self.x, data_y=data,)

	def animation(self):
		timer = QtCore.QTimer()
		timer.timeout.connect(self.startLoopbackStreaming)
		timer.start(20)
		self.start()


def chooseDevice():
	print("Audio Visualizer (under development)...")

	p = pyaudio.PyAudio()
	device_info = {} 

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
	device_id = 7 # For now, default to 7 for testing. // TODO update to user input

	#Get device info
	try:
		device_info = p.get_device_info_by_index(device_id)
	except IOError:
		device_info = p.get_device_info_by_index(default_device_index)
		print ("Selection not available, using default.")

	print("Chosen device index: " + str(device_id))
	return device_id, p


def main():
	device_index, p = chooseDevice()
	av = AudioVisualizer(device_index, p)
	av.animation()


if __name__ == '__main__':
	main()