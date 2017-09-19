#include "framework/CmdSys.h"
#include "com/SpiSender.h"
#include <stdio.h>

//#include "CmdSys.h"

#define BUFFERSIZE 10



int main(){
	initSpi();
	int input_speed;
	int command;
	int xcoord = 0;
	int ycoord = 0;
	printf("Commands:\n 1:STOP\n 2:FORWARD\n 3:REVERSE\n 4:LEFT\n 5:REFT\n 6:MOVE(NOT IMPLEMENTED)\n");
	printf("Choose command 1-6:\n");
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
		default :
			return 0;
			break;
	}
	endSpi();
}
