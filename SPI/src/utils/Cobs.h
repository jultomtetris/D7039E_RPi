#ifndef COBS_H_
#define COBS_H_

#include <stdint.h>
#include <string.h>

void stuffData(uint8_t*, int, uint8_t*);
void unStuffData(uint8_t*, int, uint8_t*);

#endif /* COBS_H_ */
