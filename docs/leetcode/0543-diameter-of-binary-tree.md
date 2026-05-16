---
title: Diameter of Binary Tree
description: "The goal is to find the length of the longest path between any two nodes in a binary tree."
tags: [Tree, Depth-First Search, Binary Tree]
---

# Diameter of Binary Tree

## Problem

The goal is to find the length of the longest path between any two nodes in a binary tree. This path might pass through the root or might not. The length of a path is defined by the number of edges it contains.

## Approach

This approach reuses the concept of calculating the height of a balanced binary tree. A global variable `diameter` is initialized to track the maximum diameter found so far. A helper function `height` is defined, which recursively calculates the height of a subtree. Inside `height`, for each node, it computes the heights of its left and right subtrees. The potential diameter passing through the current node is the sum of these left and right heights. This value is compared with the current maximum `diameter` and updated if it's larger. Finally, the `height` function returns 1 plus the maximum height of its children, effectively calculating the height of the subtree rooted at the current node. The `diameter` is then returned after the `height` function has been called on the root.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def height(node):
            nonlocal diameter

            if node is None:
                return 0

            leftHeight = height(node.left)
            rightHeight = height(node.right)
            diameter = max(diameter, leftHeight+rightHeight)

            return 1+max(leftHeight,rightHeight)
        
        height(root)
        return diameter
```

## Complexity

- **Time:** O(N) — Each node is visited exactly once.
- **Space:** O(h) — In the worst case (a skewed tree), the recursion depth can be O(N). In a balanced tree, it's O(log N).
