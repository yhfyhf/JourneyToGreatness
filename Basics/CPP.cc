#include <iostream>
using namespace std;

#define SIZE 50

class Person {
    int id;
    char name[SIZE];

public:
    virtual void aboutMe() {
	cout << "I am a person.";
    }
    ~Person() {
	cout << "Delete a person." << endl;
    }
};

class Student : public Person {
public:
    void aboutMe() {
	cout << "I am a student." << endl;
    }
}; 

temlate <class T>
class ShiftedList {
    T* array;
    int offset, size;
public:
    ShiftedList(int sz): offset(0), size(sz) {
	array = new T[size];
    }
    
    ~ShiftedList() {
	delete [] array;
    }
    
    void shiftBy(int n) {
	offset = (offset + n) % size;
    }

    T getAt(int i) {
	return array[convertIndex(i)];
    }

    void setAt(T item, int i) {
	array[convertIndex(i)] = item;
    }

private:
    int convertIndex(int i) {
	int index = (i - offset) % size;
	while (index < 0) index += size;
	return index;
    }
};


void String_find(string s) {
    
}

int main(int argc, char *argv[])
{
    Student stu;
    stu.aboutMe();
    /* ------------------------------- */
    int size = 4;
    ShiftedList<int> * list = new ShiftedLIst<int> (size);
    for (int i = 0; i < size; i++) {
	list->setAt(i, i);
    }
    cout << list->getAt(0) <<endl;
    
    return 0;
}

