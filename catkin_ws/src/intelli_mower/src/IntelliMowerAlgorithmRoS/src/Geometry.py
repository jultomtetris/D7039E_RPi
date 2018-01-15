import math

class Point():
	id = 0
	borderId = 0

	def __init__( self, x, y ):
		self.x = x
		self.y = y
		self.id = 0
		self.borderId = 0
		self.intersectingLine = None

	def DistToPoint( self, x ,y ):
		return math.sqrt(math.pow( (self.x - x), 2 ) + math.pow( (self.y - y), 2) )

class Line():
    def __init__( self, p1, p2 ):
        self.p1 = p1
        self.p2 = p2
        #self.angle = self.Angle() * ( 180 / math.pi ) * (-1)
        #self.angleRad = math.sqrt( ( self.Angle() * self.Angle() ) )

    def Angle(self):
    	x1 = self.p1.x
    	y1 = self.p1.y
    	x2 = self.p2.x
    	y2 = self.p2.y
    	inner_product = x1*x2 + y1*y2
    	len1 = math.hypot(x1, y1)
    	len2 = math.hypot(x2, y2)
    	if len1 == 0:
    		len1 = 0.001
    	if len2 == 0:
    		len2 = 0.001
    	return math.acos(inner_product/( len1 * len2 ) )

    def Length(self):
        return p1.DistToPoint(p1.x, p1.y)

    #
    def GetIntersectionPoint( self, l2 ):
        p0_x = self.p1.x
        p0_y = self.p1.y
        p1_x = self.p2.x
        p1_y = self.p2.y
        p2_x = l2.p1.x
        p2_y = l2.p1.y
        p3_x = l2.p2.x
        p3_y = l2.p2.y

        s1_x = p1_x - p0_x
        s1_y = p1_y - p0_y
        s2_x = p3_x - p2_x
        s2_y = p3_y - p2_y

        den = (-s2_x * s1_y + s1_x * s2_y)

        if den == 0:
        	#return None
        	den = 0.0000001

        s = (-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)) / den
        t = ( s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)) / den

        if s >= 0 and s <= 1 and t >= 0 and t <= 1:
            # Collision detected
            i_x = p0_x + (t * s1_x)
            i_y = p0_y + (t * s1_y)

            p = Point(i_x, i_y)
            p.intersectingLine = l2
            return p
        return None # No collision

class Shape():
    pointList = []
    lineList = []
    id = 0

    def __init__(self):
        self.pointList = []
        self.lineList = []
        self.id = 0

    def AddBorderPoint(self, p=Point(0, 0)):
        #
        self.pointList.append(p)
        #
        if len(self.pointList) == 2:
            newLine = Line(self.pointList[0], self.pointList[1])
            self.lineList.append(newLine)

        #
        if len(self.pointList) > 2:
            # delete closing line
            if len(self.pointList) >= 4:
                self.lineList.pop(-1)
            #
            currPoint = self.pointList[len(self.pointList) - 1]
            prevPoint = self.pointList[len(self.pointList) - 2]

            newLine = Line(currPoint, prevPoint)
            self.lineList.append(newLine)
            #
            closingLine = Line(currPoint, self.pointList[0])
            self.lineList.append(closingLine)

        # print (len(self.lineList))
