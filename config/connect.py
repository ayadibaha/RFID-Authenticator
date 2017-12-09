#!/usr/bin/python

import serial
import serial.tools.list_ports

class Config(object):
	'''
	arduino_devices = [
		p.device
		for p in serial.tools.list_ports.comports()
		if 'Arduino' in p.description
	]
	'''
	def __init__(self):
		#if self.arduino_devices:
		self.connection = serial.Serial("/dev/ttyACM0",9600)
		if self.connection:
			print "Connected on Arduino"
			print self.connection
		else:
			self.connection = "Error: No devices found"
			print self.connection
	def getConnection(self):
		return self.connection

