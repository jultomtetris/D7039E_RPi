#include <bcm2835.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <unistd.h>
#define LEN 8

uint16_t clk_div = BCM2835_I2C_CLOCK_DIVIDER_2500; 		//Decides clock rate.     2500 = 100KHz, 622 = 399.3610 kHz, 150 = 1.666 MHz, 148 = 1.689 MHz
uint8_t slave_address = 0x1e; 							//Read: 0x3D, 	Write: 0x3C
char buf[LEN];
int i;
uint8_t reason;

int init(){
		if (!bcm2835_init())
    {
      printf("bcm2835_init failed. Are you running as root??\n");
      return 1;
    }
    if (!bcm2835_i2c_begin())
    {
      printf("bcm2835_i2c_begin failed. Are you running as root??\n");
      return 1;
    }
	bcm2835_i2c_setSlaveAddress(slave_address);
    bcm2835_i2c_setClockDivider(clk_div);
	
	//Normal measurement
	char config[2] ={0};
	config[0] = 0x00;
	config[1] = 0x70
	;
	reason = bcm2835_i2c_write(config, 2);
	if(reason == 0x00){
		printf("Success\n");
	}
	if(reason == 0x01){
		printf("Received a NACK\n");
	}
	if(reason == 0x02){
		printf("Received Clock Stretch Timeout\n");
	}
	if(reason == 0x04){
		printf("Not all data is sent / received\n");
	}
	config[0] = 0x01;
	config[1] = 0xA0;
	bcm2835_i2c_write(config, 2);
	//config[0] = 0xA0;
	//bcm2835_i2c_write(config, 1);
	usleep(6000);
	return 0;
}

int readi2c(){
	// Read 6 bytes of data from register(0x03)
	// xMag msb, xMag lsb, zMag msb, zMag lsb, yMag msb, yMag lsb

	char config[2] ={0};
	config[0] = 0x02;
	config[1] = 0x01;
	bcm2835_i2c_write(config, 2);
	usleep(6000); 
	
	char reg[1] = {0x06};
	bcm2835_i2c_write(reg, 1);
	char data[6] ={0};
	if(bcm2835_i2c_read(data, 6) != 6){
		printf("Error : Input/output Error \n");
	}
		//Prints raw data
		for (i=0; i<6; i++) {
			printf("Read Buf[%d] = %x\n", i, data[i]);
		} 
		// Convert the data
		int xMag = (data[0] * 256 + data[1]);
		if(xMag > 32767)
		{
			xMag -= 65536;
		}

		int zMag = (data[2] * 256 + data[3]);
		if(zMag > 32767) 
		{
			zMag -= 65536;
		}

		int yMag = (data[4] * 256 + data[5]);
		if(yMag > 32767) 
		{
			yMag -= 65536;
		}

		// Output data to screen
		printf("Magnetic field in X-Axis : %d \n", xMag);
		printf("Magnetic field in Y-Axis : %d \n", yMag);
		printf("Magnetic field in Z-Axis : %d \n", zMag);
		
	
	
	/*
	for (i=0; i<LEN; i++)buf[i] = 'n';
	data = bcm2835_i2c_read(buf, LEN);
	printf("Read Result = %d\n", data);   
	for (i=0; i<LEN; i++) {
		if(buf[i] != 'n') printf("Read Buf[%d] = %x\n", i, buf[i]);
	} 
	*/
	
	//char reg[1] = {0x03};
	//bcm2835_i2c_write(reg, 1);
	//usleep(67000);
	
	return 0;	
}

int end(){
	bcm2835_i2c_end();   
    bcm2835_close();
	return 0;
}

int main(){
	init();
	readi2c();
	end();
	return 0;
}