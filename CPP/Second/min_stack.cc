#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class MinStack {
private:
    stack<int> stk;
    stack<int> m;
public:
    void push(int x) {
        stk.push(x);
        if (m.empty() || x <= m.top())
            m.push(x);
    }

    void pop() {
        if (!stk.empty()) {
            int tmp = stk.top();
            stk.pop();
            if (tmp == m.top()) {
                m.pop();
            }
        }
    }

    int top() {
        if (!stk.empty()) {
            return stk.top();
        }
    }

    int getMin() {
        if (!m.empty()) {
            return m.top();
        }
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
