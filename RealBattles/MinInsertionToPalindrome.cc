#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// http://www.geeksforgeeks.org/dynamic-programming-set-28-minimum-insertions-to-form-a-palindrome/
int findMinInsert(string str) {
    int n = str.size();
    vector<vector<int> > tab(n, vector<int>(n, 0));
    int l, h, gap;
    for (gap = 1; gap < n; ++gap) {
	for (l = 0, h = gap; h < n; ++l, ++h) {
	    tab[l][h] = (str[l] == str[h]) ? tab[l+1][h-1]: min(tab[l][h-1], tab[l+1][h]) + 1;
	}
    }

    for (int i = 0; i < n; i++) {
	for (int j = 0; j < n; j++) {
	    cout<<tab[i][j]<<" ";
	}
	cout<<endl;
    }
    return tab[0][n-1];
}

int main(int argc, char *argv[])
{
    string a = "geeks";
    cout<<findMinInsert(a)<<endl;
    return 0;
}

