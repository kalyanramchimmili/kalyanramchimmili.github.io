---
title: Balanced Binary Tree
tags: [Tree, Depth-First Search, Recursion]
---

# Balanced Binary Tree

## Problem

Determine if a given binary tree is height-balanced, meaning the heights of the two subtrees of every node never differ by more than one. An empty tree is considered balanced.

## Approach

The approach involves defining a helper function to calculate the maximum height of a tree. This height is determined by finding the maximum path from a leaf node to the root. For each node in the main tree, we then recursively calculate the heights of its left and right subtrees. If the absolute difference between these heights is greater than 1 for any node, the tree is not balanced, and we return `False`. This process is repeated for all nodes using recursion.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return 1 + max(left_height, right_height)
```

## Complexity

- **Time:** O(n^2) — For each node, we recalculate the height of its subtrees, leading to repeated computations.
- **Space:** O(n) — Due to the recursion depth, which can be up to the height of the tree in the worst case (a skewed tree).
