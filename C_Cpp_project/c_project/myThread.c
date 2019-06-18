#include <pthread.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

void *th_fun(void *arg)
{
  int *p = (int *)arg;
  printf("thread PID = %d\n", getpid());
  printf("thread ID = %x\n", (unsigned int)pthread_self());
  printf("*arg = %d\n", *p);

}

int main()
{
  pthread_t tid;
  int n = 10;

  // NULL->默认属性    第4个参数为数据
  pthread_create(&tid, NULL, th_fun, (void*)&n);
  
  //pthread_self（） 获取线程调用的id号
  // 主线程里面的phtread_creata返回值tid == 子线程里面的pthread_self() ??
  printf("main htread ID = %x\n", (unsigned int)pthread_self());
  printf("main chicld htread ID = %x\n", (unsigned int)tid);
  printf("main PID = %d\n", getpid());
  //sleep(2);
  while(1);
  
  return 0;
}