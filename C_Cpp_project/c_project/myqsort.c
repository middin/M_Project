#include <stdio.h>
#include <stdlib.h>

int comp(const void *a, const void *b)
{
  return *(int*)a-*(int*)b;
}

int main()
{
  int i = 0;
  int *array;
  int n;

  printf("输入排序个数：\n");
  scanf("%d", &n);
  array = (int*)malloc(n*sizeof(int));

  for(;i<n;i++)
  {
    scanf("%d", (array+i));
  }

  qsort(array, n, sizeof(int), comp);
  printf("排序后的结果为：\n");
  for(i=0; i<n; i++)
  {
    printf("%d\t", array[i]);
  }
  return 0;
}