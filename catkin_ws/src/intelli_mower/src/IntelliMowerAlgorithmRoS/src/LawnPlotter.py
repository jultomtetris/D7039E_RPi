

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

   # def randomHandler(self):
       # self.resetHandler()
       # random.seed()
        #tempList = [ ( random.randint(5, self.wWidth - 5), random.randint(5, self.wHeight - 50) ) for k in range(100) ]
       # for elem in tempList:
           # self.appendPoint(elem[0], elem[1])

    #def readHandler(self):
        #self.readInputFile()
       # QtGui.QWidget.update(self)


   # def readInputFile(self):
        #self.resetHandler()
        #f = open('points', 'r')
        #for line in f:
           # cords = line.split()
          #  self.appendPoint(int(cords[0]), int(cords[1]))

class LawnPlotter():
    pointList = []
    lineList = []
    routeList = []

    mowOffset = 30
    def __init__(self):

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


        def Reset(self):
            self.pointList = []
            self.lineList = []
            self.routeList = []
