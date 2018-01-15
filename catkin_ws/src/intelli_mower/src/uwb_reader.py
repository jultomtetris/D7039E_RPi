#!/usr/bin/env python
import serial
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry

def parseStr(inStr):
    x = ""
    y = ""
    commaList = []
    for i in range(len(inStr)):
        if inStr[i] == ",":
            commaList.append(i)

    x = inStr[commaList[0] + 1:commaList[1]]
    y = inStr[commaList[1] + 1:commaList[2]]
    return int(x), int(y)


def talker():
    line = ""
    pub = rospy.Publisher('uwb_pos_pub', Odometry, queue_size=10)
    rospy.init_node('uwb', anonymous=True)
    rospy.sleep(10.)
    rate = rospy.Rate(2) # 10hz
    while not rospy.is_shutdown():
        with serial.Serial('/dev/ttyACM0', 9600, timeout=None) as ser:
            line = ser.readline()
            while line != "":
                line = ser.readline()
                if line[:5] == "POS2D":
                    x, y = parseStr(line)
                    odometry = Odometry()
                    odometry.pose.pose.position.x = x
                    odometry.pose.pose.position.y = y
                    rospy.loginfo(odometry)
                    pub.publish(odometry)
        rate.sleep()

if __name__ == '__main__':
   try:
       talker()
   except rospy.ROSInterruptException:
       pass
