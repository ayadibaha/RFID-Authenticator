#!/usr/bin/python

import serial

class Config(object):
	def __init__(self, device, port):
		try:
			print "Trying...",device
			self.connection = serial.Serial(device, port)
		except:
			print "Failed to connect on",device
			self.connection = "Error connecting to the device"
	def getConnection(self):
		return self.connection

