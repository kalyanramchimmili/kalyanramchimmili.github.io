---
title: Add Binary
description: "Given two binary strings, return their sum as a new binary string."
tags: [Strings, Math]
---

# Add Binary

## Problem

Given two binary strings, return their sum as a new binary string.

## Approach

The approach involves simulating binary addition from right to left, handling carries. We iterate through the strings from their last characters, adding the corresponding digits and the carry from the previous position. If the sum of digits and carry is 2 or 3, the carry for the next position is 1; otherwise, it's 0. The last digit of the current sum (sum modulo 2) is appended to the result. This process continues as long as there are digits left in either string or there's a remaining carry. The final result is constructed by reversing the appended digits.

## Solution

```python
"""
1. if sum is 2 or 3 carry is 1, else carry is 0
2. traverse from last, i or j >= 0 or if carry is at last, count the sum, if sum is even, append 0 else append 1
3. carry would be floor operator for 0

time comp:- O(n), n being max(i+1, j+1)
space comp:- O(n)
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        ans = []
        carry = 0

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1
            
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            ans.append(str(total%2))
            carry = total//2
        
        return "".join(ans[::-1])
```

## Complexity

- **Time:** O(max(N, M)) where N and M are the lengths of strings `a` and `b`, respectively. We iterate through the strings once.
- **Space:** O(max(N, M)) for storing the result string.
