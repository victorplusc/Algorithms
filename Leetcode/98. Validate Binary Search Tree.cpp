/**
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#include <iostream>
#include <stack>

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        std::stack<TreeNode *> s;
        TreeNode *curr = root;
        int prevData;
        bool initPrev = false;
        
        while (curr != NULL || s.empty() == false)
        {
            while (curr != NULL){
                s.push(curr);
                curr = curr->left;
            }
            
            curr = s.top();
            s.pop();
            
            if (initPrev == false){
                prevData = curr->val;
                initPrev = true;
            }
            else {
                if(curr->val <= prevData){
                    return false;
                }
                prevData = curr->val;
            }
                
            curr = curr->right;   
        }
        return true;
    }
};
