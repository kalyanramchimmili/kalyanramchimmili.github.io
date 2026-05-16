---
title: Valid Anagram
description: "Determine if one string is an anagram of another."
tags: [Strings, Sorting, Hashing]
---

# Valid Anagram

## Problem

Determine if one string is an anagram of another. An anagram means the strings have the same characters with the same frequencies, just in a different order.

## Approach

The approach involves sorting both input strings. By sorting them, if they are anagrams, they will become identical strings. The sorted strings are then compared for equality.

## Solution

```python
"""
1. sort the 2 strings using sorted which would split the string into list and sort them based on ascii
2. use join to form string
3. sort both s and t compare them and return the output

time comp:- o(2nlogn) assuming n is len of t and n
space comp:- o(2n)
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        return (sorted_s == sorted_t)
```

## Complexity

- **Time:** O(N log N), where N is the length of the strings. Sorting dominates the time complexity.
- **Space:** O(N), for storing the sorted versions of the strings.
