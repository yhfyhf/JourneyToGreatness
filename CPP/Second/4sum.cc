// https://oj.leetcode.com/problems/4sum/

// Given an array S of n integers, are there elements a, b, c, and d in S such
// that a + b + c + d = target? Find all unique quadruplets in the array which
// Note:
// Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤
// The solution set must not contain duplicate quadruplets.
//     For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
//     A solution set is:
//     (-1,  0, 0, 1)
//     (-2, -1, 1, 2)
//     (-2,  0, 0, 2)

#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;
/*
  1. sort the num array
  
  2. build a hashtable, key as sum of each two numbers, value as a array, store
  the index pair of the two numbers which may sum as key. (cache, O(n^2))
  
  3. to ensure order, iterate i, j in increasing order and search
  target-num[i]-num[j] in cache, if found, make sure it's indexes are bigger than
  j, then added to result (warning: this process may introduce replicates)
  the indexes order: i < j < k.first < k.second

  4. remvoe duplicate
  
 */

class Solution {
public:
    vector<vector<int> > fourSum(vector<int> &num, int target) {
        int n = num.size();
		vector<vector<int> > res;
		if (n < 4)
			return res;
		sort(num.begin(), num.end());
		unordered_map<int, vector<pair<int, int> > > cache;
		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++)
				cache[num[i]+num[j]].push_back(make_pair(i, j));
		
		for (int i = 0; i < n - 3; i++) {
			// skip duplicate first element
			if (i != 0 && num[i] == num[i-1])    continue;
			for (int j = i+1; j < n - 2; j++) {
				// skip duplicate second element
				if (j != i+1 && num[j] == num[j-1])    continue;
				int key = target - num[i] - num[j];
				// not found
				if (cache.find(key) == cache.end())    continue;
				auto &sum2 = cache[key];
				for (int k = 0; k < sum2.size(); k++) {
					if (sum2[k].first <= j)  // diff
						continue;
					res.push_back({num[i], num[j], num[sum2[k].first], num[sum2[k].second]});
				}	
			}
		}
		//sort(res.begin(), res.end());
		res.erase(unique(res.begin(), res.end()), res.end());
		return res;
    }
};

int main(int argc, char *argv[])
{
	vector<int> v = {-3,-2,-1,0,0,1,2,3};
	Solution s;
	vector<vector<int> > res = s.fourSum(v, 0);
	for (int i = 0; i < res.size(); i++) {
		for (int j = 0; j < res[i].size(); j++)
			cout<<res[i][j]<<" ";
		cout<<endl;
	}
    return 0;
}
