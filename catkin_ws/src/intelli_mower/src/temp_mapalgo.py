#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('calc_done', String, queue_size=10)
    rospy.init_node('map_calc', anonymous=True)
    #rate = rospy.Rate
    rospy.sleep(5.)
    if not rospy.is_shutdown():
        calc_str = "calculated"
        # rospy.loginfo(calc_str)
        pub.publish(calc_str)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
