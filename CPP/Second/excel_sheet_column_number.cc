#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        int res = 0;
        for (auto c: s) {
            res = res*26 + (c - 'A' + 1);
        }
        return res;
    }
};




int main(int argc, char *argv[])
{

    return 0;
}
