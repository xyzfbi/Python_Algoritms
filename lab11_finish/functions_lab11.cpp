//
// Created by layk1i on 27.05.25.
//
#include <cmath>
#include "functions_lab11.h"

#include <iostream>
#include <climits>


TreeNode *insertNode(TreeNode *root, int value) {
    if (!root) {
        return new TreeNode(value);
    }
    if (value < root->data) {
        root->left = insertNode(root->left, value);
    }
    else {
        root->right = insertNode(root->right, value);
    }
    return root;
}


void PrintInOrder(TreeNode *root) {
    if (!root) {
        return;
    }
    PrintInOrder(root->left);
    std::cout << root->data << " ";
    PrintInOrder(root->right);
}
int FindMin(TreeNode *root) {
    if (!root) {
        return INT_MIN;
    }
    if (!root->left) {
        return root->data;
    }
    return FindMin(root->left);
}
int FindMax(TreeNode *root) {
    if (!root) {
        return INT_MAX;
    }
    if (!root->right) {
        return root->data;
    }
    return FindMax(root->right);
}
void FindClosest(TreeNode *root, double targ, int &closest, double &min_diff) {
    if (!root) {
        return;
    }
    double diff = std::abs(root->data - targ);
    if (diff < min_diff) {
        min_diff = diff;
        closest = root->data;
    }
    FindClosest(root->left, targ, closest, min_diff);
    FindClosest(root->right, targ, closest, min_diff);
}
void FreeMemory(TreeNode *root) {
    if (!root) {
        return;
    }
    FreeMemory(root->left);
    FreeMemory(root->right);
    delete root;
}

double PowRecursion(double x, int n) {
    if (n == 0)
        return 1;
    else if (n < 0) {
        return 1/PowRecursion(x, std::abs(n));
    }
    else {
        return x * PowRecursion(x, n - 1);
    }
}

double PowIteration(double x, int n) {
    if (n == 0)
        return 1;

    double result = 1.0;
    int power = std::abs(n);
    for (int i = 0; i < power; ++i) {
        result *= x;
    }
    if (n < 0) {
        return 1.0 / result;
    }
    else {
        return result; // x * pow (x, n-1) = result
    }
}