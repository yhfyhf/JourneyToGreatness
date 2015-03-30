#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    void reverseWords(string &s) {
        int idx = 0;
        // clean: strip left spaces, right spaces, 
        // more than one spaces between words
        for (int i = 0; i < s.size(); i++) {
            if (s[i] != ' ' || (idx && s[idx-1] != ' ')) 
                s[idx++] = s[i];
        }
        // now, the last character is s[idx-1]
        if (idx && s[idx-1] == ' ')
            idx--;
        s.resize(idx);
        
        // reverse
	// why this ? because iterator cannot 相加想减
        int start = 0;
        for (int i = start+1; i < s.size(); i++) {
            if (s[i] == ' ') {
                reverse(s.begin()+start, s.begin()+i);
                start = i+1;
            }
        }
        reverse(s.begin() + start, s.end());
        reverse(s.begin(), s.end());        
    }
};

int main(int argc, char *argv[])
{
    Solution so;
    string s = "a";
    so.reverseWords1(s);
    cout<<s<<endl;
    return 0;
}
