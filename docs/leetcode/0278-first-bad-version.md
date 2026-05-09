---
title: First Bad Version
tags: [Binary Search, API]
---

# First Bad Version

## Problem

Given the total number of versions of a product and an API that checks if a version is bad, find the first version that is bad. All versions after a bad version are also bad. You must minimize the number of API calls.

## Approach

The author initially tried a linear search, but it resulted in a Time Limit Exceeded error. They then switched to a binary search approach. If the middle version is bad, it might be the first bad version, or the first bad version could be before it. If the middle version is not bad, then the first bad version must be after it. The search continues until the left pointer is no longer less than the right pointer. The final `left` value represents the first bad version. For the edge case where `n` is 1, the `while` loop condition `left < right` is immediately false, and `left` (which is 1) is correctly returned.

## Solution

```python
"""
1. running a linear search didnt work, TLE
2. used binary search for this, if the mid is bad then mid could be the first bad version or previous to mid
3. if mid is not bad, then it should be from mid+1 to n
4. calculate new mid check if it is bad until left < right
5. return left, for n==1 the while would break and return left directly which is 1

time comp:- O(logn)
space comp :- O(1)
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1

        return left
```

## Complexity

- **Time:** O(log n) — Binary search halves the search space with each API call.
- **Space:** O(1) — Constant space is used, as only a few variables are needed for the pointers.
