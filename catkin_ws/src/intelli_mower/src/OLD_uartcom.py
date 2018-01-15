#!/usr/bin/env python
import serial
import rospy
import struct
#import re
from intelli_mower.msg import MowerStats
from cobs import cobs
# from nav_msgs.msg import Odometry
coordinates = []

def byteToInt(stringToDecode):
    return struct.unpack_from("d", stringToDecode)

def byteToFloat(stringToDecode):
    return struct.unpack('d', stringToDecode)
def floatToByte(floatToEncode):
    return bytearray(struct.pack('d', floatToEncode))

def readMap():
    global coordinates
    rospy.loginfo("readMap")
    with open('/home/pi/catkin_ws/src/intelli_mower/src/IntelliMowerAlgorithmRoS/src/path_list', 'r') as inp:
        for line in inp:
            row = line.split()
            #rospy.loginfo("This is MAP: %d", row)
            rospy.loginfo(row)
            coordinates.append(row)
def getNextPoint():
    global coordinates
    if len(coordinates) == 0:
        return (floatToByte(0.0), floatToByte(0.0))
    pair = coordinates.pop()
    x = float(pair[0])
    y = float(pair[1])
    rospy.loginfo("X:%f", x)
    rospy.loginfo("Y:%f", y)
    return (floatToByte(x), floatToByte(y))

def talker():
    firstTime = True
    line = b''
    decoded = b''
    bufferUart = b''
    pub = rospy.Publisher('mowstats', MowerStats, queue_size=10)
    rospy.init_node('uartcom', anonymous=True)
    #rospy.loginfo("TALKER")
    readMap()
    rate = rospy.Rate(10) #10Hz
    while not rospy.is_shutdown():
        #rospy.loginfo("is_shutdown")
        with serial.Serial('/dev/ttyUSB0', 9600, timeout=0.1) as ser:

            if firstTime == True:
                strToSend = b'\x06'
                encoded = b''
                nextPoint = getNextPoint()
                strToSend = b'\x06' + b'\xC9' + nextPoint[1] + nextPoint[1] + nextPoint[0] + nextPoint[1]
                encoded = cobs.encode(str(strToSend))
                ser.write(encoded + b'\x00')
                firstTime = False
            Str = b'\x0A'
            Str = cobs.encode(Str)+b'\x00'
            #rospy.loginfo(Str)
            #ser.write(Str)
            line = ser.read()
            bufferUart += line
            #test1 = 0
            #xPos = 0
            #yPos = 0
            while line != "":
                #rospy.loginfo("Serialread")
                line = ser.read()
                bufferUart += line
                if len(bufferUart) == 0:
                    #rospy.loginfo("BUFFEREMPTY")
                    continue
                if ord(bufferUart[-1]) == 0:
                    #rospy.loginfo("BUFFERDONE")
                    tmp = b''
                    for c in bufferUart:
                        if ord(c) == 0:
                            continue
                        tmp += c
                    decoded = cobs.decode(tmp)
                    bufferUart = b''
                    tmpStr = ''
                    byteNumber = 0
                    floatNumber = 0
                    mowerstats = MowerStats()
                    for x in decoded:
                        #rospy.loginfo("For x in decoded")
                        tmpStr += x
                        if byteNumber < 6 and len(tmpStr) == 1:
                            if byteNumber == 0:
                                mowerstats.command = tmpStr
                                rospy.loginfo(ord(tmpStr))
                            if byteNumber == 1:
                                mowerstats.bumperFront = tmpStr
                            if byteNumber == 2:
                                mowerstats.bumperBack = tmpStr
                            if byteNumber == 3:
                                mowerstats.emergency = tmpStr
                            if byteNumber == 4:
                                mowerstats.cutter = tmpStr
                            if byteNumber == 5:
                                mowerstats.lift = tmpStr
                            tmpStr = ''
                            byteNumber += 1
                        if len(tmpStr) == 8:
                            if floatNumber == 0:
                                mowerstats.leftSpeed = byteToFloat(tmpStr)[0]
                            if floatNumber == 1:
                                mowerstats.rightSpeed = byteToFloat(tmpStr)[0]
                            if floatNumber == 2:
                                mowerstats.outerRight = byteToFloat(tmpStr)[0]
                            if floatNumber == 3:
                                mowerstats.innerRight = byteToFloat(tmpStr)[0]
                            if floatNumber == 4:
                                mowerstats.innerLeft = byteToFloat(tmpStr)[0]
                            if floatNumber == 5:
                                mowerstats.outerLeft = byteToFloat(tmpStr)[0]
                            if floatNumber == 6:
                                mowerstats.xPos = byteToFloat(tmpStr)[0]
                            if floatNumber == 7:
                                mowerstats.yPos = byteToFloat(tmpStr)[0]
                            if floatNumber == 8:
                                mowerstats.heading = byteToFloat(tmpStr)[0]
                            tmpStr = ''
                            floatNumber += 1
    #                rospy.loginfo("PUBLISH")
                    pub.publish(mowerstats)
                    if ord(mowerstats.command) == 1:
                        rospy.loginfo("newtarget")
                        strToSendTwo = b'\x06'
                        encodedTwo = b''
                        nextPointTwo = getNextPoint()
                        strToSendTwo = b'\x06' + b'\xC9' + nextPointTwo[0] + nextPointTwo[0] + nextPointTwo[0] + nextPointTwo[1]
                        encodedTwo = cobs.encode(str(strToSendTwo))
                        rospy.loginfo(str(encodedTwo))
                        #print   format(int(encodedTwo),'02x')
                        ser.write(encodedTwo + b'\x00')
                        rospy.sleep(0.3)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
