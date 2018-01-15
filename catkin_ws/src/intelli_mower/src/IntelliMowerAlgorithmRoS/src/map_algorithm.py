#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from Common import Common

def talker():
	calc = 'calculated'
	pub = rospy.Publisher('calc_done', String, queue_size=10)
	rospy.init_node('mapcalc', anonymous=True)
	common = Common()
	common.Init()
	common.Frame()
	if not rospy.is_shutdown():
		rospy.loginfo(calc)
		pub.publish(calc)

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
