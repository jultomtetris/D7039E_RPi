#include "CmdSys.h"
#include "../com/SpiSender.h"
#include <stdio.h>

uint8_t rawData[BUFFERSIZE];

void TypeCast32To8(int conv, uint8_t *converted) {
  converted[0] = (conv >> 24) & 0xFF;
  converted[1] = (conv >> 16) & 0xFF;
  converted[2] = (conv >> 8) & 0xFF;
  converted[3] = conv & 0xFF;
  //return converted;
}

void SendStop(){
  rawData[0] = MCU_STOP;
  transfer(rawData);
}

void SendForward(uint8_t speed) {
  rawData[0] = MCU_FORWARD;
  rawData[1] = speed;
  transfer(rawData);
}

void SendReverse(uint8_t speed) {
  rawData[0] = MCU_REVERSE;
  rawData[1] = speed;
  transfer(rawData);
}

void SendLeft(uint8_t speed) {
  rawData[0] = MCU_LEFT;
  rawData[1] = speed;
  transfer(rawData);
}

void SendRight(uint8_t speed) {
  rawData[0] = MCU_RIGHT;
  rawData[1] = speed;
  transfer(rawData);
}

void  SendMove(uint8_t speed, int xCoord, int yCoord) {
  uint8_t xCoordArr[4];
  uint8_t yCoordArr[4];
  TypeCast32To8(xCoord, xCoordArr);
  TypeCast32To8(yCoord, yCoordArr);
  rawData[0] = MCU_MOVE;
  rawData[1] = speed;
  rawData[2] = xCoordArr[0];
  rawData[3] = xCoordArr[1];
  rawData[4] = xCoordArr[2];
  rawData[5] = xCoordArr[3];
  rawData[6] = yCoordArr[0];
  rawData[7] = yCoordArr[1];
  rawData[8] = yCoordArr[2];
  rawData[9] = yCoordArr[3];
  transfer(rawData);
}

void FeedCurrentPosition (int xCoord, int yCoord) {
  uint8_t xCoordArr[4];
  uint8_t yCoordArr[4];
  TypeCast32To8(xCoord, xCoordArr);
  TypeCast32To8(yCoord, yCoordArr);
  rawData[0] = MCU_FEED;
  rawData[1] = xCoordArr[0];
  rawData[2] = xCoordArr[1];
  rawData[3] = xCoordArr[2];
  rawData[4] = xCoordArr[3];
  rawData[5] = yCoordArr[0];
  rawData[6] = yCoordArr[1];
  rawData[7] = yCoordArr[2];
  rawData[8] = yCoordArr[3];
  transfer(rawData);
}

void TempTest () {
  initSpi();
  int input_speed;
  int command;
  int xcoord = 0;
  int ycoord = 0;
  printf("Commands:\n 1:STOP\n 2:FORWARD\n 3:REVERSE\n 4:LEFT\n 5:REFT\n 6:MOVE\n 7:FEED\n");
  printf("Choose command 1-7:\n");
  scanf("%d", &command);
  uint8_t uspeed;
  switch(command) {
    case 1 :
      SendStop();
      break;
    case 2 :
      printf("Set Speed -100-100:\n");
      scanf("%d", &input_speed);
      uspeed = (uint8_t)input_speed;
      SendForward(uspeed);
      break;
    case 3 :
      printf("Set Speed -100-100:\n");
      scanf("%d", &input_speed);
      uspeed = (uint8_t)input_speed;
      SendReverse(uspeed);
      break;
    case 4 :
      printf("Set Speed -100-100:\n");
      scanf("%d", &input_speed);
      uspeed = (uint8_t)input_speed;
      SendLeft(uspeed);
      break;
    case 5 :
      printf("Set Speed -100-100:\n");
      scanf("%d", &input_speed);
      uspeed = (uint8_t)input_speed;
      SendRight(uspeed);
      break;
    case 6 :
      printf("Set Speed -100-100:\n");
      scanf("%d", &input_speed);
      uspeed = (uint8_t)input_speed;
      printf("Set xcoord:");
      scanf("%d", &xcoord);
      printf("Set ycoord:");
      scanf("%d", &ycoord);
      SendMove(uspeed, xcoord, ycoord);
      break;
    case 7 :
      printf("Set xcoord:");
      scanf("%d", &xcoord);
      printf("Set ycoord:");
      scanf("%d", &ycoord);
      FeedCurrentPosition(xcoord, ycoord);
      break;
    default :
      //return 0;
      break;
  }
  endSpi();
}
