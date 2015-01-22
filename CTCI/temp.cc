#include <iostream>
using namespace std;

#define NAME_SIZE 50
class Person {
	int id; // private by default
	char name[NAME_SIZE];

    public:
	virtual void aboutMe() {
		cout<< "I am a Person.";
	}
};

class Student : public Person {
    public:
	void aboutMe() {
		cout<< "I am a student.";
	}
};

int main() {
	Student *p = new Student();
	p->aboutMe();
	delete p;
	return 0;
}
