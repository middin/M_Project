#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int main()
{
  int a[] = {1, 3, -4, 12, 7};
  //sort(a, a+5);
  //sort(a, a+5, greater<int>());
  sort(a, a+5, less<int>());
  for(int i = 0; i<5; i++)
  {
    cout << a[i] << " ";
  }
  cout << endl;

  string str("hello world");
  //sort(str.begin(), str.end());
  sort(str.rbegin(), str.rend()); //反向迭代器
  cout << str << endl;;
  return 0;
}