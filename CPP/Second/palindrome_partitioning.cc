#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
private:
    bool isPali(string s) {
        int start = 0, end = s.size() - 1;
        while (start < end) {
            if (s[start] != s[end])
                return false;
	    start++;
	    end--;
        }
        return true;
    }
public:
    vector<vector<string> > partition(string s) {
	// Time O(2^N), Space O(N)
        vector<string> buff;
        vector<vector<string> > res;
        dfs(s, buff, res, 0);
        return res;
    }
    
    void dfs(const string s, vector<string> &buff, vector<vector<string> > &res, int start) {
        if (start == s.size()) {
            res.push_back(buff);
            return;
        }
        for (int i = start+1; i <= s.size(); i++) {
            if (isPali(s.substr(start, i - start))) {
                buff.push_back(s.substr(start, i - start));
                dfs(s, buff, res, i);
                buff.pop_back();
            } 
        }
    }
};

int main(int argc, char *argv[])
{
    Solution so;
    auto res = so.partition("a");
    for (auto k: res){
	for(auto m: k) {
	    cout<<m<<" ";
	}
	cout<<endl;
    }
    return 0;
}
