#ifndef UARTCOM_H_
#define UARTCOM_H_
//#define BUFFERSIZE 79
int open_serial(const char * portname);
int read_serial(int fd, unsigned char *buffer);
int write_serial(int fd, const char *data)
#endif /*UARTCOM_H_*/
