#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;

struct Point {
    int x;
    int y;
    Point() : x(0), y(0) {}
    Point(int a, int b) : x(a), y(b) {}
};
// Lucid and elegant https://leetcode.com/discuss/18590/sharing-my-simple-solution-with-explanation 
class Solution {
public:
    int maxPoints(vector<Point> &points) {
	// Time O(N^2)
        int res = 0;
        unordered_map<double, int> map;
        for (int i = 0; i < points.size(); i++) {
            int samePoints = 1;
            map.clear();
            for (int j = i + 1; j < points.size(); j++) {
                // same point
                if (points[i].x == points[j].x && points[i].y == points[j].y) {
                    samePoints++;
                } // parallel to axis y
                else if (points[i].x == points[j].x) {
                    map[INT_MAX]++;
                } // general case
                else {
                    double slope = (double)(points[j].y - points[i].y) / (double)(points[j].x - points[i].x);
                    map[slope]++;
		    cout<<"slope"<<slope<<endl;
                }
            }
            int currMax = 0;
            for (auto it = map.begin(); it != map.end(); it++) {
                currMax = max(currMax, it->second);
            }
            currMax += samePoints;
            res = max(res, currMax);
        }
        return res;
    }
};

int main(int argc, char *argv[])
{
    vector<Point> v;
    v.push_back(Point(3, 10));
    v.push_back(Point(0, 2));
    v.push_back(Point(0, 3));
    v.push_back(Point(3, 10));
    Solution so;
    cout<<so.maxPoints(v)<<endl;
    return 0;
}
