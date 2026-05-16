---
title: Median of Two Sorted Arrays
description: "Given two sorted arrays, find the median of the combined sorted array."
tags: [Arrays, Sorting]
---

# Median of Two Sorted Arrays

## Problem

Given two sorted arrays, find the median of the combined sorted array. The median is the middle element if the total number of elements is odd, or the average of the two middle elements if the total number is even. The solution should aim for a logarithmic time complexity.

## Approach

_(approach inferred from code — author notes were empty)_

The approach involves merging the two input arrays into a single sorted array. Once the combined array is sorted, the median is calculated by checking if the length of the merged array is even or odd. If it's odd, the median is the element at the middle index. If it's even, the median is the average of the two elements surrounding the middle.

## Solution

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #nums1.extend(nums2)
        #nums1.sort()

        nums = sorted(nums1 + nums2)
        l1 = len(nums)
        if l1%2 == 0:
            return (nums[l1//2-1]+nums[l1//2])/2
        else:
            return nums[l1//2]
```

## Complexity

- **Time:** O((m+n) log (m+n)) — Dominated by sorting the merged array of size m+n.
- **Space:** O(m+n) — To store the merged array.
