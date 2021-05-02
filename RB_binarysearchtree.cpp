#include <iostream>
#include <string>
#include <vector>
using namespace std;

template <typename T>
class RBNode {
public:
    T value;

    RBNode<T>* left;
    RBNode<T>* right;
    RBNode<T>* parent;
    bool red;

    RBNode(T val=NULL);
};

template <typename T>
class RBTree {
public:
    RBNode<T>* root;
    RBTree();
    RBNode<T>* my_insert(RBNode<T>* root, T val);
    void insert(T val);
    RBNode<T>* right_rotate(RBNode<T> * node);
    RBNode<T>* left_rotate(RBNode<T> * node);
    string my_print(RBNode<T>* pNode);
    bool getred(RBNode<T>* pNode);
};

template <typename T>
RBNode<T>::RBNode(T val) {
    value = val;
    red = true;
    left = NULL;
    right = NULL;
    parent = NULL;
}

template <typename T>
bool RBTree<T>::getred(RBNode<T>* pNode) {
    if (pNode == NULL) {
        return false;
    }
    return pNode->red;
}

template <typename T>
RBTree<T>::RBTree() {
    root = NULL;
}

template <typename T>
RBNode<T>* RBTree<T>::right_rotate(RBNode<T> * node) {
    RBNode<T> *the_left = node->left;
    RBNode<T> *the_leftright = node->left->right;
    the_left->right = node;
    node->left = the_leftright;
    return the_left;
}

template <typename T>
RBNode<T>* RBTree<T>::left_rotate(RBNode<T> * node) {
    RBNode<T> *the_right = node->right;
    RBNode<T> *the_rightleft = node->right->left;
    the_right->left = node;
    node->right = the_rightleft;
    return the_right;
}


template <typename T>
void RBTree<T>::insert(T val) {
    root = my_insert(root, val);
    root->red = false;
}


template <typename T>
RBNode<T>* RBTree<T>::my_insert(RBNode<T>* my_root, T val) {
    RBNode<T>* child;
    if (my_root == NULL) {
        RBNode<T>* newnode = new RBNode<T>(val);
        return newnode;
    }
    if (getred(my_root->left) && getred(my_root->right)) {
        //prelimianary color changing
        my_root->left->red = false;
        my_root->right->red = false;
        my_root->red = true;
    }
    if (my_root->value > val) {
        //inserting on left
        if (my_root->left == NULL) {
            //left is empty
            RBNode<T>* newnode = new RBNode<T>(val);
            my_root->left = newnode;
            return my_root;
        }
        my_root->left = my_insert(my_root->left, val);
        if (my_root->left->red) {
            if (getred(my_root->left->left)) {
                //left left
                my_root->left->red = false;
                my_root->red = true;
                return right_rotate(my_root);
            }
            else if (getred(my_root->left->right)) {
                //left right
                my_root->left = left_rotate(my_root->left);
                my_root->left->red = false;
                my_root->red = true;
                return right_rotate(my_root);
            }
        }
    }
    else {
        //inserting on right
        if (my_root->right == NULL) {
            RBNode<T>* newnode = new RBNode<T>(val);
            my_root->right = newnode;
            return my_root;
        }
        my_root->right = my_insert(my_root->right, val);
        if (my_root->right->red) {
            if (getred(my_root->right->right)) {
                //right right
                my_root->right->red = false;
                my_root->red = true;
                return left_rotate(my_root);
            }
            else if (getred(my_root->right->left)) {
                //right left
                my_root->right = right_rotate(my_root->right);
                my_root->right->red = false;
                my_root->red = true;
                return left_rotate(my_root);
            }
        }
    }
    if (getred(my_root->left) && getred(my_root->right)) {
        //prelimianary color changing
        my_root->left->red = false;
        my_root->right->red = false;
        my_root->red = true;
    }
    return my_root;
}

template <typename T>
string RBTree<T>::my_print(RBNode<T> * pNode) {
    if (pNode == NULL) {
        return "";
    }
    string returned = my_print(pNode->left)+" "+to_string(pNode->value)+" "+my_print(pNode->right);
    return returned;
}

int main() {
    RBTree<int> newtree;
    vector<int> v = {76, 81, 74, 44, 51, 93, 18, 15, 32, 91,  8, 56, 33, 29, 41, 78, 28,
       99,  0, 34, 72, 39, 48, 98, 55, 64,  9, 94, 58, 27, 85, 38, 97, 11,
       31, 63, 13, 23, 22, 46, 26, 16,  2, 10, 47, 54, 95, 83, 73, 20, 50,
       52, 25, 87, 71, 90, 43,  3, 82, 77, 36, 14,  7, 35, 67, 12, 19, 80,
       68, 79, 69, 24, 40, 65, 89, 70, 45, 53, 60, 88, 92, 21, 62, 66, 49,
       30,  6, 37,  4,  5, 96, 57, 59, 84, 86, 42, 75, 61, 17,  1};
    for (int i : v) {
        newtree.insert(i);
    }

    cout<<newtree.my_print(newtree.root)<<endl;
    return 0;
}