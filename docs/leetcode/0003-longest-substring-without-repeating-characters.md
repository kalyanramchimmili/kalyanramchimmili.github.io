---
title: Longest Substring Without Repeating Characters
tags: [Strings, Sliding Window, Hashing]
---

# Longest Substring Without Repeating Characters

## Problem

Given a string, find the length of the longest substring that does not contain any repeating characters.

## Approach

_(approach inferred from code — author notes were empty)_

This solution utilizes the sliding window technique. A window is maintained within the string, defined by two pointers, `i` (start) and `j` (end). A set `char_set` is used to keep track of the characters currently within the window. The `j` pointer iterates through the string. If the character at `s[j]` is already present in `char_set`, it means a repeating character has been found. In this case, the window is shrunk from the left by incrementing `i` and removing characters from `char_set` until `s[j]` is no longer in the set. If `s[j]` is not in the set, it's added, and the maximum length of the current valid substring (`j - i + 1`) is updated.

## Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        char_set = set()
        max_len = 0

        for j in range(len(s)):
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1
            
            char_set.add(s[j])
            max_len = max(max_len, j-i+1)
        
        return max_len
```

## Complexity

- **Time:** O(n) — Each character is visited at most twice (once by `j` and once by `i`).
- **Space:** O(min(n, m)) — Where n is the length of the string and m is the size of the character set (e.g., 26 for lowercase English letters, 128 for ASCII). In the worst case, the set can store all unique characters in the string or the size of the alphabet.
