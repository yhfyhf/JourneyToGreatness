#include <iostream>
#include <string>
using namespace std;

string removeVowel(string str) {
    const string VOWELS = "aeiouAEIOU";
    string res;
    for (auto c: str) {
	if (VOWELS.find(c) == string::npos) {
	    res += c;
	}
    }
    return res;
}

bool isVowel(char c) {
    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
	|| c == 'A' || c == 'e' || c == 'I' || c == 'O' || c == 'U')
	return true;
    return false;
}
char* removeVowel2(char* string) {
    int n = strlen(string);
    char *res = new char [n];
    int idx = 0;
    for (int i = 0; i < n; i++) {
	if (isVowel(string[i]))
	    continue;
	res[idx++] = string[i];
    }
    res[idx] = '\0';
    return res;
}

int main(int argc, char *argv[])
{
    string s = "All copied elements are accessed.";
    char* ss = "All copied elements are accessed.";
    cout<<removeVowel(s)<<endl;
    cout<<removeVowel2(ss)<<endl;
    return 0;
}

