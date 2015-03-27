#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int> > generate(int numRows) {
        vector<vector<int> > res(numRows);
	for (int i = 0; i < numRows; i++)
	    res[i].push_back(1);
	for (int i = 1; i < numRows; i++) {
	    for (int j = 1; j < i; j++) {
		res[i].push_back(res[i-1][j-1] + res[i-1][j]);
	    }
	    res[i].push_back(1);
	}
	return res;
    }
};

int main(int argc, char *argv[])
{
    Solution so;
    auto res = so.generate(9);
    for (auto l: res) {
	for (auto i: l)
	    cout<<i<<" ";
	cout<<endl;
    }
    return 0;
}
