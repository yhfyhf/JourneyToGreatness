#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{
    int arr[] = {1,0,0,1,0,1,0,0,1,0};
    int left = 0, right = sizeof(arr)/sizeof(int) - 1;
    while (left < right) {
	while (arr[left] == 0)
	    left++;
	while (arr[right] == 1)
	    right--;
	if (left < right)
	    swap(arr[left], arr[right]);
    }
    for (int i = 0; i < sizeof(arr)/sizeof(int); i++) {
	cout<<arr[i]<<endl;
    }
    return 0;
}
