// http://alrightchiu.github.io/SecondRound/binary-tree-traversalxun-fang.html

#include <iostream>
#include <string>
#include <queue>

using namespace std;

class TreeNode{
public:
    TreeNode *leftchild, *rightchild;
    TreeNode *parent;
    string str;

    TreeNode():leftchild(0),rightchild(0),parent(0),str(""){};
    TreeNode(string s):leftchild(0),rightchild(0),parent(0),str(s){};

    friend class BinaryTree;
};

class BinaryTree{
public:
    TreeNode *root; //起點

    BinaryTree():root(0){};
    BinaryTree(TreeNode *node):root(node){};

    void Preorder(TreeNode *current); //VLR
    void Inorder(TreeNode *current);
    void Postorder(TreeNode *current);
    void Levelorder();
};


int main(){
    TreeNode *nodeA = new TreeNode("A");
    TreeNode *nodeB = new TreeNode("B");
    TreeNode *nodeC = new TreeNode("C");
    TreeNode *nodeD = new TreeNode("D");
    TreeNode *nodeE = new TreeNode("E");
    TreeNode *nodeF = new TreeNode("F");
    TreeNode *nodeG = new TreeNode("G");
    TreeNode *nodeH = new TreeNode("H");
    TreeNode *nodeI = new TreeNode("I");

    nodeA->leftchild = nodeB; nodeA->rightchild = nodeC; 
    nodeB->leftchild = nodeD; nodeB->rightchild = nodeE; 
    nodeE->leftchild = nodeG; nodeE->rightchild = nodeH; 
    nodeC->leftchild = nodeF; nodeF->rightchild = nodeI;

    BinaryTree T(nodeA);
    T.Preorder(T.root);
    cout<<endl;
    T.Inorder(T.root);
    cout<<endl;
    T.Postorder(T.root);
    cout<<endl;
    
    T.Levelorder();
    cout<<endl;


    // cout<<"test"<<endl;
    return 0;
}

// C++ code
void BinaryTree::Preorder(TreeNode *current){
    if (current) {                          // if current != NULL
        cout << current->str << " ";   // V
        Preorder(current->leftchild);       // L
        Preorder(current->rightchild);      // R
    }
}

void BinaryTree::Inorder(TreeNode *current){
    if(current){
        Inorder(current->leftchild); // L
        cout << current->str << " "; // V        
        Inorder(current->rightchild); // R
    }
}

void BinaryTree::Postorder(TreeNode *current){
    if(current){
        Postorder(current->leftchild);       // L
        Postorder(current->rightchild); // R
        cout << current->str << " "; // V
    }
}

void BinaryTree::Levelorder(){
    queue<TreeNode *> q;
    q.push(this->root); // start from root, and push in queue

    while(!q.empty()){ // if queue is not empty, means some node has NOT visited
        
        TreeNode *current = q.front();
        q.pop();
        cout<< current->str << " "; //visited

        if(current->leftchild != NULL){ // leftchild has something, push into queue
            q.push(current->leftchild);
        }

        if(current->rightchild != NULL){ // rightchild has something, push into queue
            q.push(current->rightchild);   
        }
    }
}


// compile c++
// g++ tree.cpp -o tree 
// tree

// g++ tree.cpp -o tree && tree

// g++ tree.cpp && a


