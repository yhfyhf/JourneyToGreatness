#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    int maximumGap(vector<int> &num) {
        if (num.size() < 2)
            return 0;
	const int n = num.size();
        int smallest = *min_element(num.begin(), num.end());
        int largest = *max_element(num.begin(), num.end());	
        int gap = (largest - smallest + n - 2) / (n - 1);
        int nbucs = (largest - smallest) / gap + 1;
        
        vector<int> low(nbucs, INT_MAX), up(nbucs, INT_MIN);
        for (auto e : num) {
            int idx = (e - smallest) / gap;
            low[idx] = min(low[idx], e);
            up[idx] = max(up[idx], e);
        }
        int res = 0, p = smallest;
        for (int i = 0; i < nbucs; i++) {
            if (low[i] < INT_MAX) {
                res = max(res, low[i] - p);
                p = up[i];
            }
        }
        return res;
    }
};

int main(int argc, char *argv[])
{
    Solution so;
    vector<int> L = {3, 1, 7, 4, 2};
    cout<<so.maximumGap(L)<<endl;
    return 0;
}
