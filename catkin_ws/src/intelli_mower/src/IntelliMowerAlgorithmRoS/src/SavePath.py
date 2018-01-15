#
def SavePath(pathList):

    f = open("/home/pi/catkin_ws/src/intelli_mower/src/IntelliMowerAlgorithmRoS/src/path_list", 'w')

    for point in pathList:
        f.write("%s" % float(point.x) )
        f.write(' ')
        f.write("%s\n" % float(point.y) )

    f.close()
