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
    int threeSumClosest(vector<int> &num, int target) {
	int len = num.size();
	if (num.empty() || len <= 2)
	    return INT_MIN;
	int ans = num[0]+num[1]+num[2]; // due to (num[k] + num[l] > target) pruning
		
	sort(num.begin(), num.end());

	for(int k = 0; k < len - 2; k++) {
	    // Start from negative number
			
	    int l = k+1, r = len - 1;
	    while (l < r) {
		// if first two num's sum > 0
		//cout<<"l:"<<num[l]<<" r:"<<num[r]<<" k:"<<num[k]<<endl;
		int cur_sum = num[k] + num[l] + num[r];
		if (cur_sum > target) {
		    if (abs(cur_sum - target) < abs(ans-target))
			ans = cur_sum;
					
		    r--;
		}
		else if (cur_sum < target) {
		    if (abs(cur_sum - target) < abs(ans-target)) 
			ans = cur_sum;
		    l++;
		}
		else { // find it 
		    return target;
		}

	    }
			
	    // pruning, skip duplicated k in  postion[0]
	    while(k < len && num[k] == num[k+1]) k++;
	}
	return ans;
    }
};




int main(int argc, char *argv[])
{
    Solution so;
    int arr[] = {1,1,1,0};
    vector<int> num(arr, arr + sizeof(arr)/sizeof(int));
    int k = so.threeSumClosest(num,-1000);
    cout<<"print ans:"<<k<<endl;

	
    return 0;
}
