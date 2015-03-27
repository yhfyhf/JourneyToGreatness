#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0, j = 0;
        for(;i < s.size(); i++)
            if (isalnum(s[i]))
                s[j++] = s[i];
        for(i = 0; i < --j; i++) {
            if (tolower(s[i]) != tolower(s[j]))
                return false;
        }
        return true;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
