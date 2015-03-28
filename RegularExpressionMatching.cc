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

    // ----------------------------------------------------------------
    // Time O(n), Space O(1)
    bool isMatch2(const char *s, const char *p) {
        if (*p == '\0')
            return *s == '\0';
            
        if (*(p+1) != '*') {
            return (*s == *p || (*p == '.' && *s != '\0')) && isMatch(s+1, p+1);
        }
        else { // meet star
            // one or more match
            while (*s == *p || (*p == '.' && *s != '\0')) {
                if (isMatch(s, p+2))
                    return true;
                // s++标记至少while判断通过，或者匹配更多相同的s
                s++;
            }
            // zero match, 上面的while循环根本进不去
	    cout<<"s:"<<s<<"\tp:"<<p<<endl;
            return isMatch(s, p+2);
        }
    }
	
};

int main(int argc, char *argv[])
{
	Solution so;
	// cout<<so.isMatch("aa","aa")<<endl;

	// cout<<so.isMatch("aa","a")<<endl;
	// cout<<so.isMatch("aa","aa")<<endl;
	// cout<<so.isMatch("aaa","aa")<<endl;
	// cout<<so.isMatch("aa","a*")<<endl;
	// cout<<so.isMatch("aa",".*")<<endl;
	// cout<<so.isMatch("ab",".*")<<endl;
	cout<<so.isMatch2("aab","c*a*b")<<endl;


    return 0;
}
