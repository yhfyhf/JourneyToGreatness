#include <iostream>
#include <algorithm>

using namespace std;

void  Memcpy(void *dst, void *src, size_t n) {
    char *ddst = (char *) dst;
    char *ssrc = (char *) src;
    while (ssrc) {
	*ddst++ = *ssrc++;
    }
}

void Memcpy2(void *dst, void *src, size_t n) {
    size_t remain = n % 4;
}

int main(int argc, char *argv[])
{
    char a [] = {'a','c','d'};
    char b [3];
    char *pa = a, *pb = b;
    Memcpy(pb, pa, 3);
    for (int i = 0; i < 3; i++)
	cout<<b[i]<<endl;
    return 0;
}

