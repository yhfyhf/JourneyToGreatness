// https://oj.leetcode.com/problems/candy/

// There are N children standing in a line. Each child is assigned a rating value.

// You are giving candies to these children subjected to the following requirements:

// Each child must have at least one candy.
// Children with a higher rating get more candies than their neighbors.
// What is the minimum candies you must give?

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int candy(vector<int> &ratings) {
        int n = ratings.size();
        if (n == 1)
            return 1;
        int res = 0;
        vector<int> candies(n, 1);
        for (int i = 0; i < n - 1; i++) {
            if (ratings[i] < ratings[i+1] && candies[i] >= candies[i+1])
                candies[i+1] = candies[i] + 1;
        }
        for (int i = n - 1; i > 0; i--) {
            if(ratings[i] < ratings[i-1] && candies[i-1] <= candies[i])
                candies[i-1] = candies[i] + 1;
        }

        for (auto e: candies)
            res += e;
        return res;
    }
};
int main(int argc, char *argv[])
{

    return 0;
}
