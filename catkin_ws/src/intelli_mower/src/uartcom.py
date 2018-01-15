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

def updateMowerStatsByte(mowerStats, byteNumber, value):
    if byteNumber == 0:
        mowerStats.command = value
        rospy.loginfo(ord(tmpStr))
    elif byteNumber == 1:
        mowerStats.bumperFront = value
    elif byteNumber == 2:
        mowerStats.bumperBack = value
    elif byteNumber == 3:
        mowerStats.emergency = value
    elif byteNumber == 4:
        mowerStats.cutter = value
    elif byteNumber == 5:
        mowerStats.lift = value


def updateMowerStatsFloat(mowerStats, floatNumber, value):
    if floatNumber == 0:
        mowerStats.leftSpeed = floatValue
    elif floatNumber == 1:
        mowerStats.rightSpeed = floatValue
    elif floatNumber == 2:
        mowerStats.outerRight = floatValue
    elif floatNumber == 3:
        mowerStats.innerRight = floatValue
    elif floatNumber == 4:
        mowerStats.innerLeft = floatValue
    elif floatNumber == 5:
        mowerStats.outerLeft = floatValue
    elif floatNumber == 6:
        mowerStats.xPos = floatValue
    elif floatNumber == 7:
        mowerStats.yPos = floatValue
    elif floatNumber == 8:
        mowerStats.heading = floatValue



def talker():
    firstTime = True
    readByte = b''
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
            
            # Str = b'\x0A'
            # Str = cobs.encode(Str)+b'\x00'
            
            readByte = ser.read()
            bufferUart += readByte
            
            
            while readByte != "":
                readByte = ser.read()
                bufferUart += readByte
                
                # If the buffer was cleared on the previous iteration and
                # there is no new byte to read, continue. (should break instead?)
                if len(bufferUart) == 0:
                    continue

                # Check if end of transmission (if the last byte is zero)
                if ord(bufferUart[-1]) == 0:
                   
                    # Convert the ASCII values to the values that they represent
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
                    mowerStats = MowerStats()
                    for x in decoded:
                        tmpStr += x

                        # The 6 first bytes represents single byte values
                        if byteNumber < 6 and len(tmpStr) == 1:
                            updateMowerStatsByte(mowerStats, byteNumber, tmpStr)
                            tmpStr = ''
                            byteNumber += 1
                        
                        # The rest of the data represents double precision float
                        # values (8 bytes long)
                        elif len(tmpStr) == 8:
                            floatValue = byteToFloat(tmpStr)[0]
                            updateMowerStatsFloat(mowerStats, floatNumber, floatValue)
                            tmpStr = ''
                            floatNumber += 1

                    pub.publish(mowerStats)
                   
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
