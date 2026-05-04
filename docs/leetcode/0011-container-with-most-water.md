---
title: Container With Most Water
tags: [Array, Two Pointers]
---

# Container With Most Water

## Problem

Given an array representing the heights of vertical lines, find two lines that, along with the x-axis, form a container holding the maximum amount of water. The container cannot be slanted.

## Approach

The approach uses two pointers, one starting at the beginning of the array and the other at the end. The area is calculated by taking the minimum height of the two pointers multiplied by the distance between them. The pointer pointing to the shorter line is then moved inwards, as moving the pointer for the taller line would not increase the potential area. This process continues until the pointers meet, keeping track of the maximum area found.

## Solution

```python
"""
The 2 pointer approach

1. a left and right pointer at start and end of list.
2. if len is 2 then return the min of the list
3. else calculate the max qnt of water it can hold by min of left and right multiplied by distance between both
4. if number of left index is smaller than right then inc left else dec right and record and return the max qnt.

time comp:- o(n)
space comp :- o(1) // not using any new list
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        if l == 2:
            return min(height[0], height[1])
        else:
            left = 0
            right = l - 1
            qnt = 0
            while (left < right):
                qnt = max(qnt, ((right-left) * min(height[left], height[right])))
                if height[left] < height[right]:
                    left += 1
                else:
                    right -= 1
        return qnt
```

## Complexity

- **Time:** O(n) - The two pointers traverse the array at most once.
- **Space:** O(1) - No additional data structures are used beyond a few variables.
