---
title: Longest Palindrome
tags: [Arrays, Hashing]
---

# Longest Palindrome

## Problem

Given a string composed of lowercase and uppercase English letters, determine the length of the longest possible palindrome that can be constructed using these characters. Palindromes are case-sensitive.

## Approach

This approach counts the frequency of each character in the input string using a hash map. For each character's count, if the count is even, the entire count is added to the total length of the palindrome. If the count is odd, all but one instance of that character are used (i.e., count - 1 is added to the total), and a flag is set to indicate that at least one character with an odd count exists. Finally, if the odd count flag is true, one additional character can be placed in the center of the palindrome, so 1 is added to the total length.

## Solution

```python
"""
1. intiate a hashmap to count all values
2. for val in count.values, if val is even then add to ans, if odd then add val-1 to ans.
3. also mark odd flag, if odd flag is true add 1 to ans and return
4. the approach is for "abccccdd" -> count all even count 4 c's and 2 d's. and one odd to add in between.
5. so count all even val and one add val to ans and return

Time comp :- O(N)
space comp:- O(N)
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        ans = 0
        odd = False
        for char in s:
            count[char] = count.get(char,0)+1
        
        for val in count.values():
            if val%2 == 0:
                ans += val
            else:
                ans += val-1
                odd = True
        
        if odd:
            ans += 1
        
        return ans
```

## Complexity

- **Time:** O(N) — We iterate through the string once to build the frequency map, and then iterate through the unique characters in the map (at most 52).
- **Space:** O(N) — In the worst case, all characters in the string are unique, and the hash map will store an entry for each.
