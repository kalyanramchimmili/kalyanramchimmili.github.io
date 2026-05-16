---
title: Majority Element
description: "Given an array of integers, find the element that appears more than half the time."
tags: [Arrays, Hashing]
---

# Majority Element

## Problem

Given an array of integers, find the element that appears more than half the time. The problem guarantees that such an element always exists.

## Approach

This approach uses a hash map to count the occurrences of each element. As we iterate through the array, we increment the count for each number. If the count of any number exceeds half the length of the array, we return that number. The problem statement ensures a majority element always exists, so we don't need to handle cases where it doesn't.

## Solution

```python
"""
1. similar to ransom note problem, have a count hashmap
2. inc the count, if count of an element is more than half of the list, then return the num
3. as per que there is majority element always hence no need to handle any other case

time comp:- O(N)
space comp:- O(N)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        l = len(nums)//2
        for i in nums:
            count[i] = count.get(i,0) + 1
            if count[i] > l:
                return i
```

## Complexity

- **Time:** O(N) — We iterate through the array once.
- **Space:** O(N) — In the worst case, the hash map might store all unique elements if the majority element is just over half.
