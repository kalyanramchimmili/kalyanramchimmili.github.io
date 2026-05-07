---
title: Valid Palindrome
tags: [Two Pointers, String]
---

# Valid Palindrome

## Problem

Determine if a given string is a palindrome after converting all uppercase letters to lowercase and removing all non-alphanumeric characters.

## Approach

This solution uses a two-pointer approach. Two pointers, `left` and `right`, are initialized at the beginning and end of the string, respectively. The pointers move inwards, skipping any non-alphanumeric characters. If the alphanumeric characters at the `left` and `right` pointers do not match (case-insensitive), the string is not a palindrome. If the pointers cross or meet without finding any mismatches, the string is a palindrome.

## Solution

```python
"""
1. 2 pointers method left and right starting from first and last respectively
2. if left or right char is not a char determine by isalnum which will check if it is char or num, if not skip
3. if yes compare left and right if not return false, else inc left and dec right
4. last return true if the loop passes

time comp:- o(n)
space :- o(1)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            while left < right and (not s[left].isalnum()):
                left += 1

            while left < right and (not s[right].isalnum()):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

## Complexity

- **Time:** O(n) — Each character is visited at most twice.
- **Space:** O(1) — No extra space is used beyond a few variables.
