#include <iostream>
#include <string>
#include <stack>
using namespace std;

class Solution {
private:
    double eval(double first, double second, char op) {
	switch (op) {
	case '+':
	    return first + second;
	case '-':
	    return first - second;
	case '*':
	    return first * second;
	case '/':
	    return first / second;
	}
	return 0;
    }
    double ston(string num) {
	reverse(num.begin(), num.end());
	return stod(num);
    }
public:
    double parse(string s) {
	stack<double> Number;
	stack<char> Oper;
	string buff;
	// parsing string
	for (int i = s.size() -1; i >= 0; --i) {

	    if ((s[i] >= '0' && s[i] <= '9') || s[i] == '.')
		buff += s[i];
	    else {
		if (!buff.empty()) {

		    Number.push(ston(buff));
		    buff.clear();
		}
		if (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/') {

		    if (Oper.empty() || Oper.top() == '+' || Oper.top() == '-') {
			Oper.push(s[i]);
		    }
		    else {
			double first = Number.top();
			Number.pop();
			double second = Number.top();
			Number.pop();
			char op = Oper.top();
			Oper.pop();
			double tmp = eval(first, second, op); 
			Number.push(tmp);
			Oper.push(s[i]);
		    }
		}
	    }
	} // end for
	if (!buff.empty())
	    Number.push(ston(buff));
	while (!Oper.empty()) {
	    double first = Number.top();
	    Number.pop();
	    double second = Number.top();
	    Number.pop();
	    char op = Oper.top();
	    Oper.pop();
	    double tmp = eval(first, second, op);
	    Number.push(tmp);
	}
	double res =  Number.top();
	Number.pop();
	return res;
    }
};

int main(int argc, char *argv[])
{
    Solution so;
    string p = "6-3.5*2+7.3";
    cout<<"Answer:"<<so.parse(p)<<endl;
    return 0;
}
