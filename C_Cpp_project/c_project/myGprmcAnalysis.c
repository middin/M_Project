#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
  char gprmc[]="$GNRMC,130631.000,A,2233.47239,N,11353.48314,E,0.001,0.00,120619,,,A*4E";
  char fmt[] = "%*[^,],%*[^,],%[^,],%lf,%c,%lf,%c,%s";
  char buffer[50];
  double lat=0.0, lon=0.0,hdop=0.0, altitude=0.0;
  char flag_lat = 0, flag_lon = 0;
  int satlite_num = 0;
  int valid_flag = 0;

  char valid[2];

  if(6 != sscanf(gprmc, fmt, valid, &lat, &flag_lat, &lon, &flag_lon, buffer))
  //if(4 != sscanf(gprmc, fmt, &valid_flag, &lat, &flag_lat, &lon, &flag_lon, buffer))
  {
    printf("error\n");
  }

  printf("valid = %s\n", valid);
  printf("lat = %f\n", lat);
  printf("flag_lat = %c\n", flag_lat);
  printf("lon = %f\n", lon);
  printf("flag_lon = %c\n", flag_lon);


  char gpgsa[]="GPGSA,A,3,13,15,199,193,02,29,05,195,194,30,,,1.70,1.00,1.37,1*1F";
  char *p = gpgsa;
  char cnt = 0;

  for(int i=0; i<sizeof(gpgsa)-1;i++)
  {
    if(*(p+i) == ',')
    {
      cnt++;
      printf("i = %d, cnt = %d\n", i, cnt);
    }
  }
  printf("cnt = %d\n", cnt);
  return 0;
}