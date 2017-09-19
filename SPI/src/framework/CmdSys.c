#include "CmdSys.h"
#include "../com/SpiSender.h"

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
