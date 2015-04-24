#include <iostream>
using namespace std;

class Singleton {
private:
    // private construct function
    Singleton() {};
    // private copy constructor
    Singleton(Singleton const&){}; 
    // static variable share among objecs
    static Singleton *instance;
    
public:
    static Singleton* getInstance() {
	// whether it's the first time to call
	if (instance == NULL)
	    instance = new Singleton();
	return instance;
    }
    
};



int main(int argc, char *argv[]) {
    Singleton *p1 = Singleton::getInstance();
    //CSingleton *p2 = CSingleton::getInstance();

    cout<<p1<<" "<<endl;
    return 0;
}
