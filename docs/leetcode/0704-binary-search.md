---
title: Binary Search
description: "Given a sorted array of integers, find the index of a given target value."
tags: [Arrays, Binary Search]
---

# Binary Search

## Problem

Given a sorted array of integers, find the index of a given target value. If the target is not present in the array, return -1. The algorithm must have a time complexity of O(log n).

## Approach

_(approach inferred from code — author notes were empty)_

The solution uses a standard binary search algorithm. It maintains two pointers, `left` and `right`, representing the boundaries of the search space. In each iteration, it calculates the middle index, compares the element at the middle index with the target, and narrows down the search space by adjusting `left` or `right` accordingly. The loop continues until the `left` pointer crosses the `right` pointer, indicating that the target is not found.

## Solution

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            mid = (left+right)//2
            if target == nums[mid] :
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1

        return -1
```

## Complexity

- **Time:** O(log n) — The search space is halved in each iteration.
- **Space:** O(1) — Constant extra space is used for the pointers and mid variable.
