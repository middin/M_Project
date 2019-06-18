#include <stdio.h>
#include <stdlib.h>

int main()
{
  char lang[]="2233.47295";
  printf("lang = %s\n", lang);

  double lan = 0;
  lan = (double)atof(lang);
  printf("lan = %lf\n", lan);

  char *str = "113.29464653";
  double d = strtod(str,NULL);
  printf("d=%f\n",d);

  char szOrbits[] = "365.24 29.53";
  char * pEnd;
  double d1, d2;
  d1 = strtod (szOrbits,&pEnd);
  d2 = strtod (pEnd,NULL);
  printf ("The moon completes %.2f orbits per Earth year.\n", d1/d2);

  unsigned char temp[4];
  unsigned int la;
  la = d*1000000;
  printf("la = %d\n", la);
  temp[0] = (la>>24);
  temp[1] = (la>>16);
  temp[2] = (la>>8);
  temp[3] = (la);
  printf("%02x %02x %02x %02x\n", temp[0], temp[1], temp[2], temp[3]);
  printf("%d %d %d %d\n", temp[0], temp[1], temp[2], temp[3]);


#if 0
  char str1[55] = "84612.60";
  float ff;
  ff=(float)atof(str1);
  printf("str:%s\n",str1);
  printf("%f\n",atof(str1));
  printf("2=%f\n",&ff);
#endif

  return 0;
}