---
title: Longest Common Prefix
tags: [Arrays, Hashing]
---

# Longest Common Prefix

## Problem

Given an array of strings, find the longest common prefix among them. If no common prefix exists, return an empty string.

## Approach

The strategy involves identifying the shortest string in the input list, as the common prefix cannot exceed its length. Then, iterate through the characters of this shortest string. For each character, check if it matches the corresponding character in all other strings. If a mismatch is found at any point, the current accumulated prefix is the longest common one. If all characters match across all strings for the length of the shortest string, then the shortest string itself is the longest common prefix.

## Solution

```python
"""
1. common prefix, find the shortest string in the list
2. for loop of the shortest string len, we take the intial string to create a char_to_match
3. run other for loop of num of strings in the list, if all chars are same add it to ans, if it breaks return the current ans
4. by defaults its "", would like to solve the common substring, that would be more challenging.

time comp:- o(n x l) each string is visited as number of elements in the short string
space comp:- o(1)
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if not strs:
            return ans
        l = min([len(s) for s in strs])
        n = len(strs)

        for i in range(l):
            char_to_match = strs[0][i]
            for j in range(1,n):
                if strs[j][i] != char_to_match:
                    return ans
            
            ans += char_to_match
        return ans
```

## Complexity

- **Time:** O(N * L) where N is the number of strings and L is the length of the shortest string. In the worst case, we iterate through each character of the shortest string and compare it with the corresponding character in all other strings.
- **Space:** O(1) as we only use a few variables to store the result and loop indices.
