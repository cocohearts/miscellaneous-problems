#include <string>
#include <iostream>
#include <vector>

using namespace std;

template <typename T>
class myStack {
public:
    T container[1000];
    int size;
    myStack() {
        size = 0;
    }

    void my_push(T val) {
        size++;
        container[size] = val;
    }
    void my_pop() {
        container[size] = 0;
        size--;
    }
    T my_top() {
        return container[size];
    }
    bool my_empty() {
        return (size == 0);
    }
    int my_size() {
        return size;
    }
};
int main() {
    /*
    myStack<int> my_stack;
    int k = 10;
    for (int i=0; i<k; i++) {
        my_stack.my_push(i);
    }
    cout << my_stack.my_top() << endl;
    cout << std::boolalpha << my_stack.my_empty() << endl;
    my_stack.my_pop();
    cout << my_stack.my_top()<<endl;
     */
    myStack<char> my_stack;
    vector<char> v = {'e','s','p','k'};
    for (int i=0; i<v.size(); i++) {
        my_stack.my_push(v[i]);
    }
    cout << my_stack.my_top() << endl;
    cout << std::boolalpha << my_stack.my_empty() << endl;
    my_stack.my_pop();
    cout << my_stack.my_top()<<endl;
    return 0;
}