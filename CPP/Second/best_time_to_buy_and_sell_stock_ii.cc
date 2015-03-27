#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int n = prices.size();
        if (n <= 1)    return 0;
        int res = 0;
        for (int i = 1; i < n; i++) {
            if (prices[i] > prices[i-1])
                res += prices[i] - prices[i-1];
        }
        return res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
