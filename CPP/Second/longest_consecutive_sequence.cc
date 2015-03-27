#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int> &num) {
        unordered_set<int> set;
        for (auto i: num)
            set.insert(i);
        int res = 0;
        for (auto i: num) {
            if (set.find(i) != set.end()) {
                int len = 0;
                int r = i, l = i - 1;
                while(set.find(r) != set.end()) {
                    len++;
                    set.erase(r++);
                }
                while(set.find(l) != set.end()) {
                    len++;
                    set.erase(l--);
                }
                res = max(res, len);
            }
        }
        return res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
