---
title: Lowest Common Ancestor of a Binary Search Tree
description: "Find the lowest common ancestor (LCA) of two given nodes, `p` and `q`, in a Binary Search Tree (BST)."
tags: [Tree, Depth-First Search, Binary Search Tree, Binary Tree]
---

# Lowest Common Ancestor of a Binary Search Tree

## Problem

Find the lowest common ancestor (LCA) of two given nodes, `p` and `q`, in a Binary Search Tree (BST). The LCA is the deepest node that has both `p` and `q` as descendants, where a node can be a descendant of itself.

## Approach

If the current root node is `p`, `q`, or null, it's returned. Otherwise, the function recursively searches the left and right subtrees. If both recursive calls return non-null values (meaning `p` and `q` were found in different subtrees), the current root is the LCA. If only one subtree returns a non-null value, that returned node is the LCA.

## Solution

```python
"""
1. if the root is p or q or root dosent exist return root
2. the returned root is true which mean p and q matched, return the root or parent of it
3. if both didnt match only one did, return the matched node

time comp:- O(N)
space:- O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        if left:
            return left
        
        return right
```

## Complexity

- **Time:** O(N) - In the worst case, we might visit every node in the tree.
- **Space:** O(N) - Due to the recursion stack, which can be proportional to the height of the tree (which is N in the worst case for a skewed tree).
