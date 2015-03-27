// https://oj.leetcode.com/problems/powx-n/

// Implement pow(x, n).

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
private:
    double _pow(double x, int n) {
        if (n == 0)
            return 1;
        double v = _pow(x, n/2);
        if (n % 2)
            return v * v * x;
        else
            return v * v;
    }
public:
    double pow(double x, int n) {
        if (n < 0)
            return 1.0 / _pow(x, -n);
        return _pow(x, n);
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
