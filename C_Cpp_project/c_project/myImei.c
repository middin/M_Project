#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void chartou8(char *data, int len, char *resultbuf)
{
  int i, step = 2;
  char tmp[8];
  memset(tmp, 0x00, sizeof(tmp));

  for(i = 0; i < len/2; i++)
  {
    memcpy(tmp, data+i*step, step);
    resultbuf[i] = (unsigned char)(strtol(tmp, NULL, 16) & 0xffff);
    printf("resultbu[%d] = %02x\n", i, resultbuf[i]);
  }
  return;
}
int main()
{
  char buffer[8];
  char tempbuf[8];
  char IMEI[] = "352736081611975";
  chartou8(IMEI, strlen(IMEI)+1, buffer);
  sprintf(tempbuf,"%02x%02x%02x%02x%02x%02x%02x%x0", buffer[0], buffer[1], buffer[2], buffer[3], buffer[4], buffer[5], buffer[6], buffer[7]);
  printf("%s\n", tempbuf);
  printf("%d\n", sizeof(tempbuf));
}