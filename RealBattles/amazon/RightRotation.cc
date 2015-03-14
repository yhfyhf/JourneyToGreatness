#include <iostream>
#include <string>
using namespace std;

bool rightRotation(string s1, string s2) {
    int len = s1.size();
    if(len == s2.size() && len > 0) {
	string tmp = s1 + s2;
	return tmp.find(s2) != string::npos;
    }
    return false;
}

int main(int argc, char *argv[])
{
    string a = "abcdefg", b = "fgabcde";
    cout<<rightRotation(a, b)<<endl;
    return 0;
}

