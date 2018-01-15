#!/usr/bin/python
# -*- coding: utf-8 -*-
from Geometry import Point
from Geometry import Line
from Geometry import Shape
from Mat import Mat2
from MapLoader import MapLoader
from Vector import Vec2

import sys
import random
import math
import time
import copy


#
class Map:

    sweepAngle = 0
    sweepOffset = 0
    calcDone = 0

    extremePoints = []
    boundingBox = []
    centerPoint = Point(0, 0)
    sweepLines = []
    collisionGroups = []
    collisionPairs = []

    outerBorder = Shape()
    innerBorders = []
    mLoader = MapLoader()

    #
    def __init__(self, sweepOffset):
        self.sweepAngle = 0
        self.sweepOffset = sweepOffset
        self.calcDone = 0
        self.collisionPointAdjustX = 5
        self.minAllowedPairDist = 15
        self.rotation = 0.0
        self.extremePoints = []
        self.boundingBox = []
        self.centerPoint = Point(0, 0)
        self.sweepLines = []
        self.collisionGroups = []
        self.collisionPairs = []

        self.innerBorders = []
        self.outerBorder = Shape()
        self.mowerPoint = None
        self.stationPoint = None
        self.mLoader = MapLoader()

    #
    def FindExtremePoints(self):
        mostNorth = self.outerBorder.pointList[0]
        for point in self.outerBorder.pointList:
            if mostNorth.y > point.y:
                mostNorth = point

        mostSouth = self.outerBorder.pointList[0]
        for point in self.outerBorder.pointList:
            if mostSouth.y < point.y:
                mostSouth = point

        mostEast = self.outerBorder.pointList[0]
        for point in self.outerBorder.pointList:
            if mostEast.x < point.x:
                mostEast = point

        mostWest = self.outerBorder.pointList[0]
        for point in self.outerBorder.pointList:
            if mostWest.x > point.x:
                mostWest = point

        mostNorth.y -=0
        mostSouth.y +=0
        mostEast.x +=0
        mostWest.x -=0

        self.extremePoints = []
        self.extremePoints.append(mostNorth)
        self.extremePoints.append(mostSouth)
        self.extremePoints.append(mostEast)
        self.extremePoints.append(mostWest)

        print 'Positions relative window: '
        print ('mostNorth', self.extremePoints[0].x,
               self.extremePoints[0].y)
        print ('mostSouth', self.extremePoints[1].x,
               self.extremePoints[1].y)
        print ('mostEast', self.extremePoints[2].x,
               self.extremePoints[2].y)
        print ('mostWest', self.extremePoints[3].x,
               self.extremePoints[3].y)

    #
    def CreateBoundingBox(self):
        self.boundingBox = []
        self.boundingBox.append(Point(0, 0))
        self.boundingBox.append(Point(0, 0))
        self.boundingBox.append(Point(0, 0))
        self.boundingBox.append(Point(0, 0))

        self.boundingBox[0].y = self.extremePoints[0].y  # most north
        self.boundingBox[0].x = self.extremePoints[3].x  # most west

        self.boundingBox[1].y = self.extremePoints[0].y  # most north
        self.boundingBox[1].x = self.extremePoints[2].x  # most east

        self.boundingBox[2].y = self.extremePoints[1].y  # most south
        self.boundingBox[2].x = self.extremePoints[2].x  # most east

        self.boundingBox[3].y = self.extremePoints[1].y  # most south
        self.boundingBox[3].x = self.extremePoints[3].x  # most west

    #
    def LineSweep(self):
        self.sweepLines = []
        self.collisionGroups = []

        distX = self.boundingBox[0].DistToPoint(self.boundingBox[1].x, self.boundingBox[1].y)
        distY = self.boundingBox[0].DistToPoint(self.boundingBox[3].x, self.boundingBox[3].y)
        print ('Distance X:', distX)
        print ('Distance Y:', distY)

        if self.sweepAngle == 0 or self.sweepAngle == 180:

            # traverse down on y-axis
            y = 0
            count = 0
            trigger = self.sweepOffset
            while True:
                if y >= distY:
                    break

                # "Fire line ray"
                if y >= trigger:
                    p1 = Point(self.boundingBox[0].x, self.boundingBox[0].y + y)
                    p2 = Point(self.boundingBox[0].x + distX, self.boundingBox[0].y + y)
                    l = Line(p1, p2)

                    collisionsOnSameLine = []
                    # check line intersections and collect intersect points from lawn boundarys
                    for line in self.outerBorder.lineList:
                        point = l.GetIntersectionPoint(line)
                        if point:
                            collisionsOnSameLine.append( point )

                    # check collision with obstacles
                    if len(self.innerBorders) > 0:
                        for shape in self.innerBorders:
                            # check line intersections and collect intersect points from lawn boundarys
                            for line in shape.lineList:
                                point = l.GetIntersectionPoint(line)
                                if point :
                                        collisionsOnSameLine.append(point)
                                        #prevPoint = point

                    self.SortPoints( collisionsOnSameLine )
                    self.VertexPointAdjust( collisionsOnSameLine )

                    #
                    if len(collisionsOnSameLine) % 2 != 0:
                        print("Error! odd number of collisions on line!")
                        print ("num collisions on this line", len(collisionsOnSameLine) )
                        for point in collisionsOnSameLine:
                            print point.x

                    if len(collisionsOnSameLine) > 0:
                    	self.collisionGroups.append(collisionsOnSameLine)

                    trigger += self.sweepOffset
                    count += 1
                    self.sweepLines.append(l)
                y += 1

            count = 0
            for points in self.collisionGroups:
                for point in points:
                    count +=1

            print ("Number of collision points: ", count)
            return

    # Sorts the points in a list from left closest to the y-axis line
    def SortPoints( self, inPoints ):
        i = 0
        sortedPoints = []
        points = copy.deepcopy( inPoints )
        while True:
            if len( points ) == 0:
                break

            j = 1
            # x = 0 but y on the same y as the point
            newDist = points[0].DistToPoint( 0, points[0].y )
            dist = 0
            currPoint = points[0]
            while True:
                if j >= len( points ):
                    index = points.index( currPoint )
                    sortedPoints.append( points.pop(index) )
                    #print ("saved new Dist:", newDist)
                    break

                dist = points[j].DistToPoint( 0, points[j].y )
                if newDist > dist:
                    newDist = dist
                    currPoint = points[j]
                j += 1
            i += 1
        points = sortedPoints


    # Sorts the collision points on the same line from left closest to y-axis
    def SortCollisionPoints(self):
        i = 0
        while True:
            if i >= len(self.collisionGroups):
                break
            j = 0
            points = self.collisionGroups[i]
            sortedPoints = []
            while True:
                if len(points) == 0:
                    break

                k = 1
                # x = 0 but y on the same y as the point
                newDist = points[0].DistToPoint(0, points[0].y)

                dist = 0
                currPoint = points[0]
                while True:

                    if k >= len(points):
                        index = points.index( currPoint)
                        sortedPoints.append(points.pop(index))
                        #print ("saved new Dist:", newDist)
                        break

                    dist = points[k].DistToPoint(0, points[k].y)
                    if newDist > dist:
                        newDist = dist
                        currPoint = points[k]
                    k += 1
                j += 1
            self.collisionGroups[i] = sortedPoints
            i += 1
    #
    def SplitVertexAndGetCenterPoint(self, p1, p2):
    	l1 = p1.intersectingLine
    	l2 = p2.intersectingLine

    	yDirection1 = None
    	yDirection2 = None

    	pEnd1 = p1.intersectingLine.p1
    	if pEnd1.x == p1.x and pEnd1.y == p1.y:
    		pEnd1 = p1.intersectingLine.p2

    	pEnd2 = p2.intersectingLine.p1
    	if pEnd2.x == p2.x and pEnd2.y == p2.y:
    		pEnd2 = p2.intersectingLine.p2

    	print ("pEnd1:", pEnd1.x, pEnd1.y)
    	print ("pEnd2:", pEnd2.x, pEnd2.y)

    	if p1.y > pEnd1.y:
    		yDirection1 = -1
    	elif p1.y < pEnd1.y:
    		yDirection1 = 1
    	elif p1.y == pEnd1.y:
    		print "WARNING! p1 vertex y values the same"

    		return p1

    	if p2.y > pEnd2.y:
    		yDirection2 = -1
    	elif p2.y < pEnd2.y:
    		yDirection2 = 1

    	if p2.y == pEnd2.y:
    		print "WARNING! p2 vertex y values the same"

    	if yDirection1 == yDirection2:
    		return None

    	return p1

    #
    def VertexPointAdjust( self, inPoints ):
        if len(inPoints) <= 0:
            return
        #print "BEGIN VERTEX ADJUST"
        i = 0
        while True:
            if i >= len(inPoints):
                break
            currPoint = inPoints[i]
            j = i + 1
            while True:
                if j >= len(inPoints):
                    break
                if currPoint.x == inPoints[j].x and currPoint.y == inPoints[j].y:
                    print "Vertex Found"
                    print ( currPoint.x, inPoints[j].x )
                    if self.SplitVertexAndGetCenterPoint( currPoint, inPoints[j] ):
                    	print "removing 1 points"
                    	inPoints.pop(j)
                    	j-=1
                    else:
                    	print "removing 2 points"
                    	inPoints.pop(j)
                    	inPoints.pop(i)
                    	j-=1
                    	i-=1
                j+=1
            i+=1

    #
    def RemoveClosePairs( self, shapeList, minAllowedDist ):
        # remove pairs that are to close to each other. Set distance to max mower width
        for points in shapeList:

            i = 0
            while True:
                if i >= len(self.collisionGroups):
                    break

                j = 0
                points = self.collisionGroups[i]
                while True:
                    if j >= len(points):
                        break

                    dist = points[j].DistToPoint(points[j+1].x, points[j+1].y)
                    if dist < minAllowedDist:
                        points.pop(j+1)
                        points.pop(j)
                        j-=2

                    j+=2
                i+=1

    #
    def PairAndAdjustCollisionPoints(self):
        if len(self.collisionGroups) <= 0:
            return

        self.collisionPairs = []
        newId = 1
        for points in self.collisionGroups:
            i = 0
            while True:
                if i >= len(points):
                    break

                #pair and adjust collision points on x-axis
                points[i].id = newId
                points[i].x += self.collisionPointAdjustX
                points[i + 1].id = newId
                points[i + 1].x -= self.collisionPointAdjustX

                self.collisionPairs.append(points[i])
                self.collisionPairs.append(points[i + 1])
                newId += 1
                i += 2

        print ("Number of Pair Id's: ", newId - 1)
        print ("First Pair id: ", 1)
        print ("Last Pair id: ",  newId )

    #
    def ScaleBorder( self, pList, k ):
        length = len(pList)

        if length > 0:
            i = 0
            while True:
                if i >= length:
                    break
                mat2 = Mat2()
                pList[i] = mat2.Scale(pList[i], k)
                i += 1

    #
    def RotateBorder( self, pList, degree ):
        length = len(pList)

        if length > 0:
            i = 0
            while True:
                if i >= length:
                    break
                mat2 = Mat2()
                pList[i] = mat2.Rotate( pList[i], degree )
                i += 1

    #
    def TranslateBorder( self, pList, dst ):
        length = len(pList)

        if length > 0:
            i = 0
            while True:
                if i >= length:
                    break
                mat2 = Mat2()
                pList[i] = mat2.Translate(pList[i], dst )
                i += 1

    #
    def Calculate(self):
    	print "Begin Map Calculation!......................"
        if len(self.outerBorder.pointList) <= 0:
            return


        #
        self.centerPoint.y = 400 * -1
        self.centerPoint.x = 400 * -1

        self.TranslateBorder( self.outerBorder.pointList, self.centerPoint  )
        self.RotateBorder( self.outerBorder.pointList, self.rotation )
        #self.ScaleBorder( self.outerBorder.pointList, 5 )

        #
        self.centerPoint.y = 400 * 1
        self.centerPoint.x = 400 * 1

        self.TranslateBorder( self.outerBorder.pointList, self.centerPoint  )

        self.FindExtremePoints()
        self.CreateBoundingBox()
        self.LineSweep()
        self.SortCollisionPoints()
        minAllowedDist = self.minAllowedPairDist * 3
        self.RemoveClosePairs( self.collisionGroups, minAllowedDist )
        self.PairAndAdjustCollisionPoints()

        #
        self.centerPoint.y = 400 * -1
        self.centerPoint.x = 400 * -1

        self.TranslateBorder( self.outerBorder.pointList, self.centerPoint  )
        self.TranslateBorder( self.collisionPairs, self.centerPoint  )
        self.RotateBorder( self.outerBorder.pointList, 360 - self.rotation )
        self.RotateBorder( self.collisionPairs, 360 - self.rotation )

        #self.ScaleBorder( self.outerBorder.pointList, 1.052631579 )
        #
        self.centerPoint.y = 400 * 1
        self.centerPoint.x = 400 * 1

        self.TranslateBorder( self.outerBorder.pointList, self.centerPoint  )
        self.TranslateBorder( self.collisionPairs, self.centerPoint  )
        #self.CreateBoundingBox()

        self.calcDone = 1
        print "Map Calculation......................Complete!"

    #
    def LoadMap(self):
        self.mLoader.LoadMap()
        self.outerBorder    = []
        self.innerBorders   = []
        self.outerBorder    = self.mLoader.shape
        self.innerBorders   = self.mLoader.shapes
        self.mowerPoint     = self.mLoader.mowerP
        self.stationPoint   = self.mLoader.stationP
    #
    def SaveMap(self, mower=None, station=None):
        if mower and station:
            self.mLoader.SaveMap(self.outerBorder, self.innerBorders, mower, station)
        elif mower:
            self.mLoader.SaveMap(self.outerBorder, self.innerBorders, mower)
        elif station:
            self.mLoader.SaveMap(self.outerBorder, self.innerBorders, None, station)
        else:
            self.mLoader.SaveMap(self.outerBorder, self.innerBorders)

    #
    def Reset(self):
        self.sweepAngle = 0
        self.calcDone = 0

        self.lawnExtremePoints = []
        self.boundingBox = []
        self.sweepLines = []
        self.collisionPoints = []
        self.collisionPairs = []
        self.innerBorders = []
        self.outerBorder = Shape()
        self.mowerPoint = None
        self.stationPoint = None
