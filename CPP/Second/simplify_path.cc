// https://oj.leetcode.com/problems/simplify-path/

// Given an absolute path for a file (Unix-style), simplify it.
// For example,
// path = "/home/", => "/home"
// path = "/a/./b/../../c/", => "/c"
// click to show corner cases.
// Corner Cases:
// Did you consider the case where path = "/../"?
// In this case, you should return "/".
// Another corner case is the path might contain multiple slashes '/' together,
// In this case, you should ignore redundant slashes and return "/home/foo".

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    string simplifyPath(string path) {
        string s;
        string curr="";
        // This is important, because we only process current dir when meet '/'
        path.push_back('/');
        for (auto c: path) {
            if (c == '/') {
                if (curr == "." || curr == "")
                    ;
                else if (curr == "..") {
                    if (s.size() > 0)
                        s.erase(s.rfind('/'));
                } else {
                    s += ("/" + curr);
                }
                curr = "";
            }
            else {
                curr += c;
            }
        }
        if (s.empty())
            return "/";
        return s;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
