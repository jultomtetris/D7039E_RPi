#!/usr/bin/python
# -*- coding: utf-8 -*-

#from UserInterface import UserInterface
from IntelliMower import IntelliMower
import sys, time
#from PyQt4 import QtGui, QtCore

#
class Common():
	initialized = 0

	# comment in these for user interface
	#app = QtGui.QApplication(sys.argv)
	#ui = UserInterface()

	def __init__(self):
		self.initialized = 0

	def Init(self):
			self.iMower = IntelliMower()

			# comment in these for user interface
			#self.ui.Init( 800, 800 )
			self.initialized = 1

	def Frame(self):
		self.iMower.Reset()
		self.iMower.LoadMap()
		self.iMower.SetState(0)
		self.iMower.Calculate()
		#
		# #self.iMower.PlaceMower(685, 417)
		#
		#self.iMower.SetState(0)
		#
		self.iMower.CalculatePath()

		# Comment in for user interface
		#sys.exit(self.app.exec_())
