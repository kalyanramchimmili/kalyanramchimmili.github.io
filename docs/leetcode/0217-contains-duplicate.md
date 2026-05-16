---
title: Contains Duplicate
description: "Given an array of integers, determine if any number appears more than once."
tags: [Arrays, Hashing]
---

# Contains Duplicate

## Problem

Given an array of integers, determine if any number appears more than once. If a duplicate exists, return `true`; otherwise, return `false`.

## Approach

The approach uses a hash map (dictionary in Python) to count the occurrences of each number in the input array. If, during iteration, any number's count exceeds one, it signifies a duplicate, and the function immediately returns `true`. If the entire array is processed without finding any number with a count greater than one, it means all elements are distinct, and the function returns `false`.

## Solution

```python
"""
1. A hashmap count to cound the instances
2. if count is greater than 1 for any number in nums, return true
3. if the loop is completed, it exits then return False as there is duplicate

Time comp:- O(N), N being number of int in nums
Space comp:- O(N), hashmap space
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
            if count[i] > 1:
                return True
            
        return False
```

## Complexity

- **Time:** O(N) — We iterate through the array once. Hash map operations (insertion and lookup) take average O(1) time.
- **Space:** O(N) — In the worst case, if all elements are distinct, the hash map will store all N elements.
