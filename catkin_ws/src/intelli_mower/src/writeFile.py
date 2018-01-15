#!/usr/bin/env python
import rospy
from intelli_mower.msg import MowerStats

def callback(mowerstats):
    rospy.loginfo("Line 1 CMD: %d", ord(mowerstats.command))
    rospy.loginfo("Line 1 Front: %s", mowerstats.bumperFront)
    rospy.loginfo("Line 1 Back: %s", mowerstats.bumperBack)
    rospy.loginfo("Line 1 xPos: %f", mowerstats.xPos)
    rospy.loginfo("Line 1 yPos: %f", mowerstats.yPos)

def listener():
    rospy.init_node('writeFile', anonymous=True)

    rospy.Subscriber('mowstats', MowerStats, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
