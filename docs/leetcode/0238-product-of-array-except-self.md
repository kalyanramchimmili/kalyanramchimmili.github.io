---
title: Product Of Array Except Self
description: Compute the product of all elements in an array except for the element at the current index, without using division.
tags: [Arrays, Prefix Sum, Two Pointers]
---

# Product of Array Except Self

## Problem

Given an array of integers, calculate a new array where each element is the product of all other elements in the original array. The solution must achieve this in linear time complexity and avoid using the division operation.

## Approach

The author initially considered a solution using three separate arrays: one for prefix products, one for postfix products, and one for the final result. The prefix array would store the cumulative product of elements from the left, and the postfix array would store the cumulative product from the right. The final result would be the element-wise product of the prefix and postfix arrays.

The optimal approach refines this by using only one result array. First, it populates the result array with the prefix products. Then, it iterates from right to left, multiplying each element in the result array by the corresponding postfix product, which is maintained in a single variable. This avoids the need for explicit prefix and postfix arrays, reducing the space complexity.

## Solution

```python
"""
1. without division operator in o(n) time, intially though of prefix and postfix approach, which works we intialize 3 arrays prefix postfix and res.
2. First compute prefix from range of 1 to l, prefix is prefix[i-1]*nums[i-1]
for n = 1 2 3 4
prefix = 1 1 2 6, for 1 no prefix def to 1, for 2 it is 1 for 3 is 2*1 and for 4 it is 3*2*1
3. similarly for postfix, postfix is postfix[i+1]*nums[i+1], 
for n = 1 2 3 4 -> 4 3 2 1
postfix = 1 4 12 24, start from back for 4 its def 1 as no postfix, for 3 it is prev postfix and nums, so 4 then for 2 it is 4*3 and for 1 it is 12*2.
For result, multiply prefix and postfix and return result multiplying both prefix and postfix.

-> the optimal approach is we dont need prefix and postfix arrays, so we compute the same in res, first put prefix in res and start from opp to multiply with postfix and return the res.
To achieve this we have prefix = 1, postfix = 1, for prefix it is 1, and prefix multiplys with the num so it becomes 1 1 2 6 and then we come from back so 6 2 1 1
-> now 6 multiplies with 1 so 6 and for 2 it mulplies with 4 i.e nums[i] etc gives the final result.

Time comp:- O(n)
space comp:- o(1), as per the problem the output array is not added to space.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = 1
        postfix = 1
        res = [1]*l
        for i in range(l):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(l-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
"""
        l = len(nums)
        prefix = [1]*l
        postfix = [1]*l
        res = [1]*l
        for i in range(1,l):
            prefix[i] = nums[i-1]*prefix[i-1]
            
        for i in range(l-2 , -1, -1):
            postfix[i] = nums[i+1]*postfix[i+1]
        
        for i in range(l):
            res[i] = prefix[i]*postfix[i]
        return res
"""
```

## Complexity

- **Time:** O(n) — The solution involves two passes through the array, each taking linear time.
- **Space:** O(1) — The output array is not considered extra space, and only a few constant-space variables are used.
