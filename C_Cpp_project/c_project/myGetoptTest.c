#include <stdio.h>
#include <stdlib.h>

#include <unistd.h>

int main(char argc, char *argv[])
{
  extern char *optarg;
  extern int optind, opterr, optopt;
  int opt=0;
  while ((opt = getopt(argc, argv, "Nb:e:B")) != -1){
    printf("opt = %c\n", opt);
    switch(opt)
    {
      case 'b':
      {
        printf("option parameter is b\n");
      }
      break;

      case 'e':
      {
        printf("option parameter is e, value is %s\n", optarg);
      }
      break;

      default:
      break;
    }
  }
  if(optind < argc)
  {
      printf("argv[%d] = %s\n", optind, argv[optind]);
      printf("argc = %d\n", argc);
  }
    
  return 0;
}