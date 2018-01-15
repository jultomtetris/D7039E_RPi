
//#include "framework/CmdSys.h"
#include "../include/intelli_mower/CmdSys.h"
#include "../include/intelli_mower/SpiSender.h"
#include <stdio.h>
#include "ros/ros.h"
#include "std_msgs/String.h"
#include "nav_msgs/Odometry.h"
#include <sstream>
#include <string>
#include <fstream>
#include <iterator>
#include <vector>
//#include <math>

int isCalc;
int readMap;
int firstMove;
double lastDist = 1000000;
double origDist;
struct CoordinatePair
{
		double x;
		double y;
};
int XorY = 0;
int stopThis = 0;
std::vector<CoordinatePair> v;

CoordinatePair targetPoint;
//#include "CmdSys.h"



std::istream& operator>>(std::istream& is, CoordinatePair& coordinates)
{
    is >> coordinates.x >> coordinates.y;

    return is;
}

double GetDistTwoPoints( double x1, double y1, double x2, double y2) {
	CoordinatePair p1;
	CoordinatePair p2;
	ROS_INFO("GETDIST");
	ROS_INFO("x1 %f", x1);
	ROS_INFO("y1 %f", y1);
	ROS_INFO("x2 %f", x2);
	ROS_INFO("y2 %f", y2);
	p1.x = x1;
	p1.y = y1;
	p2.x = x2;
	p2.y = y2;
  return sqrt( ( (p2.x - p1.x	) * (p2.x - p1.x) ) + ( (p2.y - p1.y) * (p2.y - p1.y) ) );
	 //return sqrt(2500);

}

bool checkNextPoint(double currentX, double currentY) {
	double deviation = 10.0;
	ROS_INFO("CheckPOINT");
	double newDist = GetDistTwoPoints(targetPoint.x, targetPoint.y, currentX, currentY);
	ROS_INFO("lastDist [%f]", lastDist);
	ROS_INFO("newDist [%f]", newDist);

	if (newDist > origDist / 2) {
		return false;
	}

	if (newDist > lastDist || newDist < 5.0){
		ROS_INFO("STOP");
		SendStop();
		targetPoint.x = v.back().x;
		targetPoint.y = v.back().y;
		if (v.size() == 0){
			stopThis = 1;
		}
		v.pop_back();
		XorY = 1;
		lastDist = 1000000;

		return true;
	}

	// if ((newDist > lastDist) && (XorY == 1)){
	// 	ROS_INFO("STOP");
	//  	SendStop();
	//  	targetPoint.x = v.back().x;
	//  	targetPoint.y = v.back().y;
	//  	v.pop_back();
	//  	stopThis = 1;
	// 	lastDist = 1000000;
	//  	return true;
	//  }
	 lastDist = newDist;
	return false;

}

void chatterCallback (const nav_msgs::Odometry::ConstPtr& msg) {
	double currentX = msg->pose.pose.position.x;
	double currentY = msg->pose.pose.position.y;

	if ((stopThis == 0) && (isCalc == 1)) {
		if(checkNextPoint(currentX, currentY) || firstMove == 1) {
			//SendStop();
			origDist = GetDistTwoPoints(currentX, currentY, targetPoint.x, targetPoint.y);
			SendMove(-50, msg->pose.pose.position.x, msg->pose.pose.position.y, (float)targetPoint.x, (float)targetPoint.y);
			ROS_INFO("SEND_MOVE");
			firstMove = 0;
		}
    //
		// if(isCalc == 1 && readMap == 1) {
		// 	//ROS_INFO("Seq: [%d]", msg->header.seq);
		// 	//ROS_INFO("I heard X: [%f]", msg->pose.pose.position.x);
		// 	//ROS_INFO("I heard Y: [%f]", msg->pose.pose.position.y);
		// 	//FeedCurrentPosition(msg->pose.pose.position.x, msg->pose.pose.position.y);
		// }
	}else{
		ROS_INFO("COMPLETE STOP");
		SendStop();
	}

}

void calcCallback (const std_msgs::String::ConstPtr& msg) {
	ROS_INFO("INSIDE CALLBACK");
	ROS_INFO("Message recieved: [%s]", msg->data.c_str());
	std::string recmsg = msg->data.c_str();
	if (recmsg == "calculated") {
		ROS_INFO("STRING_CHECK");
		isCalc = 1;
		char filename[] = "/home/pi/catkin_ws/src/intelli_mower/src/IntelliMowerAlgorithmRoS/src/path_list";
		std::ifstream ifs(filename);
		if(ifs){
			ROS_INFO("INSIDE FILEREAD");
			std::copy(std::istream_iterator<CoordinatePair>(ifs),std::istream_iterator<CoordinatePair>(),std::back_inserter(v));
			readMap = 1;
		}
		for (int i =0; i<v.size(); i++){
			ROS_INFO("x: [%f]", v.at(i).x);
			ROS_INFO("y: [%f]", v.at(i).y);
		}
		targetPoint.x = v.back().x;
		targetPoint.y = v.back().y;
		v.pop_back();
		firstMove = 1;
	}
	else {
		isCalc = 0;
	}
}

int main(int argc, char **argv){
	isCalc = 0;
	readMap = 0;
	firstMove = 0;
	initSpi();
	//SendMove(-30, 2200, 900, 2200, 2900);
	// testParser();
	ros::init(argc, argv, "listener");
	ros::NodeHandle n;
	//ros::Publisher mapSendCalc = n.advertise<std_msgs::int16>("mapSendCalc", 1000);

	// if(ros::ok()) {
	// 	std_msgs::Int16 cmdToCalc;
	// 	cmdToCalc = 1;
	// 	ROS_INFO("%d", cmdToCalc.data());
	// 	mapSendCalc.publish(msg);
	// }
	ros::Subscriber mapcalc = n.subscribe("calc_done", 1000, calcCallback);
	ROS_INFO("HOW TO");
	//ros::Subscriber sub = n.subscribe("uwb_pos_pub", 1000, chatterCallback);
  	ros::Subscriber sub = n.subscribe("uwb_pos_pub", 1000, chatterCallback);
	//ros::Subscriber sub2 = n.subscribe("sam_mapping", 1000, chatter2Callback);

	ros::spin();
	endSpi();
	return 0;
}
