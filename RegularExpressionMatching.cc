#include <iostream>

using namespace std;

/* Idea stolen from Rob Pike's code
 * http://www.cs.princeton.edu/courses/archive/spr10/cos333/beautiful.html
 */
class Solution {
public:
    bool isMatch(const char *s, const char *p) {
		char *text = (char *)s;
		char *regexp = (char *)p;
		return match(regexp, text);
		
    }
	bool match(char *regexp, char *text) {
		if (regexp[0] == '\0')
			return *text == '\0';
		if (regexp[1] == '*')
			return matchStar(regexp[0], regexp+2, text);
		if (*text != '\0' && (regexp[0] =='.' || regexp[0] == *text))
			return match(regexp+1, text+1);
		return false;
	}


	bool matchStar(int c, char *regexp, char *text) {
		do {
			if (match(regexp, text))
				return true;
		} while(*text != '\0' && (*text++ == c || c == '.'));
		return false;
	}
	
};

int main(int argc, char *argv[])
{
	Solution so;
	cout<<so.isMatch("aa","aa")<<endl;

	cout<<so.isMatch("aa","a")<<endl;
	cout<<so.isMatch("aa","aa")<<endl;
	cout<<so.isMatch("aaa","aa")<<endl;
	cout<<so.isMatch("aa","a*")<<endl;
	cout<<so.isMatch("aa",".*")<<endl;
	cout<<so.isMatch("ab",".*")<<endl;
	cout<<so.isMatch("aab","c*a*b")<<endl;


    return 0;
}
