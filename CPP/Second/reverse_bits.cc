#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            if (n>>i & 1) {
                res |= 1<<(31 - i);
            }
        }
        return res;
    }
};
