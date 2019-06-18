#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
  char name[100];
  char *description;

  strcpy(name, "Zara Ali");

  /*动态分配内存*/
  description = malloc(30*sizeof(char));
  if(description == NULL)
  {
    fprintf(stderr, "Error - unable to allocate required memory\n");
  }
  else
  {
    strcpy(description, "Zara ali a DPS student in class 10th");
  }
  printf("Name = %s\n", name);
  printf("Description: %s\n", description);

#if 0
  strcat(description, "put one's head together");
#else
  description = realloc(description, 50*sizeof(char));
  if(description == NULL)
  {
    fprintf(stderr, "Error\n");
  }
  else
  {
    strcat(description, " put one's head together");
  }
#endif

  printf("new description is : %s\n", description);
  free(description);
  return 0;
}