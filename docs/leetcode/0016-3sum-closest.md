---
title: 3Sum Closest
description: "Given an array of integers, find three distinct numbers whose sum is as close as possible to a given target value."
tags: [Sorting, Two Pointers]
---

# 3Sum Closest

## Problem

Given an array of integers, find three distinct numbers whose sum is as close as possible to a given target value. Return the sum of these three numbers.

## Approach

This problem is similar to the 3Sum problem. We start by sorting the input array. Then, we iterate through the array, fixing one element at a time. For each fixed element, we use two pointers (left and right) to find the remaining two elements. We initialize the closest sum found so far with the sum of the first three elements in the sorted array. During the two-pointer traversal, if the current sum is equal to the target, we return it immediately. Otherwise, if the absolute difference between the current sum and the target is smaller than the current closest difference, we update the closest sum. If the current sum is less than the target, we increment the left pointer to increase the sum; otherwise, we decrement the right pointer to decrease the sum.

## Solution

```python
"""
1. similar to the prev 3-sum problem
2. one fixed var and a left and right pointer, sort the array to begin with and get the sum of min 3 elements as a baseline
3. for fixed from 0 to n-2, if the sum is equal to target best match return the target or curr_sum
4. if the diff btw the curr sum and target is lower than ans then replace ans with curr sum.
5. if the sum is grater than target dec right else inc left, return the final ans

time comp:- O(n^2)
space comp:- O(1)
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)

        nums.sort()
        ans = nums[0] + nums[1] + nums[2]

        for fixed in range(n - 2):
            left = fixed + 1
            right = n - 1

            while left < right:
                curr_sum = nums[fixed] + nums[left] + nums[right]
                if curr_sum == target:
                    return curr_sum

                if abs(curr_sum - target) < abs(ans - target):
                    ans = curr_sum

                if curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return ans
```

## Complexity

- **Time:** O(n^2) — Sorting takes O(n log n), and the nested loops (outer loop for `fixed` and inner `while` loop for `left` and `right` pointers) take O(n^2). The dominant factor is O(n^2).
- **Space:** O(1) — We are modifying the input array in-place for sorting, and the additional space used for variables is constant.
