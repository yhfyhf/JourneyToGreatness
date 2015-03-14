#include <iostream>
using namespace std;

bool isGray(char a, char b) {
    char x = (a ^ b);
    // important
    if (x == 0)
	return false;
    return (x&(x-1)) == 0;
}

int main(int argc, char *argv[])
{
    char a = 0x0f, b = 0x5f;
    cout<<isGray(a, b)<<endl;
    return 0;
}

