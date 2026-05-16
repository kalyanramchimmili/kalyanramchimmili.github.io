---
title: Maximum Depth of Binary Tree
description: "Given the root of a binary tree, determine the maximum depth."
tags: [Tree, Depth-First Search, Binary Tree]
---

# Maximum Depth of Binary Tree

## Problem

Given the root of a binary tree, determine the maximum depth. The maximum depth is defined as the number of nodes along the longest path from the root to any leaf node.

## Approach

This problem is similar to finding the diameter or checking for a balanced binary tree, as it involves calculating the height of the tree from a given node. A recursive approach is used: for any given node, we recursively calculate the height of its left and right subtrees. The height of the current node is then 1 (for the node itself) plus the maximum height of its left or right subtree. The base case for the recursion is when a node is `None`, in which case its height is 0. The function returns the calculated height from the root.

## Solution

```python
"""
1. similar to diameter or balanced binary tree, find the max height of a tree from node
2. make a height fun for left and right node, return 1+max(left,hight) would give max height of left or right and add in recursive way
3. return the height from node

time comp:- O(N)
space comp:- O(h) - recusive stack
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if node is None:
                return 0
            left = height(node.left)
            right = height(node.right)
            return 1+max(left, right)
        
        return height(root)
```

## Complexity

- **Time:** O(N) — We visit each node in the tree exactly once.
- **Space:** O(h) — Where h is the height of the tree. This is due to the recursive call stack. In the worst case (a skewed tree), h can be N, resulting in O(N) space. In a balanced tree, h is log(N), resulting in O(log N) space.
