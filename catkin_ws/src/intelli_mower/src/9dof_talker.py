#!/usr/bin/env python
from __future__ import print_function
import rospy
import roslib
#from std_msgs.msg import String
from sensor_msgs.msg import Imu
import time, sys, math
sys.path.insert(0, '/home/pi/projects/D7039E_RPi/I2C/python')
from nxp_imu import FXAS21002, FXOS8700, I2C, IMU
from nxp_imu import IMU as imu

import tf

#from i2clibraries import i2c_hmc5883l
#hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1)
#hmc5883l.setContinuousMode()
#hmc5883l.setDeclination(0,6)

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

global Xavg, Yavg, Zavg
global r, p, h, a, m, g
global Havg

imuMsg = Imu()

'''Magnetometer calibration avarages'''
Xavg = -280 
Yavg = -452
Zavg = -1548

def read9():

	
	#--------9dof init----------
	imu = IMU(gs=2, dps=2000, verbose=False)
	i2c = I2C(0x1F)
	
	#--------Set calibration values for magnetometer---------
	'''Splits avarages to MSB and LSB'''
	XMSB = (Xavg/256) & 0xFF
	XLSB = Xavg & 0xFF
	YMSB = (Yavg/256) & 0xFF
	YLSB = Yavg & 0xFF
	ZMSB = (Zavg/256) & 0xFF
	ZLSB = Zavg & 0xFF
	
	'''Writes splitted avarages to offset registers'''
	i2c.write8(0x3F, int(XMSB))
	i2c.write8(0x40, int(XLSB))
	i2c.write8(0x41, int(YMSB))
	i2c.write8(0x42, int(YLSB))
	i2c.write8(0x43, int(ZMSB))
	i2c.write8(0x44, int(ZLSB))

	
	#--------Talker node init------------
	#pub = rospy.Publisher('chatter', String, queue_size=10)
	pub = rospy.Publisher('imu', Imu)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10) # 25hz
	
	#---------Readloop---------
	while not rospy.is_shutdown():
		Havg = 0
		
		#Collects samples and returns avaraged value.
		for x in range (0, 20):
			try: 
				a, m, g = imu.get() 					#Gets data from sensors
				r, p, h = imu.getOrientation(a, m) 		#calculates orientation from data
				ac, ma = imu.rawOrientation() 			#raw data for magnetometer
				
				'''
				#Prevents error in Havg when heading fluctuates between 359 and 0.
				if(x > 1):
					if(Havg > 260):
						if(h < 100):
							h += 360
					if(Havg < 100):
						if(h > 260):
							h -= 360
				
				Havg = (Havg + h)/2
				'''
			except IOError:
				pass
		'''
		#Corrects the heading so that 0 < Havg < 359.
		if(Havg < 0):
			Havg += 360
		if(Havg >= 360):
			Havg -= 360
		
		heading = str(Havg)
		'''
		roll  =  r * (3.141592/180.0) #converts degrees to radians
		pitch =  p * (3.141592/180.0)
		yaw   =  h * (3.141592/180.0)
		'''
		a[0] = a[0] * 9.806 #converts g's to m/s^2
		a[1] = a[1] * 9.806
		a[2] = a[2] * 9.806
		
		g[0] = g[0] * (3.141592/180.0) #converts degrees to radians
		g[1] = g[1] * (3.141592/180.0)
		g[2] = g[2] * (3.141592/180.0)
		'''
		print("Heading: " + str(h))
		#q = toQuaternion(r, p, h)
		q = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
		imuMsg.orientation.x = q[0] #magnetometer
		imuMsg.orientation.y = q[1]
		imuMsg.orientation.z = q[2]
		imuMsg.orientation.w = q[3]
		
		imuMsg.angular_velocity.x = g[0] * (3.141592/180.0) #gyro
		imuMsg.angular_velocity.y = g[1] * (3.141592/180.0)
		imuMsg.angular_velocity.z = g[2] * (3.141592/180.0)
		
		imuMsg.linear_acceleration.x = a[0] * 9.806 #accelerometer
		imuMsg.linear_acceleration.y = a[1] * 9.806
		imuMsg.linear_acceleration.z = a[2] * 9.806
		
		rospy.loginfo(imuMsg)
		pub.publish(imuMsg)
		rate.sleep()

'''		
def readHeading():
	print(hmc5883l.getHeading())
	
def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        heading = hmc5883l.getHeading() % rospy.get_time()
        rospy.loginfo(heading)
        pub.publish(heading)
        rate.sleep()
'''


if __name__ == '__main__':
    try:
        read9()
    except rospy.ROSInterruptException:
        pass
