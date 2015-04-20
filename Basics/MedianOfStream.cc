#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;
// https://ronzii.wordpress.com/2012/03/30/median-in-a-stream-of-numbers/

/*
  maxHeap: 堆顶是最小的 存较大的一半数
  minHeap: 堆顶是最大的 存较小的一半数
 */
void insert(priority_queue<int, vector<int>, less<int> > &maxHeap,
	    priority_queue<int, vector<int>, greater<int> > &minHeap, int n) {
    
    if (maxHeap.size() == minHeap.size()) {
	//  
	if (!minHeap.empty() && n > minHeap.top()) {
	    maxHeap.push(minHeap.top());
	    minHeap.pop();
	    minHeap.push(n);
	}
	else
	    maxHeap.push(n);
    }
    else {
	// maxHeap size 比 minHeap 大 1，往 minHeap 里放
	// 比median 小,
	if (n < maxHeap.top()) {
	    minHeap.push(maxHeap.top());
	    maxHeap.pop();
	    maxHeap.push(n);
	}
	else
	    minHeap.push(n);
    }
}
double getMedian(priority_queue<int, vector<int>, less<int> > maxHeap,
		 priority_queue<int, vector<int>, greater<int> > minHeap) {
    int a = minHeap.size();
    int b = maxHeap.size();
    if(a==0 && b==0) return -1;
    if((a+b)%2==0)
        return (double)(minHeap.top() + maxHeap.top())/2;
    else
        return maxHeap.top();
}
int main()
{
    priority_queue<int> maxHeap;
    priority_queue<int,vector<int>, greater<int> > minHeap;
    int a[] = {7,11,17,8,19,2,3,15,16};
    int n = sizeof(a)/sizeof(a[0]);
    for(int i=0; i<n; i++)
    {
        insert(maxHeap,minHeap,a[i]);
        cout<<getMedian(maxHeap,minHeap)<<endl;
    }
    return 0;
}
