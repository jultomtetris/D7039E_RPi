#ifndef SPISENDER_H_
#define SPISENDER_H_

#define BUFFERSIZE 10

int initSpi();
void endSpi();
void transfer(uint8_t *raw_data);


#endif /*SPISENDER_H_*/
