from Geometry import Point
from Geometry import Line
from Geometry import Shape
from Vector import Vec2
from Map import Map
from Pathfinder import Pathfinder
from SavePath import SavePath

import sys
import random
import math
import time
import copy

class IntelliMower():
	state = 0
	mowOffset = 30
	posX = 0
	posY = 0
	lawn = Map(mowOffset)
	path = Pathfinder()

	#
	def __init__(self):
		self.pathCalcComplete 	= 0
		self.isMowerPlaced		= 0
		self.isStationPlaced	= 0
		self.state 				= 0
		self.bladesOn 			= 0
		self.mowOffset 			= 30
		self.posX 				= 0
		self.posY 				= 0
		self.stationPosX		= 0
		self.stationPosY 		= 0
		self.lawn 				= Map( self.mowOffset )
		self.path 					= Pathfinder()

	#
	def SetState(self, state):
		self.calcDone = 0
		self.state = state

		# print( "IntelliMowerState:", state )
		# add new obstacle everytime state is set to 2
		if self.state == 2:
			newObstacle = Shape()
			self.lawn.innerBorders.append(newObstacle)
			self.lawn.innerBorders[-1].id = len( self.lawn.innerBorders )
			#print("Obstacle Id:", len( self.lawn.innerBorders ) )

	#
	def PlaceMower(self, x, y):
		self.pathCalcComplete = 0
		self.path.Reset()
		self.posX = x
		self.posY = y
		print ("Mower position ", x, y)
		self.path.UpdatePos( x, y )
		self.path.Init( self.lawn.outerBorder, self.lawn.innerBorders, self.lawn.collisionPairs )
		self.isMowerPlaced = 1
		if self.isStationPlaced:
			self.path.UpdateStationPos( self.stationPosX, self.stationPosY )
			self.path.Init( self.lawn.outerBorder, self.lawn.innerBorders, self.lawn.collisionPairs )

	#
	def PlaceStation(self, x, y):
		if self.isMowerPlaced == 1:
			self.stationPosX = x
			self.stationPosY = y
			self.pathCalcComplete = 0
			self.path.Reset()
			print ("Station position ", x, y )
			self.path.UpdateStationPos( x, y )
			self.path.UpdatePos( self.posX, self.posY )
			self.path.Init( self.lawn.outerBorder, self.lawn.innerBorders, self.lawn.collisionPairs )
			self.isStationPlaced = 1

	#
	def Calculate(self):
		self.lawn.Calculate()
		self.path.Init( self.lawn.outerBorder, self.lawn.innerBorders, self.lawn.collisionPairs )

	#
	def FindNextPath(self):
		# if no map calculated exit
		if self.lawn.calcDone != 1:
			return

		if self.path.pathingComplete == 0:
			self.path.FindNextPath()
		else:
			self.pathCalcComplete = 1

	#
	def CalculatePath(self):
		# if no map calculated exit
		print "implement Calculate Path for the raspberry"
		startTime = time.time()
		while self.pathCalcComplete != 1:
			newTime = time.time() - startTime
			self.FindNextPath()
		elapsedTime = time.time() - startTime
		print ( "Elapsed Time:", elapsedTime )
		self.SavePath()

	# Runs when clicking mouse on the map in user interface
	def Controller(self, x=0, y=0):
		if self.state == 0:
			return
		# state 1 is in Set Lawn Boundary Mode
		elif self.state == 1:
			newLawnPoint = Point(x, y)
			newLawnPoint.borderId = 0
			self.lawn.outerBorder.AddBorderPoint(newLawnPoint)

		# state 2 is in Set Obstacle Boundary Mode
		elif self.state == 2:
			newObstaclePoint = Point(x, y)
			newObstaclePoint.borderId = len( self.lawn.innerBorders )
			self.lawn.innerBorders[-1].AddBorderPoint(newObstaclePoint)

		# state 3 place the mower with mouse click
		elif self.state == 3:
			self.PlaceMower(x,y)

		# state 4 place the charging station with mouse click
		elif self.state == 4:
			self.PlaceStation(x,y)

	#
	def SaveMap(self):
		mower = None
		station = None
		if self.isMowerPlaced:
			mower = Point(self.posX, self.posY)
			mower.borderId = 0
		if self.isStationPlaced:
			station = Point(self.stationPosX, self.stationPosY)
			station.borderId = 0

		self.lawn.SaveMap( mower, station)

	#
	def LoadMap(self):
		self.lawn.LoadMap()
		if self.lawn.mowerPoint:
			self.posX = self.lawn.mowerPoint.x
			self.posY = self.lawn.mowerPoint.y
			self.PlaceMower(self.posX,self.posY)
		if self.lawn.stationPoint:
			self.stationPosX = self.lawn.stationPoint.x
			self.stationPosY = self.lawn.stationPoint.y
			self.PlaceStation(self.stationPosX, self.stationPosY)

	#
	def SavePath(self):
		if self.pathCalcComplete:
			self.path.pathList.reverse()
			#for point in self.path.pathList:
				#print point.x, point.y
			SavePath(self.path.pathList)
			self.path.pathList.reverse()

	#
	def Reset(self):
		self.pathCalcComplete 	= 0
		self.isMowerPlaced		= 0
		self.isStationPlaced	= 0
		self.SetState(0)
		self.posX 				= 0
		self.posY 				= 0
		self.stationPosX		= 0
		self.stationPosY 		= 0
		self.path.Reset()
		self.lawn.Reset()
