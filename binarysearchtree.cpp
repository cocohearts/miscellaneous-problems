#include <iostream>
#include <string>
using namespace std;

template <typename T>
class Node {
public:
    T value;
    Node * left_child;
    Node * right_child;
    Node(T val) {
        value = val;
        left_child = NULL;
        right_child = NULL;
    }
    void my_insert(T val);

    string my_print(Node * pNode);
};

template <typename T>
void Node<T>::my_insert(T val) {
    if (value > val) {
        if (left_child != NULL) {
            left_child->my_insert(val);
        }
        else {
            left_child = new Node<T>(val);
            cout<<left_child->value<<endl;
        }
    }
    else {
        if (right_child != NULL) {
            right_child->my_insert(val);
        }
        else {
            right_child = new Node<T>(val);
            cout<<right_child->value<<endl;
        }
    }
}

template <typename T>
string Node<T>::my_print(Node<T> * pNode) {
    if (pNode == NULL) {
        return "";
    }
    string returned = to_string(pNode->value);
    returned += " "+my_print(pNode->left_child)+" "+my_print(pNode->right_child);
    return returned;
}

int main() {
    Node<double> root(10.0);
    root.my_insert(15.0);
    root.my_insert(20.0);
    root.my_insert(18.0);
    root.my_insert(-2.0);
    cout<<root.my_print(&root)<<endl;
}