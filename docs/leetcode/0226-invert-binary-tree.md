---
title: Invert Binary Tree
tags: [Tree, Depth-First Search, Breadth-First Search, Recursion]
---

# Invert Binary Tree

## Problem

Given the root of a binary tree, invert the tree by swapping its left and right children at each node. The function should return the root of the inverted tree.

## Approach

The solution uses a standard recursive approach. At each node, the left and right children are swapped. This process is then recursively applied to the left and right subtrees until all nodes have been processed. If the root is `None` (an empty tree), `None` is returned. The root node is returned at the end of the recursion.

## Solution

```python
"""
1. standard recurssion, at each node swap the lest and right nodes and call the fun in a loop until it is done for every node
2. return the root node at end of recurrsion
3. if root is none, return none as per testcase

time comp:- O(N)
space comp:- O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left , root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```

## Complexity

- **Time:** O(N) — Each node in the tree is visited exactly once.
- **Space:** O(N) — In the worst case (a skewed tree), the recursion depth can be equal to the number of nodes.
