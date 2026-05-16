---
title: Palindrome Number
description: "Determine if a given integer reads the same forwards and backward."
tags: [Math]
---

# Palindrome Number

## Problem

Determine if a given integer reads the same forwards and backward. Negative numbers and numbers ending in zero (except for zero itself) are not palindromes.

## Approach

The author notes that this problem is similar to reversing an integer. Negative numbers are immediately disqualified as their sign would appear at the end when reversed. Single-digit numbers (0-9) are always palindromes. The core idea is to reverse the integer using a temporary variable and then compare the reversed integer with the original.

## Solution

```python
"""
It was similar to reverse.
1. As per problem description, negative numbers with sign are not palindromes as the sign comes post the int after reversing it
2. 0-9 are all palindromes
3. was to rev a int with tmp variable and check if its a palindrome

time comp:- O(log10(x)) // number of digits in x
space comp:- o(1) //just 2 constants
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif 0 <= x <= 9:
            return True
        else:
            rev = 0
            tmp_x = x
            while x != 0:
                tmp = x % 10
                rev = rev * 10 + tmp
                x = int(x / 10)

            if rev == tmp_x:
                return True

        return False
```

## Complexity

- **Time:** O(log10(x)) — The number of operations is proportional to the number of digits in x.
- **Space:** O(1) — Only a few constant space variables are used.
