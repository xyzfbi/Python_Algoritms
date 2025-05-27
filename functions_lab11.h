//
// Created by layk1i on 27.05.25.
//

#ifndef FUNCTIONS_LAB11_H
#define FUNCTIONS_LAB11_H
struct TreeNode {
    int data;
    TreeNode *left;
    TreeNode *right;
    explicit TreeNode(int v) : data(v), left(nullptr), right(nullptr) {}
};

double PowRecursion(double x, int n);
double PowIteration(double x, int n);
TreeNode *insertNode(TreeNode *root, int value);
void PrintInOrder(TreeNode *root);
int FindMin(TreeNode *root);
int FindMax(TreeNode *root);
void FindClosest(TreeNode *root, double targ, int &closest, double &min_diff);
void FreeMemory(TreeNode *root);



#endif //FUNCTIONS_LAB11_H
