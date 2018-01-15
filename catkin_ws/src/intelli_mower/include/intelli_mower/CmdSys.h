#ifndef CMDSYS_H_
#define CMDSYS_H_
#include <stdint.h>
#include "std_msgs/String.h"
#include "ros/ros.h"
#include <sstream>
#include <string>

#define MCU_STOP 0x01
#define MCU_FORWARD 0x02
#define MCU_REVERSE 0x03
#define MCU_LEFT 0x04
#define MCU_RIGHT 0x05
#define MCU_MOVE 0x06
#define MCU_FEED 0x07
#define MCU_NULL 0x00


void SendStop();
void SendForward(uint8_t speed);
void SendReverse(uint8_t speed);
void SendLeft(uint8_t speed);
void SendRight(uint8_t speed);
void SendMove(uint8_t speed, int xCurrentPos, int yCurrentPos, int xCoord, int yCoord);
void FeedCurrentPosition(float xCoord, float yCoord);
void TempTest(const std_msgs::String::ConstPtr& msg);

#endif /*CMDSYS_H_*/
