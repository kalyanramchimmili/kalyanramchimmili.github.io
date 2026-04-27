---
title: Two Sum
tags: [Arrays, Sorting, Two Pointers]
---

# Two Sum

## Problem

Given an array of integers and a target integer, find the indices of two numbers that add up to the target. It's guaranteed that exactly one solution exists and the same element cannot be used twice.

## Approach

_(approach inferred from code — author notes were empty)_

The approach involves sorting the input array to enable a two-pointer technique. One pointer starts at the beginning of the sorted array, and the other starts at the end. We sum the values at these pointers. If the sum is greater than the target, we move the right pointer inwards; if it's less, we move the left pointer inwards. When the sum equals the target, we find the original indices of these two numbers in the unsorted input array and return them.

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

- **Time:** O(n log n) — dominated by the sorting step. The two-pointer traversal is O(n), and finding indices in the original array can take O(n) in the worst case for each element, but since we only do this once, it's still within the overall O(n log n).
- **Space:** O(n) — for storing the sorted copy of the array. If modifying the input array is allowed, space could be O(1) by sorting in-place and then needing a way to map back to original indices without extra space.
