// https://oj.leetcode.com/problems/gas-station/
// There are N gas stations along a circular route, where the amount of gas at
// station i is gas[i].

// You have a car with an unlimited gas tank and it costs cost[i] of gas to
// travel from station i to its next station (i+1). You begin the journey with
// an empty tank at one of the gas stations.

// Return the starting gas station's index if you can travel around the circuit
// once, otherwise return -1.

// Note:
// The solution is guaranteed to be unique.
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
/*
    Because it's unique
*/
class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        int has_solution = 0;
        for (int i = 0; i < gas.size(); i++)
            has_solution += gas[i] - cost[i];
        if (has_solution < 0)
            return -1;
        int start = 0, remain = 0;
        for (int i = 0; i < gas.size(); i++) {
            if (gas[i] + remain >= cost[i]) {
                remain += gas[i] - cost[i];
            }
            else {
                remain = 0;
                start = i+1;
            }
        }
        return start;
    }
};


int main(int argc, char *argv[])
{

    return 0;
}
