#include "CmdSys.h"
#include <stdio.h>

//#include "CmdSys.h"

#define BUFFERSIZE 10



int main(){
	/*uint8_t raw_data[BUFFERSIZE];
	uint8_t cmd = 0x04;
	int input_speed;
	//uint8_t speed = 60;
	uint8_t speed;
	printf("Please submit the desired Speed...\n");
	scanf("%d", &input_speed);
	speed = (uint8_t)input_speed;
	printf("Speed: %d\n", speed);
	raw_data[0] = cmd;
	raw_data[1] = speed;
	initSpi();
	transfer(raw_data);
	endSpi();
	return 0;*/
	int input_speed;
	int command;
	int xcoord = 0;
	int ycoord = 0;
	printf("Commands:\n 1: STOP\n 2:FORWARD\n 3:REVERSE\n 4:LEFT\n 5:REFT\n 6:MOVE(NOT IMPLEMENTED)\n")
	printf("Choose command 1-6:\n");
	scanf("%d\n", &command);
	printf("Set Speed -100-100:\n");
	scanf("%d\n", &input_speed);
	uint8_t uspeed;
	uspeed = (uint8_t)input_speed;
	switch(command) {
		case 1 :
			SendStop();
		case 2 :
			SendForward(uspeed);
		case 3 :
			SendReverse(uspeed);
		case 4 :
			SendLeft(uspeed);
		case 5 :
			SendRight(uspeed);
		case 6 :
			SendMove(uspeed, xcoord, ycoord);

		default :
			return 0:
			break;
	}

}
