#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, random, math, time, copy
from PyQt4 import QtGui, QtCore
from operator import itemgetter, attrgetter


    def distToPoint( self, x, y ):
        return math.sqrt(math.pow( (self.x - x), 2 ) + math.pow( (self.y - y), 2) )

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.prevLine = None
        self.nextLine = None


class Example(QtGui.QWidget):
    pointList = []
    lineList = []
    routeList = []
    mowOffset = 30
    wHeight = 800
    wWidth = 1000


    def __init__(self):
        super(Example, self).__init__()
        #self.readInputFile()
        QtGui.QWidget.__init__(self)


        self.calculateButton = QtGui.QPushButton('Calculate', self)
        self.calculateButton.clicked.connect(self.calculateHandler)

        self.randomButton = QtGui.QPushButton('Random', self)
        self.randomButton.clicked.connect(self.randomHandler)

        self.readButton = QtGui.QPushButton('Load', self)
        self.readButton.clicked.connect(self.readHandler)

        self.resetButton = QtGui.QPushButton('Reset', self)
        self.resetButton.clicked.connect(self.resetHandler)

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.calculateButton)
        layout.addWidget(self.randomButton)
        layout.addWidget(self.readButton)
        layout.addWidget(self.resetButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(layout)
        self.setLayout(vbox)

        self.initUI()


    # def calculateHandler(self):
    #
    #     leftTurnPoints = []
    #     leftLineIndex = -1
    #     rightLineIndex = 0
    #
    #     furthestDown = 0
    #
    #     for point in self.pointList:
    #         if point.y > furthestDown:
    #             furthestDown = point.y
    #
    #     for line in self.lineList:
    #         leftTurn = self.leftTurn(line.p1, line.p2, line.nextLine.p2)
    #         if leftTurn:
    #             leftTurnPoints.append(line.p2)
    #
    #
    #
    #     self.routeList.append(self.pointList[0])
    #     currentPoint = self.getMowPoint(self.lineList[0], self.mowOffset)
    #     self.routeList.append(currentPoint)
    #
    #     while currentPoint.y + self.mowOffset < furthestDown:
    #
    #         leftLineIndex = -1
    #         rightLineIndex = 0
    #         while -leftLineIndex <= len(self.lineList):
    #
    #             pivotLine = Line( Point(currentPoint.x - 1000, currentPoint.y), Point(currentPoint.x + 1000, currentPoint.y) )
    #             iPoint = self.getLineIntersection( pivotLine, self.lineList[leftLineIndex] )
    #
    #             if iPoint:
    #                 self.routeList.append( iPoint )
    #
    #                 nextPoint = self.getMowPoint( Line(iPoint, self.lineList[leftLineIndex].p1), self.mowOffset )
    #                 lastPoint = self.lineList[leftLineIndex].p1
    #
    #                 if nextPoint.y > lastPoint.y:
    #                     self.routeList.append(lastPoint)
    #                     self.mowOffset = nextPoint.y - lastPoint.y
    #                     nextPoint = self.getMowPoint( Line(lastPoint, self.lineList[leftLineIndex - 1].p1), self.mowOffset )
    #                     self.mowOffset = 30
    #
    #                 self.routeList.append(nextPoint)
    #                 currentPoint = nextPoint
    #                 break
    #
    #             leftLineIndex -= 1
    #
    #         while rightLineIndex < len(self.lineList):
    #
    #             pivotLine = Line( Point(currentPoint.x - 1000, currentPoint.y), Point(currentPoint.x + 1000, currentPoint.y) )
    #             iPoint = self.getLineIntersection( pivotLine, self.lineList[rightLineIndex] )
    #
    #
    #             if iPoint:
    #                 self.routeList.append( iPoint )
    #
    #                 nextPoint = self.getMowPoint( Line(iPoint, self.lineList[rightLineIndex].p2), self.mowOffset )
    #                 lastPoint = self.lineList[rightLineIndex].p2
    #
    #                 if nextPoint.y > lastPoint.y:
    #                     self.routeList.append(lastPoint)
    #                     mowOffset = nextPoint.y - lastPoint.y
    #                     nextPoint = self.getMowPoint( Line(lastPoint, self.lineList[rightLineIndex + 1].p2), mowOffset )
    #
    #                 self.routeList.append(nextPoint)
    #                 currentPoint = nextPoint
    #                 break
    #
    #             rightLineIndex += 1
    #
    #     QtGui.QWidget.update(self)






    # def calculateHandler(self):
    #     furthestDown = 0
    #
    #     for point in self.pointList:
    #         if point.y > furthestDown:
    #             furthestDown = point.y
    #
    #     currentLine = self.lineList[0]
    #     self.routeList.append(currentLine.p1)
    #     currentPoint = self.getMowPoint(currentLine, self.mowOffset)
    #     self.routeList.append(currentPoint)
    #     currentLine = currentLine.nextLine
    #
    #
    #     while currentPoint.y + self.mowOffset < furthestDown:
    #         pivotLine = Line( Point(currentPoint.x - 1000, currentPoint.y), Point(currentPoint.x + 1000, currentPoint.y) )
    #
    #         while True:
    #
    #             iPoint = self.getLineIntersection(pivotLine, currentLine)
    #
    #             if iPoint:
    #                 self.routeList.append( iPoint )
    #
    #
    #                 lastPoint = None
    #                 if currentLine.p1 > currentLine.p2:
    #                     lastPoint = currentLine.p1
    #                 else:
    #                     lastPoint = currentLine.p2
    #
    #
    #                 nextPoint = self.getMowPoint( Line(iPoint, lastPoint), self.mowOffset )
    #                 self.routeList.append(nextPoint)
    #                 # if math.fabs(nextPoint.y - lastPoint.y) < self.mowOffset:
    #                 #     self.routeList.append(lastPoint)
    #                 #     nextPoint = self.getMowPoint( currentLine.nextLine, math.fabs(nextPoint.y - lastPoint.y) )
    #                 #     currentLine = currentLine.nextLine
    #
    #
    #                 # self.routeList.append(nextPoint)
    #                 # currentPoint = nextPoint
    #                 currentPoint = nextPoint
    #
    #                 if currentLine.p1 > currentLine.p2:
    #                     currentLine = currentLine.prevLine
    #                 else:
    #                     currentLine = currentLine.nextLine
    #
    #                 break
    #
    #             if currentLine.p1 > currentLine.p2:
    #                 currentLine = currentLine.prevLine
    #             else:
    #                 currentLine = currentLine.nextLine
    #
    #
    #
    #
    #     QtGui.QWidget.update(self)


    def calculateHandler(self):
        currentLine = self.lineList[0]
        currentPoint = self.getMowPoint(currentLine, self.mowOffset)
        listOfIntersections = []

        lowestPoint = 0

        for point in self.pointList:
            if point.y > lowestPoint:
                lowestPoint = point.y

        listOfLeftTurns = []
        for line in self.lineList:
            leftTurn = self.leftTurn(line.p1, line.p2, line.nextLine.p2)
            if leftTurn:
                listOfLeftTurns.append(line.p2)



        n = 0
        while n * self.mowOffset < lowestPoint:
            pivotLine = Line( Point(currentPoint.x - 1000, currentPoint.y + (n * self.mowOffset)), Point(currentPoint.x + 1000, currentPoint.y + (n * self.mowOffset)) )
            tempList = []
            for line in self.lineList:
                iPoint = self.getLineIntersection(pivotLine, line)
                if iPoint:
                    tempList.append(iPoint)


            tempList.sort(key=attrgetter("x"), reverse=False)

            listOfIntersections.append(copy.deepcopy(tempList))
            n += 1

        while len(listOfIntersections) > 0:
            toggle = False
            for lst in listOfIntersections:
                if len(lst) == 0:
                    listOfIntersections.remove(lst)
                    continue
                if len(lst) == 1:
                    self.routeList.append(lst[0])
                    continue

                for line in self.lineList:
                    if self.getLineIntersection(Line(lst[0], lst[1]), line):
                        continue

                    # if count > 0 and len(listOfLeftTurns) > 0:
                    #     self.routeList.append(listOfLeftTurns.pop(0))


                self.routeList.append(lst.pop(0))
                if len(lst) > 0:
                    self.routeList.append(lst.pop(0))

                # if toggle:
                #     self.routeList.append(lst.pop(0))
                # else:
                #     self.routeList.append(lst.pop(1))
                # toggle = True if toggle == False else False


    # def calculateHandler(self):
    #     iterations = 1
    #     for line in self.lineList:
    #         angle = self.angleThreePoints(line.prevLine.p1, line.p1, line.p2) / 2
    #         x = line.p1.x
    #         y = line.p1.y
    #         self.routeList.append(Point(x + self.mowOffset * math.sin(angle), y + self.mowOffset * math.cos(angle)))





    def randomHandler(self):
        self.resetHandler()
        random.seed()
        tempList = [ ( random.randint(5, self.wWidth - 5), random.randint(5, self.wHeight - 50) ) for k in range(100) ]
        for elem in tempList:
            self.appendPoint(elem[0], elem[1])

    def resetHandler(self):
        self.pointList = []
        self.lineList = []
        self.routeList = []
        QtGui.QWidget.update(self)

    def readHandler(self):
        self.readInputFile()
        QtGui.QWidget.update(self)

    def readInputFile(self):
        self.resetHandler()
        f = open('points', 'r')
        for line in f:
            cords = line.split()
            self.appendPoint(int(cords[0]), int(cords[1]))

    def initUI(self):
        self.setGeometry(100, 100, self.wWidth, self.wHeight)
        self.setWindowTitle('Convex hull')
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        self.drawLines(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(QtCore.Qt.red)
        qp.setBrush(QtCore.Qt.red)
        size = self.size()
        radius = 3

        for point in self.pointList:
            center = QtCore.QPoint(point.x, point.y)
            qp.drawEllipse(center, radius, radius)

        qp.setPen(QtCore.Qt.green)
        qp.setBrush(QtCore.Qt.green)

        for point in self.routeList:
            center = QtCore.QPoint(point.x, point.y)
            qp.drawEllipse(center, radius, radius)

    def drawLines(self, qp):
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        for line in self.lineList:
            qp.drawLine(line.p1.x, line.p1.y, line.p2.x, line.p2.y)


        pen = QtGui.QPen(QtCore.Qt.green, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        for point in self.routeList:
            if self.routeList[-1] != point:
                p2 = self.routeList[self.routeList.index(point) + 1]
                qp.drawLine(point.x, point.y, p2.x, p2.y)

        QtGui.QWidget.update(self)



    def angleThreePoints(self, p1, p2, p3):
        # Angle between the lines from middle point to the others
        a = (p2.x-p1.x)**2 + (p2.y-p1.y)**2
        b = (p2.x-p3.x)**2 + (p2.y-p3.y)**2
        c = (p3.x-p1.x)**2 + (p3.y-p1.y)**2

        num =  (a + b - c)
        den = math.sqrt(4 * a * b)
        if den != 0:
            fraction = num / den
            if fraction < -1:
                fraction = -1
            if fraction > 1:
                fraction = 1

            res = math.acos( fraction )
            # print "angle ", res
            return res
        # print "angle ", 2*math.pi
        return 2*math.pi


    def getMowPoint(self, line, mowOffset):
        x1 = line.p1.x
        y1 = line.p1.y

        angle = self.angleThreePoints(line.p2, line.p1, Point(x1, y1**2 + 1))
        # print "sin", self.mowOffset * math.sin(angle)
        # print "cos", self.mowOffset * math.cos(angle)
        if line.p1.x > line.p2.x:
            x2 = x1 - math.sin(angle) * (mowOffset / math.cos(angle))
            #x2 = x1 - self.mowOffset * math.sin(angle)
            y2 = y1 + mowOffset# * math.cos(angle)
            return Point(x2, y2)
        else:
            x2 = x1 + math.sin(angle) * (mowOffset / math.cos(angle))
            #x2 = x1 + self.mowOffset * math.sin(angle)
            y2 = y1 + mowOffset# * math.cos(angle)
            return Point(x2, y2)

    def getLineIntersection(self, l1, l2):
        p0_x = l1.p1.x
        p0_y = l1.p1.y
        p1_x = l1.p2.x
        p1_y = l1.p2.y
        p2_x = l2.p1.x
        p2_y = l2.p1.y
        p3_x = l2.p2.x
        p3_y = l2.p2.y

        s1_x = p1_x - p0_x
        s1_y = p1_y - p0_y
        s2_x = p3_x - p2_x
        s2_y = p3_y - p2_y

        s = (-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)) / (-s2_x * s1_y + s1_x * s2_y)
        t = ( s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)) / (-s2_x * s1_y + s1_x * s2_y)

        if s >= 0 and s <= 1 and t >= 0 and t <= 1:
            #Collision detected
            i_x = p0_x + (t * s1_x)
            i_y = p0_y + (t * s1_y)
            return Point(i_x, i_y)
        return None # No collision

    def leftTurn(self, p1, p2, p3):
        res = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
        if res > 0:
            return False
        return True




    def mousePressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        self.appendPoint(x, y)
        QtGui.QWidget.update(self)

    # def mouseReleaseEvent(self, QMouseEvent):
    #     cursor =QtGui.QCursor()
    #     print cursor.pos()



def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
