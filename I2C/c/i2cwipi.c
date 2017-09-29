#include <wiringPiI2C.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int init(){
	if(wiringPiI2CSetup(0x1e) == -1){
		printf("Init error\n");
	}
	
	wiringPiI2CWriteReg8 (0x1e, 0x3C, 0x0070) ;
	wiringPiI2CWriteReg8 (0x1e, 0x3C, 0x01A0) ;

	return 1;
}
int readi2c(){
	
	wiringPiI2CWriteReg8 (0x1e, 0x3C, 0x0201) ;
	usleep(6000); 
	wiringPiI2CWriteReg8 (0x1e, 0x3D, 0x06) ;
	int data = wiringPiI2CReadReg8 (0x1e, 0x3D) ;
	
	printf("data: %i\n", data);
	
	
	return 1;
}
int main(){
	init();
	//readi2c();
	return 0;
}