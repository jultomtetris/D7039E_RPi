from Geometry import Point
from Geometry import Line
from Geometry import Shape

class MapLoader():
	shape = Shape()
	shapes = []

	loadState = 0

	def __init__(self):
		self.mowerP 	= None
		self.stationP 	= None
		self.shape 		= Shape()
		self.shapes 	= []
		self.loadState 	= 0

	#
	def LoadMap(self):
		self.shape 		= Shape()
		self.shapes 	= []
		self.loadState 	= 0
		self.lawn 		= 'lawn'
		self.obstacle 	= 'obstacle'
		self.mower 		= 'mower'
		self.station 	= 'station'

		f = open("/home/pi/catkin_ws/src/intelli_mower/src/IntelliMowerAlgorithmRoS/src/map_one", 'r')
		for line in f:
			if line.strip() == str(self.lawn):
				self.loadState = 3

			elif line.strip() == str(self.obstacle):
				self.loadState = 4
				newShape = Shape()
				self.shapes.append( newShape )

			elif line.strip() == str(self.mower):
				self.loadState = 1


			elif line.strip() == str(self.station):
				self.loadState = 2


			else:
				if self.loadState == 1:
					cords = line.split()
					self.mowerP = Point( float(cords[0]), float(cords[1]) )
					self.mowerP.borderId = int(cords[2])

				elif self.loadState == 2:
					cords = line.split()
					self.stationP = Point( float(cords[0]), float(cords[1]) )
					self.stationP.borderId = int(cords[2])

				# load outer border
				elif self.loadState == 3:
					cords = line.split()
					p = Point( float(cords[0]), float(cords[1]) )
					p.borderId = int(cords[2])
					self.shape.AddBorderPoint( p )

				# load inner border
				elif self.loadState == 4:
					cords = line.split()
					p = Point( float(cords[0]), float(cords[1]) )
					p.borderId = int(cords[2])
					self.shapes[-1].AddBorderPoint( p )
		f.close()

	#
	def SaveMap(self, lawn, obstacles, mower=None, station=None):
		s = lawn
		obstacles = obstacles
		f = open("/home/pi/catkin_ws/src/intelli_mower/src/IntelliMowerAlgorithmRoS/src/map_one", 'w')
		if mower:
			f.write("%s\n" % 'mower')
			f.write("%s" % mower.x )
			f.write(' ')
			f.write("%s" % mower.y )
			f.write(' ')
			f.write("%s\n" % 0 )

		if station:
			f.write("%s\n" % 'station')
			f.write("%s" % station.x )
			f.write(' ')
			f.write("%s" % station.y )
			f.write(' ')
			f.write("%s\n" % 0 )

		f.write("%s\n" % 'lawn')
		for point in s.pointList:
			f.write("%s" % point.x )
			f.write(' ')
			f.write("%s" % point.y )
			f.write(' ')
			f.write("%s\n" % point.borderId )

		for shape in obstacles:
			f.write("%s\n" % 'obstacle')
			for point in shape.pointList:
				f.write("%s" % point.x )
				f.write(' ')
				f.write("%s" % point.y )
				f.write(' ')
				f.write("%s\n" % point.borderId )

		f.close()
