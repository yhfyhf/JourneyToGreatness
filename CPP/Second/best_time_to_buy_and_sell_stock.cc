#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int> &prices) {
        if (prices.size() <= 1)
            return 0;
        int low = prices[0], res = 0;
        for (int i = 1; i < prices.size(); i++) {
            res = max(res, prices[i] - low);
            low = min(low, prices[i]);
        }
        return res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
