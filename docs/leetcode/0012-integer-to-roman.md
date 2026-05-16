---
title: Integer To Roman
description: "Convert an integer into its Roman numeral representation."
tags: [Math, Greedy]
---

# Integer to Roman

## Problem

Convert an integer into its Roman numeral representation. Roman numerals are formed by combining symbols representing specific values, with rules for repetition and subtractive forms for certain numbers like 4 and 9.

## Approach

The approach uses a mapping of Roman numeral values and their corresponding symbols, including the subtractive forms (e.g., 900 for "CM", 40 for "XL"). It iterates through this mapping from the largest value to the smallest. For each value, it determines how many times that value can fit into the remaining integer, appends the corresponding symbol that many times to the result string, and then updates the integer by taking the remainder. This process continues until the integer becomes zero.

## Solution

```python
"""
1. map a dict whichs serves as hash map, instead of handling 4 and 9's map those at as well
2. from first value and its symbol, first do a floor of num and value to get how many times of value is the number and add the symbol that many times to ans string
3. Modify the num by over-writing it with reminder and continue until it is not 0

time comp:- o(1) // runs 13 times (13 entires in dict)
space comp:- o(1)
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        conv_map = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
   
        ans = ""
        for value, sym in conv_map:
            if num != 0:
                temp = num // value
                ans += sym*temp
                num %= value #similar to num = num - (temp*value)
            else:
                break
        
        return ans
```

## Complexity

- **Time:** O(1) — The loop runs a fixed number of times (13 iterations based on the number of mappings).
- **Space:** O(1) — The space used by the mapping and the result string is constant relative to the input number.
