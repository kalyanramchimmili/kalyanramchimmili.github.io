---
title: Longest Palindromic Substring
description: "Given a string `s`, find and return the longest substring within `s` that is also a palindrome."
tags: [Strings, Dynamic Programming, Expanding Around Center]
---

# Longest Palindromic Substring

## Problem

Given a string `s`, find and return the longest substring within `s` that is also a palindrome. A palindrome reads the same forwards and backward.

## Approach

This solution uses the "expand around center" approach. The core idea is that every palindrome has a center. This center can be a single character (for odd-length palindromes like "aba") or the space between two characters (for even-length palindromes like "abba").

The algorithm iterates through each character of the string. For each character, it considers two possible centers:
1. The character itself (index `i`) as the center for odd-length palindromes.
2. The space between the character at index `i` and the next character at `i+1` as the center for even-length palindromes.

For each center, it expands outwards (decrementing `left` and incrementing `right`) as long as the characters at `left` and `right` are equal and within the bounds of the string. During this expansion, it keeps track of the longest palindrome found so far.

## Solution

```python
class Solution:

    def longestPalindrome(self, s: str) -> str:

        l1 = len(s)
        max_str = ""

        for i in range(l1):
            for left, right in [(i,i), (i,i+1)]:
                while left >= 0 and right < l1 and s[left]==s[right]:
                    if (right-left+1) > len(max_str):
                        max_str = s[left : right+1]
                    
                    left -= 1
                    right += 1
        return max_str
```

## Complexity

- **Time:** O(n^2) — The outer loop iterates `n` times (where `n` is the length of the string). In the worst case, the `while` loop (expansion) can also run up to `n` times for each center.
- **Space:** O(1) — The algorithm uses a constant amount of extra space for variables like `max_str`, `left`, and `right`.
