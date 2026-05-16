---
title: Reverse Integer
description: "Reverse the digits of a signed 32-bit integer."
tags: [Math, Two Pointers]
---

# Reverse Integer

## Problem

Reverse the digits of a signed 32-bit integer. If the reversed integer falls outside the 32-bit signed integer range, return 0.

## Approach

The approach involves reversing the digits of the integer using standard arithmetic operations. A flag is used to track if the original number was negative. The number is made positive, its digits are reversed by repeatedly taking the remainder and building the reversed number, and then it's made negative again if necessary. Finally, a check is performed to ensure the reversed integer stays within the 32-bit signed integer range, returning 0 if it overflows.

## Solution

```python
"""
This is quite simple
1. the std reversal of number, get the last digit out, mul the prev rev into 10 and add the rem we get until the orginal number becomes 0
2. for neg numbers, have a flag, mul with -1 first and after reversing mul with -1 again as per que
3. if the reversal overflows return 0 checking with the  if reverse < -2**31 or reverse > (2**31 - 1):
"""
class Solution:
    def reverse(self, x: int) -> int:

        reverse = 0

        if x > 0:
            isneg = False
        else:
            isneg = True
            x = x * -1

        while x != 0:
            rem = x % 10
            reverse = reverse*10 + rem
            x = int(x/10)

        if isneg:
            reverse = reverse * -1

        if reverse < -2**31 or reverse > (2**31 - 1):
            return 0
        
        return reverse
```

## Complexity

- **Time:** O(log10(x)) — The number of iterations is proportional to the number of digits in `x`.
- **Space:** O(1) — Constant extra space is used regardless of the input size.
