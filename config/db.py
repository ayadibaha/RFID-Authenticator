#!/usr/bin/python


import sqlite3 as sql

class Db(object):
	def __init__(self):
		try:
			self.cnx = sql.connect('test.db')
			self.cursor = self.cnx.cursor()
			print "Database Connection Successfully"
		except:
			print "Failed to connect to Database"
	def getUser(self, code):
		self.user = self.cursor.execute('''SELECT * FROM users WHERE code=?''',code)
		return self.user
	def getCursor(self):
		return self.cursor
