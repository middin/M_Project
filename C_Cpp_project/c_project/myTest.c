#include <stdio.h>

//校验和取反之后再加0xAA
unsigned char sum8(unsigned char *A, unsigned char n)
{
  unsigned char i;
  unsigned char checksum = 0;
  for(i = 0; i< sizeof(A); i++)
  {
    checksum += A[i];
  }
  checksum = ~checksum + 0xAA;
  return checksum;
}

int main()
{
  char buf[]={0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64};
  printf("%s\n", buf);

  unsigned char A68[] = {0xD6,0xC2,0xD4,0xB6,0x32,0x70,0x68};
  unsigned char A54[] = {0xD6,0xC2,0xD4,0xB6,0x32,0x40,0x54};
  unsigned char checksum = 0;

  checksum = sum8(A68, 7);
  //printf("A68=%d\n", checksum);
  printf("A68=%x\n", checksum);

  checksum = sum8(A54, 7);
  //printf("A54=%d\n", checksum);
  printf("A54=%x\n", checksum);
}