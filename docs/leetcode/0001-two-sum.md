---
title: Two Sum
tags: [Arrays, Sorting, Two Pointers]
---

# Two Sum

## Problem

Given an array of integers, find the indices of two numbers that add up to a specific target value. Each input is guaranteed to have exactly one solution, and the same element cannot be used twice. The order of the returned indices does not matter.

## Approach

_(approach inferred from code — author notes were empty)_

The approach involves sorting the input array to efficiently find the two numbers. After sorting, two pointers are used, one at the beginning and one at the end of the sorted array. The sum of the numbers pointed to by these pointers is compared to the target. If the sum is greater than the target, the right pointer moves inwards; if it's less, the left pointer moves inwards. When the sum equals the target, the original indices of these numbers are found in the unsorted array and returned. Special care is taken to find the correct indices if the two numbers are the same.

## Solution

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        len_num = len(nums)
        i = 0
        j = len_num - 1
        while i < j:
            s = sorted_nums[i] + sorted_nums[j]
            if s > target:
                j = j - 1
            elif s < target:
                i = i + 1
            else:
                val_i, val_j = sorted_nums[i], sorted_nums[j]
                ind_i = nums.index(val_i)
                ind_j = nums.index(val_j, ind_i + 1) if val_i == val_j else nums.index(val_j)
                return [ind_i, ind_j]
```

## Complexity

- **Time:** O(n log n) — dominated by the initial sorting of the array. The two-pointer traversal takes O(n) time. Finding indices using `list.index()` can take O(n) in the worst case, but since it's done at most twice and the numbers are found efficiently after sorting, it doesn't increase the overall complexity beyond O(n log n).
- **Space:** O(n) — if the space for the sorted array is considered. If sorting is done in-place (which `sorted()` in Python does not do), the space complexity could be O(1) for the pointers.
