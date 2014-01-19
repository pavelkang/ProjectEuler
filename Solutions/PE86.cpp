#include <iostream>
#include <math.h>
using namespace std;

int f(int M) {
  int number = 0;
  for (int a=1;a<=M;a++) {
    for (int b=1;b<=a;b++) {
      for (int c=1;c<=b;c++) {
	  double result = (b+c)*(b+c) + a*a;
	  double s = sqrt(result) ;
	    if (s == (int)(s)) {
	      number++;
	    }
	}
    }
  }
  return number;
}

int main() {
  cout << "The answer is " << f(1810) << endl;
  return 0;
}
