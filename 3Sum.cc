#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void printV (vector<int> vv) {
	for(int i = 0; i < vv.size(); i++) {
		cout << vv[i]<< " ";
	}
	cout<<endl;
}

/*
  Duplicate dectection here is the time consuming part, to avoid that, use some pruning
  0-1 backpack also has duplicate detection problem
 */
class Solution {
public:
    vector<vector<int> > threeSum(vector<int> &num) {
		vector<vector<int> > ans;
		int len = num.size();
		if (len <= 2)
			return ans;		
		sort(num.begin(), num.end()); 
		for(int k = 0; k < len - 2; k++) {
			// Start from negative number
			if (num[k] > 0)
				break;			
			int l = k+1, r = len - 1;
			while (l < r) {
				// if first two num's sum > 0
				//cout<<"l:"<<num[l]<<" r:"<<num[r]<<" k:"<<num[k]<<endl;
				if (num[k] + num[l] > 0)
					break;
				
				if (num[k] + num[l] + num[r] > 0)
					r--;
				else if (num[k] + num[l] + num[r] < 0)
					l++;
				else {
					int cur[] = {num[k], num[l], num[r]};
					ans.push_back(vector<int>(cur, cur+3));
					l++, r--;					
					// pruning, skip duplicated l, r in postion[1], [2]
					while(l<r && num[l] == num[l-1]) l++;
					while(l<r && num[r] == num[r+1]) r--;
				}
			}			
			// pruning, skip duplicated k in  postion[0]
			while(k < len && num[k] == num[k+1]) k++;
		}
		return ans;
    }

    // More elegant version
    vector<vector<int> > threeSum(vector<int> &num) {
        int n = num.size();
		vector<vector<int> > res;
		sort(num.begin(), num.end());
		if (n < 3)
		    return res;
		for(int i = 0; i < n; ) {
		    int j = i + 1, k = n - 1, s = -num[i], old;
		    while (j < k) {
		        if (num[j] + num[k] < s)
		            j++;
		        else if (num[j] + num[k] > s)
		            k--;
		        else {
		            res.push_back(vector<int>{num[i], num[j], num[k]});
		            old = num[j];
			    // remove duplicate j
		            while (++j < k && num[j] == old);
		            k--;
		        }
		    }
		    // remove duplicated i
		    old = num[i];
		    while (++i < k && num[i] == old);
		}
	    return res;
    }
};




int main(int argc, char *argv[])
{
    Solution so;
	int arr[] = {7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6};
	vector<int> num(arr, arr + sizeof(arr)/sizeof(int));
	vector<vector<int> > k = so.threeSum(num);
	cout<<"print ans:"<<endl;
	for(int i = 0; i < k.size(); i++) { 
		for(int j = 0; j < k[i].size(); j++) {
			cout<<k[i][j]<<" ";
		}
		cout<<endl;
	}
	
    return 0;
}
