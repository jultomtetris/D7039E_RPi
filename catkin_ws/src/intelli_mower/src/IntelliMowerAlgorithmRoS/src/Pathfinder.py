#!/usr/bin/python
# -*- coding: utf-8 -*-

from Geometry import Point
from Geometry import Line
from Geometry import Shape
import copy

class Pathfinder:
    isInitialized = 0
    bPThresh = 0
    iPThresh = 0
    distToPairThresh = 0
    currentPos = Point(0, 0)
    distToNextPos = 0
    pathState = 0
    copyPairs = []
    undetectedPaths = []
    innerBorders = []
    outerBorder = Shape()
    collisionPairs = []
    pathList = []

    def __init__(self):
        self.bPThresh = 1  # border point threshhold
        self.iPThresh = 0.5
        self.fDThresh = 400  # free destination distance threshold
        self.distToPairThresh = 0  # distance to pair threshold
        self.isInitialized = 0
        self.pathingComplete = 0
        self.currentPos = Point(0, 0)
        self.currentStationPos = None
        self.distToNextPos = 0
        self.pathState = 0
        self.copyPairs = []
        self.undetectedPaths = []
        self.numPairPoints = 0
        self.innerBorders = []
        self.outerBorder = Shape()
        self.collisionPairs = []
        self.pathList = []
        self.decreasingSide = []
        self.increasingSide = []

    #
    def Init( self, outerBorder, innerBorders, collisionPairs ):
        self.outerBorder = copy.deepcopy(outerBorder)
        self.innerBorders = copy.deepcopy(innerBorders)
        self.undetectedPaths = copy.deepcopy(collisionPairs)
        self.numPairPoints = len(self.undetectedPaths)
        self.isInitialized = 1

    # NOTE! is only called from IntelliMower object to set an initial position!
    def UpdatePos(self, x, y):
        p = Point(x, y)
        self.currentPos = p
        self.pathList = []
        self.pathList.append(p)

    def UpdateStationPos(self, x, y):
        p = Point(x, y)
        p.id = "ChargingStation"
        self.currentStationPos = p

    # find closest point in a given list to a given point
    def ClosestPoint(self, pList, p):
        i = 0
        closestIndex = 0
        currDist = 0
        #select a current distance not equal to zero distance
        while i < len(pList):
            currDist = p.DistToPoint(pList[i].x, pList[i].y)
            if pList[i].x != p.x or pList[i].y != p.y:
                closestIndex = i
                break
            i += 1

        i = closestIndex + 1
        while i < len( pList ):
            nextDist = p.DistToPoint(pList[i].x, pList[i].y)
            if currDist > nextDist:
                currDist = nextDist

                closestIndex = i
            i += 1

        return pList[closestIndex]

    #
    def ClosestPointFromAllLists(self, pos ):
        closestPoints = []

        if len(self.undetectedPaths):
            closestPoints.append( self.ClosestPoint(self.undetectedPaths, pos) )
        if len(self.decreasingSide):
            closestPoints.append( self.ClosestPoint(self.decreasingSide, pos) )
        if len(self.increasingSide):
            closestPoints.append( self.ClosestPoint(self.increasingSide, pos) )

        i = 1
        clsIndex = 0
        dist = pos.DistToPoint( closestPoints[0].x, closestPoints[0].y )
        while i < len(closestPoints):
            newDist = pos.DistToPoint( closestPoints[i].x, closestPoints[i].y )
            if dist >= newDist:
                dist = newDist
                clsIndex = i
            i += 1
        return closestPoints[clsIndex]

    #
    def PairPoint(self, points, point):
        for p in points:
            if point.id == p.id:
                return p
        print 'ERROR! in function PairPoint: No pair point found!'

    #
    def ClosestIntersectionPointToDst( self, p1, p2 ):
        line = Line(p1, p2)
        intersectionPointList = []
        # check intersecting outer borders on line to closest pair point
        for l in self.outerBorder.lineList:
            p = line.GetIntersectionPoint(l)
            if p:
                # print 'Found OB intersection!'
                intersectionPointList.append(p)

        # check intersecting inner borders on line to closest pair point
        for shape in self.innerBorders:
            for l in shape.lineList:
                p = line.GetIntersectionPoint(l)
                if p:
                    # print 'Found IB intersection!'
                    # print p.borderId
                    intersectionPointList.append(p)
        # if any intersections found return the closest
        if len(intersectionPointList) > 0:
            # print 'Returning Closest Intersection point!'
            return self.ClosestPoint(intersectionPointList, p2)
        else:
            return None

    #
    def ClosestIntersectionPointOnBorder( self, p1, p2, border ):
        line = Line(p1, p2)
        intersectionPointList = []
        # check intersecting outer borders on line to closest pair point
        if border == 0:
            for l in self.outerBorder.lineList:
                p = line.GetIntersectionPoint(l)
                if p:
                    # print 'Found OB intersection!'
                    intersectionPointList.append(p)
        elif border > 0:
            # check intersecting inner borders on line to closest pair point
            shape = self.innerBorders[border - 1]
            for l in shape.lineList:
                p = line.GetIntersectionPoint(l)
                if p:
                    #print 'Found IB intersection!'
                    #print p.intersectingLine.p1.borderId
                    intersectionPointList.append(p)

        # if any intersections found return the closest
        if len(intersectionPointList) > 0:
            # print 'Returning Closest Intersection point!'
            return self.ClosestPoint(intersectionPointList, p2)
        else:
            return None

    #
    def ClosestIntersectionPoint( self, p1, p2 ):
        line = Line(p2, p1)
        intersectionPointList = []
        # check intersecting outer borders on line to closest pair point
        for l in self.outerBorder.lineList:
            p = line.GetIntersectionPoint(l)
            if p:
                # print 'Found OB intersection!'
                intersectionPointList.append( p )
        # check intersecting inner borders on line to closest pair point
        for shape in self.innerBorders:
            for l in shape.lineList:
                p = line.GetIntersectionPoint( l )
                if p:
                    #print 'Found IB intersection!'
                    #print p.intersectingLine.p1.borderId
                    intersectionPointList.append( p )

        # if any intersections found return the closest
        if len(intersectionPointList) > 0:
            # print 'Returning Closest Intersection point!'
            return self.ClosestPoint( intersectionPointList, p1 )
        else:
            return None

    # if we are standing on a border choose a intersection point not on this border
    def AltClosestIntersectionPoint( self, p1, p2 ):
        border = p1.borderId
        print "AltClosestIntersectionPoint"
        #print ("BorderId:", border)
        line = Line( p2, p1 )
        intersectionPointList = []
        # check intersecting outer borders on line to closest pair point
        for l in self.outerBorder.lineList:
            p = line.GetIntersectionPoint( l )
            if p and p.intersectingLine.p1.borderId != border:
                # print 'Found OB intersection!'
                intersectionPointList.append( p )
        # check intersecting inner borders on line to closest pair point
        for shape in self.innerBorders:
            for l in shape.lineList:
                p = line.GetIntersectionPoint( l )
                if p and p.intersectingLine.p1.borderId != border:
                    #print 'Found IB intersection!'
                    #print ("intersection has border Id:", p.intersectingLine.p1.borderId )
                    intersectionPointList.append( p )

        # if any intersections found return the closest
        if len(intersectionPointList) > 0:
            # print 'Returning Closest Intersection point!'
            return self.ClosestPoint( intersectionPointList, p1 )
        else:
            return None

    # Note this is bugged because of mirroring probably
    # Fixme! this function should be rewritten to fix the mirroring problem
    def ClosestPointWithLoS( self, points, currentPos ):
        if len(points) < 1:
            # print "List is empty"
            return None

        pointsCopy = copy.deepcopy(points)

        while len(pointsCopy) > 0:
            closestPos = self.ClosestPoint(pointsCopy, currentPos)
            intersectionP = self.ClosestIntersectionPoint( currentPos, closestPos )

            if intersectionP == None:
                return closestPos
            # if intersection point and closest point on line is the same we do have free LoS
            elif intersectionP.x == closestPos.x and intersectionP.y == closestPos.y:
                return closestPos
            elif intersectionP.x == currentPos.x and intersectionP.y == currentPos.y:
                interP = self.ClosestIntersectionPointToDst( currentPos, closestPos )
                if interP.x == currentPos.x and interP.y == currentPos.y:
                    print 'Warning in ClosestPointWithLoS: standing on intersection point!'
                    return closestPos

            pointsCopy.pop( pointsCopy.index(closestPos) )

        print "Error in ClosestPointWithLoS: No closest point with LoS found"
        return None

    #
    def DeletePointInList(self, points, p ):
        i = 0
        while i < len(points):
            if points[i].x == p.x and points[i].y == p.y:
                points.pop(i)
                i -= 1
            i += 1

    #
    def CalculateVisiblePaths( self, points, incSide, decSide, currPos, num ):
        # we are not standing on a pair point try to go to closest visible
        if currPos.id == 0:
            print 'Warning CalculateVisiblePaths: Not standing on pair point!'
            return

        # split up the mow lines in two lists depending
        # on which side of the mower they are on
        i = 0
        while i < num and len(points) > 0:
            closestPos = self.ClosestPointWithLoS(points, currPos)
            if closestPos == None:
                i += 1
                continue
            elif closestPos.id < currPos.id:
                decSide.append(closestPos)
                self.DeletePointInList(points, closestPos)
                pairPoint = self.PairPoint(points, closestPos)
                decSide.append(pairPoint)
                self.DeletePointInList(points, pairPoint)
            elif closestPos.id > currPos.id:
                incSide.append(closestPos)
                self.DeletePointInList(points, closestPos)
                pairPoint = self.PairPoint(points, closestPos)
                incSide.append(pairPoint)
                self.DeletePointInList(points, pairPoint)
            i += 1

    #
    def PickActiveSide( self, increasingSide, decreasingSide, currentPos ):

        # pick the closest mow line for which there exist the smallest
        # number of lines to mow on that side of the mower
        if len(increasingSide) == 0 and len(decreasingSide) == 0:
            print "Error! Can't pick active side both sides are empty"
            return None
        elif len(increasingSide) == 0:
            return decreasingSide
        elif len(decreasingSide) == 0:
            return increasingSide
        else:

            incClosest = self.ClosestPointWithLoS(increasingSide,
                    currentPos)
            decClosest = self.ClosestPointWithLoS(decreasingSide,
                    currentPos)

            if incClosest:
                incDist = currentPos.DistToPoint(incClosest.x,
                        incClosest.y)
            else:
                return decreasingSide

            if decClosest:
                decDist = currentPos.DistToPoint(decClosest.x,
                        decClosest.y)
            else:
                return increasingSide

            if incDist < decDist:
                return increasingSide
            else:
                return decreasingSide

    #
    def GetBorderPath( self, borderList, startP, endP):
        if len(borderList) <= 0:
            print 'Error borderList is empty!'
            return
        if borderList[0].borderId != startP.intersectingLine.p1.borderId \
            and borderList[0].borderId != endP.intersectingLine.p1.borderId:
            print 'Error border id mismatch!'
            return
        if startP.intersectingLine.p1.borderId != endP.intersectingLine.p1.borderId:
            print 'Error border Id startP and endP not the same!'
            return

        # start point vertices
        bp1 = startP.intersectingLine.p1
        bp2 = startP.intersectingLine.p2

        # end point vertices
        ebp1 = endP.intersectingLine.p1
        ebp2 = endP.intersectingLine.p2

        # positive traverse
        pTL1 = []
        pTL2 = []
        shortestPTL = []
        i = borderList.index(bp1)
        j = borderList.index(bp2)
        count = 0
        print ("bp1 index:", i )
        print ("bp2 index:", j )
        while True:
            # print "hej"
            pTL1.append(borderList[i])
            pTL2.append(borderList[j])
            if borderList[i].x == ebp1.x and borderList[i].y == ebp1.y \
                or borderList[i].x == ebp2.x and borderList[i].y == ebp2.y:
                shortestPTL = pTL1
                break
            if borderList[j].x == ebp1.x and borderList[j].y == ebp1.y \
                or borderList[j].x == ebp2.x and borderList[j].y == ebp2.y:
                shortestPTL = pTL2
                break

            i += 1
            j += 1
            count += 1
            if i == len(borderList):  # if we overflow set the index to the beginning of list
                i = 0
            if j == len(borderList):
                j = 0

            # if we count over one length of border without founding a free LoS we have to jump to next obstacle
            if count == len(borderList):
                break

        # negative traverse
        nTL1 = []
        nTL2 = []
        shortestNTL = []
        j = borderList.index(bp1)
        i = borderList.index(bp2)
        count = 0
        while True:
            nTL1.append(borderList[i])
            nTL2.append(borderList[j])
            if borderList[i].x == ebp1.x and borderList[i].y == ebp1.y \
                or borderList[i].x == ebp2.x and borderList[i].y \
                == ebp2.y:
                shortestNTL = nTL1
                break
            if borderList[i].x == ebp1.x and borderList[i].y == ebp1.y \
                or borderList[i].x == ebp2.x and borderList[i].y \
                == ebp2.y:
                shortestNTL = nTL2
                break
            i -= 1
            j -= 1
            count += 1
            if i == 0:  # if we overflow set the index to the end of list
                i = len(borderList) - 1
            if j == 0:
                j = len(borderList) - 1

            #if we count over one length of border without founding a free LoS we have to jump to next obstacle
            if count == len(borderList):
                break

        if len(shortestNTL) < 1 and len(shortestPTL) < 1:
            print 'Error border lists are faulty'
            return None
        elif len(shortestNTL) < 1:
            return shortestPTL
        elif len(shortestPTL) < 1:
            return shortestNTL
        elif len(shortestPTL) > len(shortestNTL):
            return shortestNTL
        elif len(shortestPTL) < len(shortestNTL):
            return shortestPTL
        elif len(shortestPTL) == len(shortestNTL):
            print 'Both border paths are the same lenght!'
            print ('shortestPTL:', len(shortestPTL))
            print ('shortestNTL:', len(shortestNTL))
            return shortestPTL

    #
    def MowBorderPath( self, borderList, startP ):
        if len(borderList) <= 0:
            print 'Error borderList is empty!'
            return
        if borderList[0].borderId != startP.borderId:
            print 'Error border id mismatch!'
            return

        pList = []
        i = 0
        count = -1
        while i < len( borderList ):
            if borderList[i].x == startP.x and borderList[i].y == startP.y:
                print ( "Found start P index i: ", i )
                break
            i += 1

        while True:
            # print "hej"
            pList.append(borderList[i])

            if count > 0 and borderList[i].x == startP.x and borderList[i].y == startP.y:
                break

            i += 1
            count += 1
            if i == len( borderList ):  # if we overflow set the index to the beginning of list
                i = 0
            # if we count over one length of border without founding a free LoS we have to jump to next obstacle
            if count == len( borderList ):
                break

        if len( pList ) < 1:
            print 'Error border lists are faulty'
            return None

        return pList

    # follows border until we get free LoS to a pair
    # point or to the next border intersection point
    def TraverseBorder( self, startP, endP ):

        # print ("startP:", startP.x, startP.y )
        # print ("endP:", endP.x, endP.y )
        # print ("startP border id:", startP.intersectingLine.p1.borderId )
        # print ("endP border id:", endP.intersectingLine.p1.borderId )

        traversedPath = []
        if startP.intersectingLine.p1.borderId == 0:
            print 'Following lawn border!'
            traversedPath = self.GetBorderPath( self.outerBorder.pointList, startP, endP )
        elif startP.intersectingLine.p1.borderId > 0:
            print 'Following obstacle border!'
            traversedPath = self.GetBorderPath( self.innerBorders[ startP.intersectingLine.p1.borderId - 1 ].pointList, startP, endP )

        completedPath = []
        completedPath.append(startP)  # we add start intersection point to pathList first before inserting the planned border paths
        i = 0

        # we check if we see any free LoS points on the way to end point
        while i < len( traversedPath ):

            # print "Num undetected points left:", len( self.undetectedPaths )
            # print "Num points in ActiveSide:", len( pairPoints )
            p = traversedPath[i]
            completedPath.append(p)

            p.x += 4
            undetectedPos = self.ClosestPointWithLoS( self.undetectedPaths, p )
            incPos = self.ClosestPointWithLoS( self.increasingSide, p )
            decPos = self.ClosestPointWithLoS( self.decreasingSide, p )
            if undetectedPos:
                print 'Found closer undetected point!'
                completedPath.append(undetectedPos)
                self.DeletePointInList(self.undetectedPaths,
                        undetectedPos)
                break
            elif incPos:
                print 'Found closer LoS point!'
                completedPath.append(incPos)
                self.DeletePointInList(self.increasingSide, incPos)
                break
            elif decPos:
                print 'Found closer LoS point!'
                completedPath.append(decPos)
                self.DeletePointInList(self.decreasingSide, decPos)
                break

            p.x -= 4 * 2
            undetectedPos = self.ClosestPointWithLoS(self.undetectedPaths, p)
            incPos = self.ClosestPointWithLoS(self.increasingSide, p)
            decPos = self.ClosestPointWithLoS(self.decreasingSide, p)
            if undetectedPos:
                print 'Found closer undetected point!'
                completedPath.append(undetectedPos)
                self.DeletePointInList(self.undetectedPaths,
                        undetectedPos)
                break
            elif incPos:
                print 'Found closer LoS point!'
                completedPath.append(incPos)
                self.DeletePointInList(self.increasingSide, incPos)
                break
            elif decPos:
                print 'Found closer LoS point!'
                completedPath.append(decPos)
                self.DeletePointInList(self.decreasingSide, decPos)
                break

            p.x += 4
            i += 1

        i = 0
        while i < len(completedPath):
            self.GoTo(completedPath[i])
            i += 1

    #
    def GoTo( self, p ):
        self.currentPos = p
        if p.id:  # if route pair id update pair id and turn on path state 1
            print ("p id: " , p.id)
            self.pathState = 1
            print "Path State set to 1"

        self.pathList.append( p )

    #
    def GoToNextPair(self):
        # find next route pair and set it to next position
        for point in self.increasingSide:
            if self.currentPos.id == point.id:

                # insert planned next position
                self.currentPos = point
                self.pathList.append(point)

                # remove traveled position
                self.increasingSide.pop(self.increasingSide.index(point))
                return

        for point in self.decreasingSide:
            if self.currentPos.id == point.id:

                # insert planned next position
                self.currentPos = point
                self.pathList.append(point)

                # remove traveled position
                self.decreasingSide.pop(self.decreasingSide.index(point))
                return

        for point in self.undetectedPaths:
            if self.currentPos.id == point.id:

                # insert planned next position
                self.currentPos = point
                self.pathList.append(point)

                # remove traveled position
                self.undetectedPaths.pop(self.undetectedPaths.index(point))
                return

        print 'ERROR! No pair point found!'

    #
    def GoToClosestPairPoint( self ):
        print 'Moving to closest pair point!'
        pos = self.ClosestPointWithLoS( self.undetectedPaths, self.currentPos )
        if pos == None:
            print "Can't move to closest pair point none visible! FIXME! Check if we are standing on a border point!"
            if len( self.undetectedPaths ) or len( self.increasingSide ) or len( self.decreasingSide ):
                # we get closest pair point
                closestP = self.ClosestPointFromAllLists( self.currentPos )
                # we set the closest intersection point
                startP = self.AltClosestIntersectionPoint( self.currentPos, closestP )
                #we set the last intersection point on the obstacle border we wish to traverse
                endP = self.ClosestIntersectionPointOnBorder( startP, closestP, startP.intersectingLine.p1.borderId )
                # start traverse
                self.TraverseBorder( startP, endP )
                #self.pathState = 0
            # check if we are standing on a border line
            return

        self.GoTo(pos)
        self.DeletePointInList( self.undetectedPaths, pos)
        self.pathState = 1

    #
    def GoToNextPath( self, increasingSide, decreasingSide, currentPos ):
        activeSide = self.PickActiveSide( increasingSide, decreasingSide, currentPos )
        # we are not standing on a pair point try to go to closest visible
        if activeSide == None:
            if len(self.undetectedPaths) != 0:
                print 'no visible pairs available and inc and dec lists are empty. Following border to closest undected pair point! FIXME'
                # try checking for close visible path's
                print 'Looking for closer visible paths'
                self.CalculateVisiblePaths(self.undetectedPaths,
                        self.increasingSide, self.decreasingSide,
                        self.currentPos, 1)
                activeSide = self.PickActiveSide(increasingSide,
                        decreasingSide, currentPos)
                print 'Updated points in decreasing side memory: ', \
                    len(self.decreasingSide)
                print 'Updated points in increasing side memory: ', \
                    len(self.increasingSide)
                print 'Num undetected points left:', \
                    len(self.undetectedPaths)
                pos = None
                if activeSide:
                    pos = self.ClosestPointWithLoS( activeSide, currentPos )

                # we did not find any close visible paths after re calculation follow border
                if pos == None:
                    print 'No visible paths available following border to closest pair point!'
                    closestP = self.ClosestPoint( self.undetectedPaths, currentPos )
                    if closestP == None:
                        return
                    startP = self.ClosestIntersectionPoint( currentPos, closestP )
                    if startP == None:
                        return
                    endP = self.ClosestIntersectionPointOnBorder( startP, closestP, startP.intersectingLine.p1.borderId )
                    self.TraverseBorder( startP, endP )
                    return

            print 'No paths available!'
            return

        pos = self.ClosestPointWithLoS(activeSide, currentPos)
        if pos == None:
            # try checking for close visible path's
            print 'Looking for closer visible paths'
            self.CalculateVisiblePaths(self.undetectedPaths,
                    self.increasingSide, self.decreasingSide,
                    self.currentPos, 1)
            activeSide = self.PickActiveSide(increasingSide,
                    decreasingSide, currentPos)
            print 'Updated points in decreasing side memory: ', \
                len(self.decreasingSide)
            print 'Updated points in increasing side memory: ', \
                len(self.increasingSide)
            print 'Num undetected points left:', \
                len(self.undetectedPaths)
            pos = self.ClosestPointWithLoS(activeSide, currentPos)

            # we did not find any close visible paths after re calculation follow border
            if pos == None:
                print 'No visible paths available following border to closest pair point!'
                closestP = self.ClosestPoint( activeSide, currentPos )
                startP = self.ClosestIntersectionPoint( currentPos, closestP )
                endP = self.ClosestIntersectionPointOnBorder( startP, closestP, startP.intersectingLine.p1.borderId )
                self.TraverseBorder( startP, endP )
                return

        self.GoTo( pos )
        self.DeletePointInList( activeSide, pos )

    # Only mows outer border right now
    def MowBorders( self ):
        #outerBorderPoints = copy.deepcopy( self.outerBorder.pointList )
        #print len( outerBorderPoints )

        dst = self.ClosestPointWithLoS( self.outerBorder.pointList, self.currentPos )
        #self.GoTo( dst )

        tPath = self.MowBorderPath( self.outerBorder.pointList, dst )
        print len( self.outerBorder.pointList )
        print len(tPath)
        i = 0
        while i < len( tPath ):
            self.GoTo( tPath[i] )
            i += 1

        #self.GoTo( dst )
        #self.TraverseBorder( startP, startP )

        self.pathState = 2

    #
    def FindNextPath( self ):

        if self.isInitialized != 1:
            return

        if self.pathState == 3:
            print "Docked with charging station"
            self.pathingComplete = 1

        if self.pathState == 2:
            print 'Returning to Charging Station'
            if self.currentStationPos:
                self.undetectedPaths    = []
                self.increasingSide     = []
                self.decreasingSide     = []
                #self.increasingSide.append(self.currentStationPos)
                #self.decreasingSide.append(self.currentStationPos)

                self.undetectedPaths.append(self.currentStationPos)
                closestPos = self.ClosestPointWithLoS(self.undetectedPaths, self.currentPos)
                if closestPos != None:
                    self.GoTo(closestPos)
                else:
                    self.GoToNextPath( self.increasingSide, \
                                        self.decreasingSide, self.currentPos)
                self.pathState = 3
                return
            print "Couldn't go to charging station"
            self.pathingComplete = 1

        # if pos is on a pair point go to next pair point
        # we are assuming next route pair point is always visible
        if self.pathState == 0:
            if len( self.pathList ) >= self.numPairPoints \
                and len( self.undetectedPaths ) == 0 \
                and len( self.decreasingSide ) == 0 \
                and len( self.increasingSide ) == 0:
                # all routes have ben mowed cut the borders now!
                print 'Lawn route Completed time to mow borders!'
                self.MowBorders()
                self.pathState = 2
            elif self.currentPos.id == 0:
                self.GoToClosestPairPoint()

            else:
                print 'Total number of pair points: ', \
                    self.numPairPoints
                print 'Num undetected points left:', \
                    len(self.undetectedPaths)
                print 'Traversed pair points: ', len(self.pathList)
                print 'Points in decreasing side memory: ', \
                    len(self.decreasingSide)
                print 'Points in increasing side memory: ', \
                    len(self.increasingSide)

                if len(self.increasingSide) < 1 \
                    and len(self.decreasingSide) < 1:
                    self.CalculateVisiblePaths(self.undetectedPaths,
                            self.increasingSide, self.decreasingSide,
                            self.currentPos, 1)

                    print 'Calculating Visible Paths........................'
                    print 'num undetected points left:', \
                        len(self.undetectedPaths)
                    print 'Num detected decreasing Side points in memory:', \
                        len(self.decreasingSide)
                    print 'Num detected increasing side points in memory:', \
                        len(self.increasingSide)

                self.GoToNextPath(self.increasingSide,
                                  self.decreasingSide, self.currentPos)
        elif self.pathState == 1:
            #print 'Going To Next Pair Point!'
            self.GoToNextPair()
            self.pathState = 0

        return

    #
    def Reset(self):
        self.isInitialized = 0
        self.currentPos = Point(0, 0)
        self.currentStationPos = None
        self.distToNextPos = 0
        self.pathingComplete = 0
        self.pathState = 0
        self.pathList = []
        self.undetectedPaths = []
        self.innerBorders = []
        self.outerBorder = Shape()
        self.collisionPairs = []
        self.decreasingSide = []
        self.increasingSide = []
