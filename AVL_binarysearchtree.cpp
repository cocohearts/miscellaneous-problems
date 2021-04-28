#include <iostream>
#include <string>
using namespace std;


template <typename T>
class Node {
public:
    T value;
    int height;
    Node * left_child;
    Node * right_child;
    Node(T val) {
        value = val;
        left_child = NULL;
        right_child = NULL;
        height = 0;
    }

    static int get_height(Node *ptrNode);
};

template <typename T>
class AVLTree {
public:
    Node<T> * root;

    AVLTree() {
        root = NULL;
    }
    
    Node<T>* my_insert(Node<T>* root, T val);

    void insert(T val);

    Node<T>* left_rotate(Node<T> * node);

    Node<T>* right_rotate(Node<T> * node);

    string my_print(Node<T> * pNode);

    void update_height(Node<T> * root);
};

template <typename T>
int Node<T>::get_height(Node<T> *ptrNode) {
    if (ptrNode == NULL) {
        return -1;
    }
    return ptrNode->height;
}

template <typename T>
void AVLTree<T>::update_height(Node<T>* root) {
    root->height = 1+max(Node<T>::get_height(root->left_child), Node<T>::get_height(root->right_child));
}

template <typename T>
Node<T>* AVLTree<T>::my_insert(Node<T>* root, T val) {
    if (root==NULL) {
        Node<T>* pNewnode = new Node<T>(val);
        return pNewnode;
    }
    if (root->value > val) {
        root->left_child = my_insert(root->left_child,val);
    }
    else {
        root->right_child = my_insert(root->right_child,val);
    }
    update_height(root);
    if (Node<T>::get_height(root->left_child)>Node<T>::get_height(root->right_child)+1) {
        if (val<root->left_child->value) {
            return right_rotate(root);
        }
        else {
            root->left_child = left_rotate(root->left_child);
            return right_rotate(root);
        }
    }
    if (Node<T>::get_height(root->right_child)>Node<T>::get_height(root->left_child)+1) {
        if (val>root->right_child->value) {
            return left_rotate(root);
        }
        else {
            root->right_child = right_rotate(root->right_child);
            return left_rotate(root);
        }
    }
    return root;
}

template <typename T>
void AVLTree<T>::insert(T val) {
    root = my_insert(root, val);
}

template <typename T>
Node<T>* AVLTree<T>::right_rotate(Node<T> * node) {
    Node<T> *left = node->left_child;
    Node<T> *leftright = left->right_child;
    left->right_child = node;
    node->left_child = leftright;
    update_height(node);
    update_height(left);
    return left;
}


template <typename T>
Node<T>* AVLTree<T>::left_rotate(Node<T> * node) {
    Node<T> *right = node->right_child;
    Node<T> *rightleft = right->left_child;
    right->left_child = node;
    node->right_child = rightleft;
    update_height(node);
    update_height(right);
    return right;
}

template <typename T>
string AVLTree<T>::my_print(Node<T> * pNode) {
    if (pNode == NULL) {
        return "";
    }
    return my_print(pNode->left_child)+" "+to_string(pNode->value)+" "+my_print(pNode->right_child);
}

int main() {
    AVLTree<int> myTree;
    myTree.insert(10);
    myTree.insert(15);
    myTree.insert(20);
    myTree.insert(30);
    myTree.insert(18);
    myTree.insert(35);
    myTree.insert(40);
    
    cout<<myTree.my_print(myTree.root)<<endl;
}