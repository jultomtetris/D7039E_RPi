
from Geometry import Point
from IntelliMower import IntelliMower

from PyQt4 import QtGui, QtCore
from operator import itemgetter, attrgetter

import time

class UserInterface(QtGui.QWidget):
    iMower = IntelliMower()
    drawPointList = []
    drawLineList = []
    draw = 0

    #
    def __init__(self):
        self.iMower = IntelliMower()
        self.drawPointList = []
        self.drawLineList = []
        self.draw = 0
        self.isCalcPathActivated = 0
        super(UserInterface, self).__init__()
        #self.readInputFile()
        QtGui.QWidget.__init__(self)

        self.lawnButton = QtGui.QPushButton('NewLawn', self)
        self.obstacleButton = QtGui.QPushButton('NewObstacle', self)
        self.calculateButton = QtGui.QPushButton('Calculate', self)
        self.placeMowerButton = QtGui.QPushButton('PlaceMower', self)
        self.placeStationButton = QtGui.QPushButton('PlaceStation', self)
        self.nextPathButton = QtGui.QPushButton('NextPath', self)
        self.calcPathButton = QtGui.QPushButton('CalcPath', self)
        self.saveButton = QtGui.QPushButton('Save', self)
        self.loadButton = QtGui.QPushButton('Load', self)

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.lawnButton)
        layout.addWidget(self.obstacleButton)
        layout.addWidget(self.calculateButton)
        layout.addWidget(self.placeMowerButton)
        layout.addWidget(self.placeStationButton)
        layout.addWidget(self.nextPathButton)
        layout.addWidget(self.calcPathButton)
        layout.addWidget(self.saveButton)
        layout.addWidget(self.loadButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(layout)
        self.setLayout(vbox)

        # button logic
        self.lawnButton.clicked.connect( self.NewLawn )
        self.obstacleButton.clicked.connect( self.NewObstacle )
        self.calculateButton.clicked.connect(self.Calculate)
        self.placeMowerButton.clicked.connect( self.PlaceMower )
        self.placeStationButton.clicked.connect(self.PlaceStation)
        self.nextPathButton.clicked.connect( self.NextPath )
        self.calcPathButton.clicked.connect( self.CalculatePath )
        self.saveButton.clicked.connect( self.Save )
        self.loadButton.clicked.connect( self.Load )

    #
    def Init(self, wWidth, wHeight):
        print "Sweep line drawing off"
        self.setGeometry(100, 100, wWidth, wHeight)
        self.setWindowTitle('IntelliMower Lawn Plotter Tool v0.4')
        self.show()

    #
    def NewLawn(self):
        self.iMower.Reset()
        self.draw = 1
        QtGui.QWidget.update( self )
        self.iMower.SetState( 1 )

    #
    def NewObstacle(self):
        self.iMower.SetState( 2 )

    #
    def Calculate(self):
        self.iMower.SetState(0)
        self.iMower.Calculate()
        self.draw = 1
        QtGui.QWidget.update( self )

    #
    def PlaceMower(self):
        self.iMower.SetState(3)

    #
    def PlaceStation(self):
        self.iMower.SetState(4)

    #
    def NextPath(self):
        #self.iMower.SetState(3)
        self.iMower.FindNextPath()
        self.draw = 1
        QtGui.QWidget.update(self)

    #
    def CalculatePath(self):
        #self.iMower.SetState(3)
        startTime = time.time()
        while self.iMower.pathCalcComplete != 1:
            newTime = time.time() - startTime
            self.iMower.FindNextPath()
            self.draw = 1
            QtGui.QWidget.update(self)
            QtGui.QApplication.processEvents()

            # wait for approx 2 secs
            # while True:
            #     if newTime >= 2:
            #         newTime = 0
            #         startTime = time.time()
            #         break
        elapsedTime = time.time() - startTime
        print ( "Elapsed Time:", elapsedTime )
        self.iMower.SavePath()

    #
    def Save(self):
        self.iMower.SetState(0)
        self.iMower.SaveMap()

    #
    def Load(self):
        self.iMower.Reset()
        self.iMower.LoadMap()
        self.draw = 1
        QtGui.QWidget.update(self)

    #
    def mousePressEvent(self, event):
        self.iMower.Controller( event.pos().x(), event.pos().y() )
        self.draw = 1
        QtGui.QWidget.update(self)

    #
    def mouseReleaseEvent(self, QMouseEvent):
        #cursor = QtGui.QCursor()
        #print ("Positions relative screen: ")
        #print cursor.pos()
        return

    #
    def GetMousePos(self):
        return

    #
    def paintEvent(self, e):
        if self.draw == 1:
            self.w = QtGui.QWidget(self)
            #qtw = QtGui.QListWidget()
            palette = self.w.palette()
            role = self.w.backgroundRole()
            palette.setColor(role, QtCore.Qt.white)
            self.w.setPalette(palette)

            palette = self.palette()
            role = self.backgroundRole()
            palette.setColor(role, QtCore.Qt.white)
            self.setPalette(palette)

            #qtw.setAutoFillBackground(True)
            #qtw.setPalette(p)

            qp = QtGui.QPainter()
            qp.begin(self)
            self.DrawLines(qp)
            self.DrawPoints(qp)
            qp.end()
            self.draw = 1

    #
    def DrawPoints(self, qp):

        #draw collision points
        self.drawPointList = self.iMower.lawn.collisionPairs
        for point in self.drawPointList:
            qp.setPen(QtCore.Qt.black)
            qp.setBrush(QtCore.Qt.black)
            size = self.size()
            radius = 2
            center = QtCore.QPoint(point.x, point.y)
            qp.drawEllipse(center, radius, radius)

        # Draw mower
        if self.iMower.posX != 0 and self.iMower.posY != 0:
            qp.setPen(QtCore.Qt.blue)
            qp.setBrush(QtCore.Qt.blue)
            size = self.size()
            radius = 30
            center = QtCore.QPoint(self.iMower.posX, self.iMower.posY)
            qp.drawEllipse(center, radius, radius)

        # Draw station
        if self.iMower.stationPosX != 0 and self.iMower.stationPosY != 0:
            qp.setPen(QtCore.Qt.black)
            qp.setBrush(QtCore.Qt.black)
            size = self.size()
            radius = 10
            center = QtCore.QPoint(self.iMower.stationPosX, self.iMower.stationPosY)
            qp.drawEllipse(center, radius, radius)
    #
    def DrawLines(self, qp):
        # draw Lawn border line
        pen = QtGui.QPen(QtCore.Qt.black , 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        self.drawLineList = self.iMower.lawn.outerBorder.lineList
        for line in self.drawLineList:
            qp.drawLine(line.p1.x, line.p1.y, line.p2.x, line.p2.y)

        # draw obstacle borders
        numObstacles = len(self.iMower.lawn.innerBorders)
        if numObstacles > 0:
            # Obstacle line settings
            pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
            qp.setPen(pen)
            i = 0
            while True:
                if i >= numObstacles:
                    break
                self.drawLineList = self.iMower.lawn.innerBorders[i].lineList
                i+=1
                for line in self.drawLineList:
                    qp.drawLine(line.p1.x, line.p1.y, line.p2.x, line.p2.y)

        # draw bounding box
        # if len( self.iMower.lawn.boundingBox ) > 0:
        #     pen = QtGui.QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine)
        #     qp.setPen(pen)
        #
        #     qp.drawLine( self.iMower.lawn.boundingBox[0].x, self.iMower.lawn.boundingBox[0].y, self.iMower.lawn.boundingBox[1].x, self.iMower.lawn.boundingBox[1].y )
        #     qp.drawLine( self.iMower.lawn.boundingBox[1].x, self.iMower.lawn.boundingBox[1].y, self.iMower.lawn.boundingBox[2].x, self.iMower.lawn.boundingBox[2].y )
        #     qp.drawLine( self.iMower.lawn.boundingBox[2].x, self.iMower.lawn.boundingBox[2].y, self.iMower.lawn.boundingBox[3].x, self.iMower.lawn.boundingBox[3].y )
        #     qp.drawLine( self.iMower.lawn.boundingBox[3].x, self.iMower.lawn.boundingBox[3].y, self.iMower.lawn.boundingBox[0].x, self.iMower.lawn.boundingBox[0].y )

        # draw sweep lines
        if len( self.iMower.lawn.sweepLines ) > 0:
            # Sweep line settings
            pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
            qp.setPen(pen)
            self.drawLineList = self.iMower.lawn.sweepLines

            #for line in self.drawLineList:
                #qp.drawLine(line.p1.x, line.p1.y, line.p2.x, line.p2.y)

        #draw collision pair lines
        numPairs = len( self.iMower.lawn.collisionPairs)
        if numPairs > 0:
            pen = QtGui.QPen(QtCore.Qt.green, 2, QtCore.Qt.SolidLine)
            qp.setPen(pen)
            tmpPointList = self.iMower.lawn.collisionPairs
            i = 0
            while True:
                if i >= (numPairs - 1):
                    break
                #if tmpPointList[i].id == tmpPointList[i+1].id:
                qp.drawLine(tmpPointList[i].x, tmpPointList[i].y, tmpPointList[i+1].x, tmpPointList[i+1].y)
                i+=2

        #mow paths
        numRoutePoints = len( self.iMower.path.pathList )
        if numRoutePoints > 1:
            pen = QtGui.QPen(QtCore.Qt.blue, 5, QtCore.Qt.SolidLine)
            qp.setPen(pen)
            tmpPointList = self.iMower.path.pathList
            i = 0
            while i < ( numRoutePoints - 1 ):
                qp.drawLine(tmpPointList[i].x, tmpPointList[i].y, tmpPointList[i+1].x, tmpPointList[i+1].y)
                i+=1

        #draw traveled paths
        # numRoutePoints = len( self.iMower.path.pathList )
        # if numRoutePoints > 1:
        #     pen = QtGui.QPen( QtCore.Qt.red, 10, QtCore.Qt.SolidLine )
        #     qp.setPen(pen)
        #     tmpPointList = self.iMower.path.pathList
        #     i = 0
        #     while i < ( numRoutePoints - 2 ):
        #         qp.drawLine( tmpPointList[i].x, tmpPointList[i].y, tmpPointList[i+1].x, tmpPointList[i+1].y )
        #         i+=2
