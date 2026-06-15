---
title: Search In Rotated Sorted Array
description: Find a target value in a sorted array that has been rotated at an unknown pivot point.
tags: [Binary Search, Arrays]
---

# Search In Rotated Sorted Array

## Problem

Given an array of distinct integers that was originally sorted in ascending order and then possibly rotated at an unknown pivot, find the index of a given target value. If the target is not present, return -1. The algorithm must run in O(log n) time.

## Approach

The problem can be solved using a modified binary search. The key idea is that in a rotated sorted array, at least one half of the array (from left to mid, or from mid to right) must be sorted. We can use this property to determine which half to search in.

First, we perform a standard binary search. If the middle element is the target, we return its index. If not, we check which half of the array is sorted.

If the left half (from `left` to `mid`) is sorted (i.e., `nums[left] <= nums[mid]`), we then check if the `target` falls within this sorted range (`nums[left] <= target < nums[mid]`). If it does, we search the left half by setting `right = mid - 1`. Otherwise, the target must be in the right half, so we set `left = mid + 1`.

If the left half is not sorted, it implies the right half (from `mid` to `right`) is sorted. We then check if the `target` falls within this sorted range (`nums[mid] < target <= nums[right]`). If it does, we search the right half by setting `left = mid + 1`. Otherwise, the target must be in the left half, so we set `right = mid - 1`.

If the `while` loop completes without finding the target, it means the target is not in the array, and we return -1.

## Solution

```python
"""
1. you can run a liner search for o(n), for o(logn), its a midified binary search.
2. if the array is rotated first part of array is sorted or 2nd part is sorted like [4,5,6,7,|0,1,2,3], 2 part of the array.
3. doing a normal bs, if the value is mid return else, if num is left is < num in mid that means first part of array is sorted, check if values is in btw these if it is run a bs btw left and mid-1, else move left to mid+1.
4. If the array is not sorted till left to mid in cases like [6,7,0,1,2,3,4], such case array of right part would be sorted, check if the value is in that part of array if not move the right to mid-1 to check on left part of array.
5. if not found return, for array with 2 nums [3,1] mid would be 3 left would be 3, so nums[left] <= nums[mid]. Return -1 if not found.

Time comp:- O(logn)
space comp:- O(1)
"""
class Solution:
    def search(self, nums: List[int], value: int) -> int:
        l = len(nums)
        left = 0
        right = l-1
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == value:
                return mid
            # First part of array is sorted    
            elif nums[left] <= nums[mid]:
                if nums[left] <= value < nums[mid]:
                    right = mid - 1
                else:
                    left = mid+1
            # right part of array is sorted
            else:
                if nums[mid] < value <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1

        return -1
```

## Complexity

- **Time:** O(log n) — The algorithm performs a binary search, dividing the search space in half at each step.
- **Space:** O(1) — The algorithm uses a constant amount of extra space for variables.
