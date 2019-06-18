#include <stdio.h>
#include <stdlib.h>

//创建socket用到
#include <sys/types.h>
#include <sys/socket.h>

#include <netdb.h>

//struct sockadd_in 使用
#include <netinet/in.h>

#include <arpa/inet.h>

#include <unistd.h>

int main()
{
  // 创建
  int sockId = -1;
  sockId = socket(AF_INET, SOCK_STREAM, 0);
  if(sockId > 0)
  {
    printf("sockId = %d\n", sockId);
  }

  // 域名解析
  char hostname[]="auth.mqtt.9iot.cn";
  //char hostname[] = "a1yjksbBsf6.iot-as-mqtt.cn-shanghai.aliyuncs.com";
  //char hostname[] = "www.baidu.com";
  struct hostent *h;
  h = gethostbyname(hostname);
  if(h != NULL)
  {
    printf("%s\n", h->h_name);
    printf("%d - %d\n", h->h_addrtype, h->h_length);
    printf("%s - %s\n", h->h_addr_list[1], h->h_aliases[0]);
    printf("%d:%d:%d:%d\n", h->h_addr[0], h->h_addr[1], h->h_addr[2], h->h_addr[3]);
  }

  char addrBuf[14];
  sprintf(addrBuf, "%d.%d.%d.%d", h->h_addr[0], h->h_addr[1], h->h_addr[2], h->h_addr[3]);
  printf("addrBuf = %s\n", addrBuf);

  // 连接
  int connectRet = 0;
  struct sockaddr_in servadd;
  servadd.sin_family = AF_INET;
  servadd.sin_port = htons(1883);
  //servadd.sin_addr.s_addr = inet_addr(addrBuf);
  servadd.sin_addr=*((struct in_addr *)h->h_addr);

  printf("%d\n", servadd.sin_addr.s_addr);
  connectRet = connect(sockId, (struct sockaddr *)&servadd, sizeof(servadd));
  printf("connectRet = %d\n", connectRet);
  
  if(connectRet < 0)
  {
    printf("connect error\n");
  }
  else if(connectRet == -2)
  {
    printf("wouldblock\n");
  }
  printf("%d\n", servadd.sin_addr.s_addr);
  close(sockId);
  
  return 0;
}