#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    // consider corner case first
    string convertToTitle(int n) {
        string res;
        while (n > 0) {
	    // first trap, n-- here, consider 26
            n--;
	    // second trap, (char) here, otherwise cannot add
	    res = (char)((n % 26) + 'A') + res;
	    n /= 26;
        }
        return res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
