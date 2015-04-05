#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
private:
    static bool cmp(const int a, const int b){
	string sa = to_string(a);
	string sb = to_string(b);
	return sa + sb > sb + sa;
    }
public:
    string largestNumber(vector<int> &num) {
        string res = "";
        sort(num.begin(), num.end(), cmp);
        for (auto i: num)
            res += to_string(i);
        if (res[0] == '0')
            return "0";
        return res;
    }
};

int main(int argc, char *argv[])
{
    vector<int> v = {1};
    Solution so;
    cout<<so.largestNumber(v)<<endl;
    return 0;
}
