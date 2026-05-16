---
title: Maximum Subarray
description: "Given an array of integers, find the contiguous subarray with the largest sum and return its sum."
tags: [Arrays, Hashing]
---

# Maximum Subarray

## Problem

Given an array of integers, find the contiguous subarray with the largest sum and return its sum.

## Approach

The author initially considered a sliding window approach, similar to finding the maximum substring, using greedy pointers. However, this approach was found to be unsuitable. The problem is better solved using Kadane's algorithm.

Kadane's algorithm maintains two variables: `current` and `maximum`. Both are initialized with the first element of the array. The `current` variable tracks the maximum sum ending at the current position, deciding whether to extend the current subarray or start a new one. For each element, `current` is updated by taking the maximum of the current element itself or the sum of the current element and the previous `current` sum. The `maximum` variable keeps track of the overall largest sum encountered so far, updating itself with the `current` sum if `current` is larger. The algorithm returns `maximum` after iterating through the entire array.

## Solution

```python
"""
1. I was trying to do the sliding window technique, similar to max substring, using greedy to slide the left and right pointers.
2. But that dosent work, and for problem like this we need kadence algorithm

3. current and maximum starts at first index, current determines if it needs to continue with the subarray or start fresh
4. max(nums[i], nums[i]+current) for -50 2 5, at -2 it choose max(2, -48), it will choose 2
5. maximum records the max current, and returns it and end of loop.

time comp:- O(N)
space comp:- O(1)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        maximum = nums[0]
        for i in range(1, len(nums)):
            current = max(nums[i], current+nums[i])
            maximum = max(maximum, current)
        return maximum
```

## Complexity

- **Time:** O(N) — The algorithm iterates through the array once.
- **Space:** O(1) — The algorithm uses a constant amount of extra space for variables.
