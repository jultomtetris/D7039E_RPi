#include <stdio.h>
#include <wiringPiSPI.h>

int channel = 0;
int speed = 25000000;
unsigned char databuffer[32] = "Test";
int len = 32;

void initSPI(int channel, int speed){
	printf("Initializing SPI...\n");

	if(wiringPiSPISetup(channel, speed) < 0){
		printf("Could not initialize SPI\n");
	}else{
		printf("Init SPI Done\n");
	}
}

void testSPIRW(int channel,  unsigned char *data, int len){
	printf("Sending test data\n");
	int ret = wiringPiSPIDataRW(channel, data, len);
	if(ret < 0){
		printf("SPI transmission failed\n");
	}else{
		printf ("Data recieved: %s \n", data);
	}
}

int main(void){
	initSPI(channel, speed);
	testSPIRW(channel, databuffer, len);
	return 0;
}