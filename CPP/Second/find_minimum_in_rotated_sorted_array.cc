
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    /*
     Time O(kn), space O(1)
     */
    void rotate(int nums[], int n, int k) {
        if (k >= n)
            k %= n;
        for (int i = 0; i < k; i++) {
            int tmp = nums[n-1];
            for (int j = n-1; j > 0; j--)
                nums[j] = nums[j-1];
            nums[0] = tmp;
        }
    }
    
};

int main(int argc, char *argv[])
{

    return 0;
}
