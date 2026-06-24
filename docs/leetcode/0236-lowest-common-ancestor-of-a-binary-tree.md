---
title: Lowest Common Ancestor of a Binary Tree
description: Find the deepest node shared by two given nodes in a binary tree.
tags: [Tree, Depth-First Search, Binary Tree]
---

# Lowest Common Ancestor of a Binary Tree

## Problem

Given a binary tree, identify the lowest common ancestor (LCA) for two specified nodes. The LCA is defined as the deepest node in the tree that has both target nodes as descendants, where a node is considered a descendant of itself.

## Approach

We utilize a depth-first search (DFS) approach. The recursive function checks if the current node is one of the target nodes (`p` or `q`). If it is, we return the node itself. Otherwise, we recursively search the left and right subtrees. If both the left and right recursive calls return a non-null node (meaning `p` and `q` were found in different subtrees), the current node is the LCA. If only one of the recursive calls returns a node, that node is returned upwards. If neither finds a target node, `None` is returned.

## Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return None
            if root == p or root == q:
                return root
            
            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                return root
            
            if right:
                return right
            else:
                return left
        
        return dfs(root)
```

## Complexity

- **Time:** O(N) — We visit each node in the tree at most once.
- **Space:** O(N) — In the worst case (a skewed tree), the recursion depth can be N.
