// https://oj.leetcode.com/problems/two-sum/

// Given an array of integers, find two numbers such that they add up to a
// The function twoSum should return indices of the two numbers such that they add
// up to the target, where index1 must be less than index2. Please note that your
// You may assume that each input would have exactly one solution.
// Input: numbers={2, 7, 11, 15}, target=9
// Output: index1=1, index2=2

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        unordered_map<int, int> map;
        vector<int> res;
        for (int i = 0; i < numbers.size(); i++) {
            map[numbers[i]] = i;
        }
        for (int i = 0; i < numbers.size(); i++) {
            int t = target - numbers[i];
            // ensure not the same one
            if (map.find(t) != map.end() && map[t] > i) {
                res.push_back(i+1);
                res.push_back(map[t]+1);
                return res;
            }
        }
        return vector<int> {-1, -1};
    }
};
int main(int argc, char *argv[])
{

    return 0;
}
