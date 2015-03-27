// https://oj.leetcode.com/problems/divide-two-integers/

// Divide two integers without using multiplication, division and mod operator.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int divide(int dividend, int divisor) {
        bool neg = false;
	 long dvd = dividend;
	 long dvr = divisor;

        if (dvd < 0) {
            dvd = -dvd; 
            neg = !neg;
        }
        if (dvr < 0) {
            dvr = -dvr;
            neg = !neg;
        }

        long long res = (dvr == 0) ? INT_MAX : 0;
        int times = 0;
        
        while ((dvd>>1) >= dvr) {
            dvr <<= 1;
            times++;
        }
        while (times >= 0) {
            if (dvd >= dvr) {
                res += (1 << times);
                dvd -= dvr;
            }
            dvr >>= 1;
            times--;
        }
	res = neg ? -res : res;
         if (res > INT_MAX || res < -INT_MAX)
             return INT_MAX;
        return res;
    }
};
int main(int argc, char *argv[])
{
    Solution so;
    cout<<so.divide(-1010369383, -2147483648)<<endl;
    cout<<so.divide(-2147483648, 1)<<endl;
    cout<<so.divide(-2147483648, -1)<<endl;
    cout<<"------------"<<endl;
    cout<<INT_MAX<<endl;
    cout<<INT_MIN<<endl;
    cout<<-INT_MAX<<endl;
    return 0;
}
