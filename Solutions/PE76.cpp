#include <iostream>
using namespace std;

int getWays(int n, int m)
{
  //  Returns how many ways to write n as a sum of numbers whose values are at least m
  if ( m > (n/2.0) )
    {
      return 0;
    }
  else
    {
      int result = 1;
      for (int i=m;i<n-m+1;i++)
	{
	  result += getWays(n-m, i);
	}
      return result;
    }
}

int count(int n)
{
  int result = 0;
  for (int i=1;i<n/2+1;i++)
    {
      result += getWays(n,i);
    }
  return result;
}

int main()
{
  cout << "The answer is: " << count(100) << endl;
  return 0;
}
	
