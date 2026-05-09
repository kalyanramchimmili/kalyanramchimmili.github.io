---
title: Ransom Note
tags: [Strings, Hashing, Counting]
---

# Ransom Note

## Problem

Given two strings, `ransomNote` and `magazine`, determine if the `ransomNote` can be constructed using the letters from `magazine`. Each letter in `magazine` can only be used once.

## Approach

First, we initialize a frequency map (or counter) and count all the characters present in the `magazine` string. Then, we iterate through the `ransomNote` string. For each character in `ransomNote`, we check if it exists in our frequency map and if its count is greater than zero. If the character is not found in the map or its count is already zero, it means we don't have enough of that letter from the magazine, so we return `false`. Otherwise, we decrement the count of that character in the frequency map. If we successfully iterate through the entire `ransomNote` without returning `false`, it means the note can be constructed, and we return `true`.

## Solution

```python
"""
1. intialize count var and count all char in magazine
2. check in ransomNote if there is any char not in count or if its frew has got to 0, but the char exists in ransomNote, return false
3. dec the count of the ch in count other wise 
4. if loop completes, ransomNote can be made form magazine, return true

time comp:- O(N), n = len(ransomNote)
space comp:- O(N)
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        count = {}

        for char in magazine:
            count[char] = count.get(char,0)+1
        
        for ch in ransomNote:
            if ch not in count or count[ch] == 0:
                return False
            
            count[ch] -= 1
        
        return True
```

## Complexity

- **Time:** O(M + N) where M is the length of `magazine` and N is the length of `ransomNote`. This is because we iterate through `magazine` once to build the frequency map and then iterate through `ransomNote` once to check for constructability.
- **Space:** O(K) where K is the number of unique characters in `magazine`. In the worst case, if all characters are unique, this could be O(26) for lowercase English letters, which is effectively O(1). However, if the character set were larger, it would be O(K).
