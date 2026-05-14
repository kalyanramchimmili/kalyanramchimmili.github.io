---
title: Binary Tree Level Order Traversal
tags: [Tree, BFS, Recursion]
---

# Binary Tree Level Order Traversal

## Problem

Given the root of a binary tree, return the values of its nodes level by level, from left to right. The output should be a list of lists, where each inner list represents a level.

## Approach

This problem can be solved using Breadth-First Search (BFS). We maintain a result list `ans` and a `level` counter. For each level, we append a new empty list to `ans` if it doesn't exist yet. Then, we append the current node's value to the appropriate level's list. We recursively call the BFS function for the left and right children, incrementing the level.

## Solution

```python
"""
1. BFS Problem (Breadth first search). The height of binary tree was DFS.
2. have a res array, level var set at [] and 0 respectively.
3. append a empty [] from level == 1 onwards, to add list within list.
4. append root val if not none, and continue recursively for left and right from the root.
5. Return the ans list.

time comp:- O(N), Each node is visited once.
space comp:- O(N), N:- recursive stack.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        level = 0

        def bfs(root, ans, level):
            if root is None:
                return

            if len(ans) <= level:
                ans.append([])

            ans[level].append(root.val)
            bfs(root.left, ans, level + 1)
            bfs(root.right, ans, level + 1)

        bfs(root, ans, level)
        return ans
```

## Complexity

- **Time:** O(N) — Each node in the tree is visited exactly once.
- **Space:** O(N) — In the worst case (a skewed tree), the recursion stack can go as deep as N.
