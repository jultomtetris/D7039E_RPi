#include "SpiSender.h"
#include <bcm2835.h>
#include <stdio.h>
#include "../utils/Cobs.h"

int initSpi(){
	if (!bcm2835_init()){
		printf("bcm2835_init failed. Are you running as root?\n");
			return 1;
		}
		if (!bcm2835_spi_begin()){
			printf("bcm2835_spi_begin failed. Are you running as root?\n");
			return 1;
		}
		bcm2835_spi_setBitOrder(BCM2835_SPI_BIT_ORDER_MSBFIRST);      // The default
		bcm2835_spi_setDataMode(BCM2835_SPI_MODE0);                   // The default
		bcm2835_spi_setClockDivider(BCM2835_SPI_CLOCK_DIVIDER_65536); // The default
		bcm2835_spi_chipSelect(BCM2835_SPI_CS0);                      // The default
		bcm2835_spi_setChipSelectPolarity(BCM2835_SPI_CS0, LOW);      // the default
	return 0;
}
void endSpi(){
	bcm2835_spi_end();
	bcm2835_close();
}

void transfer(uint8_t *raw_data){
	uint8_t send_data[BUFFERSIZE+2];
	//uint8_t unstuffed_data[BUFFERSIZE+2];
	//printf("size:%d\n", sizeof(raw_data));
	stuffData(raw_data, BUFFERSIZE, send_data); //sending to COBS
	size_t send_size = BUFFERSIZE+2; //determining size for the for-loop
	//unStuffData(send_data, 3, unstuffed_data);
	//printf("unstuffed:%d\n", unstuffed_data[1]);
	for(int i = 0; i < send_size; ++i){
		uint8_t read_data = bcm2835_spi_transfer(send_data[i]); //sends data, byte by byte over spi
		printf("test: %d\n", read_data);
		printf("encoded: %d\n", send_data[i]);
	}
}
