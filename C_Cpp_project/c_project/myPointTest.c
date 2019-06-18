#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUF_SIZE  20

char buffer[BUF_SIZE];
char length = 0;

void test_point_func(char *buf, int len)
{
  char *p=NULL, *bufTest=NULL;
  p = buffer;
  bufTest = buffer+length;

  strncpy(bufTest, buf, len);
  printf("p = %s, buf=%s, bufTest = %s\n", p, buf, bufTest);
  length += len;
  printf("length = %d\n", length);
}

int main()
{
  char *p=buffer;
  test_point_func("hello\nworld", sizeof("hello\nworld"));
  printf("buffer = %s\n", buffer);
  //test_point_func("world", sizeof("world"));
  printf("p = %s\n", p);
  return 0;
}