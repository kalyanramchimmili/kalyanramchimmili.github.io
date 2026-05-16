---
title: Letter Combinations of a Phone Number
description: "Given a string of digits from 2-9, generate all possible letter combinations that the digits can represent, based on a standard phone…"
tags: [Arrays, Hashing]
---

# Letter Combinations of a Phone Number

## Problem

Given a string of digits from 2-9, generate all possible letter combinations that the digits can represent, based on a standard phone keypad mapping.

## Approach

The author mapped each digit to its corresponding letters, similar to how Roman numerals are mapped. They then created a list of these letter groups for each digit in the input. The `itertools.product` function was used to generate all combinations of letters, taking one letter from each group. Finally, these combinations, which are initially tuples of characters, are joined into strings.

## Solution

```python
"""
1. map out the numbers to letters, similar to int to roman problem
2. make a list of all the group of numbers based on lists i.e., ans_list
3. using something called itertools.product which multiples each list element with other list element to return all possible values -> combinations
4. the prob here is combinations spits out ("a" , "d"), to convert into "ad", use "".join for all combination groups inside combinations and return the value

itertools.product is a new thing for me in python, haven't used it before

time comp:- O(3^6 * 4^2 * n), n being size of string -> O(4^n * n)
Space comp:- O(4^n * n) as we are building ans_list
"""
import itertools
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        conv_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        ans_list = []
        for d in digits:
            ans_list.append(conv_map[d])
        
        combinations = itertools.product(*ans_list)
        return ["".join(comb) for comb in combinations]
```

## Complexity

- **Time:** O(4^n * n) — where n is the length of the `digits` string. The maximum number of combinations is 4^n (since '7' and '9' have 4 letters), and joining each combination takes O(n) time.
- **Space:** O(4^n * n) — to store the resulting list of letter combinations.
