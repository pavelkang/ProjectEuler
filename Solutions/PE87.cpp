#include <iostream>
#include <math.h>
using namespace std;

bool isPrime(int x) {
  if ( x<=1 ) {
    return false;}
  if ( x==2 ) {
    return true;}
  int s = (int) pow(x,0.5);
  for ( int i=2; i<=s; i++ ) {
    if ( x%i == 0) {
      return false;}
  }
  return true;
}


int main () {
 
  double limit = 50000000.0;
  int forthLimit = (int) pow(limit, 0.25);
  int count = 0;
  for (int c=2; c<= 84; c++) {
    if (isPrime(c)) {
      // the third element is here.
      double remain_first = limit - pow(c, 4.0) ;
      int cubeLimit = (int) pow(remain_first, .3333333) ;
      for (int b=2; b< cubeLimit; b++) {
	if (isPrime(b)) {
	  // the second element is here.
	  double remain_second = remain_first - pow(b,3.0);
	  int squareLimit = (int) pow(remain_second, 0.5) ;
	  for (int a=2; a< squareLimit; a++) {
	    if (isPrime(a)) {
	      if ( pow(a,2) + pow(b,3) + pow(c,4) < limit) {
		count++;}
	    }
	  }
	}
      }
    }
  }
  cout << count << endl;

  return 0;
}
