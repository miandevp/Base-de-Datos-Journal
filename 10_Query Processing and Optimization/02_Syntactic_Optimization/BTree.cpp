#include<iostream>
#include<vector>

using namespace std;

struct Node{
    bool leaf;
    vector<int> keys;
    vector<Node*> children;

    Node(bool isLeaf){
        leaf = isLeaf;
    }
};

class BTree{
    private:
        Node* root;
    public:
        BTree(){
            root = new Node(true);
        }
};

int main(){
    return 0;
}