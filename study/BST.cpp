#include <iostream>

using namespace std;

struct BstNode {
    int data;
    BstNode* left;
    BstNode* right;
};

// Dynamically creates new node
BstNode* GetNewNode(int data) {
    BstNode* newNode = new BstNode();
    newNode->data = data;
    newNode->left = newNode->right = NULL; 
    return newNode;
}

BstNode* Insert(BstNode* root, int data) {
    
    // If tree is empty
    if (root == NULL) {
        root = GetNewNode(data);
        return root;
    }

    else if (data <= root->data) {
        root->left = Insert(root->left, data); // recursive call to insert data to left subtree
    }

    else {
        root->right = Insert(root->right, data);
    }
    return root;
}

bool Search(BstNode* root, int data) {
    if (root == NULL) return false;
    else if (root->data == data) return true;
    else if (data <= root->data) return Search(root->left, data);
    else return Search(root->right, data);
}

int main() {

    BstNode* root = NULL; // stores address of root node
    root = Inser(root ,15);

    return 0;
}