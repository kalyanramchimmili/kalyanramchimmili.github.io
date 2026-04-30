---
title: Zigzag Conversion
tags: [Arrays, String]
---

# Zigzag Conversion

## Problem

Given a string and a number of rows, arrange the string in a zigzag pattern and then read it line by line to produce a new string.

## Approach

The author initially considered using a 2D array to represent the zigzag pattern, tracking movement direction with a flag. However, this approach was found to be slow. The refined approach treats the problem as distributing characters into "buckets" (an array of strings, where each string represents a row). Characters are added to these buckets while simulating the zigzag movement: going down the rows until the last row, then moving diagonally up until the first row, and repeating this pattern. Finally, all the buckets are concatenated to form the result.

## Solution

```python
"""
This was a tough one, the quetion wasn't that clear.

Old approach:-
seeing the disscussion I understood how the output should look like
1. use a 2D array, with flag goingDown to determine if we are going down or diagonal
2. if the row is not the last row yet then keep going down, if it is equal to last one, dec the row and inc col to move diagonal
3. if we are moving diagnoal, if we reach row 0 then start moving down and at last run a 2 for loops, add all non blank row col values to a string and return

new approach:-
Although the old apporach ran, it was bit slow, I wanted to optimize, not gonna like i did use ai to see how to do it, then it said me instead of 2d array treat it like buckets
1. same concept moving down and moving diagonally, instead of adding it to 2D array, we are adding to a array of string of len numRows
2. same pattern, current row inc for going down until it touches the last row, if current row is last then start dec the current_row.
3. if the current_row == 0 then start inc it again, finally add all the row_buckets and return it as a string.

time comp:- o(n)
space comp:- o(n)
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row_bucket = ["" for _ in range(numRows)]

        current_row = 0
        goingDown = True
        n = len(s)

        for i in range(n):
            row_bucket[current_row] += s[i]
            if goingDown:
                if current_row == numRows-1:
                    current_row -= 1
                    goingDown = False
                else:
                    current_row += 1
            else:
                if current_row > 0:
                    current_row -= 1
                else:
                    goingDown = True
                    current_row += 1

        ans = ""
        for _ in range(numRows):
            ans += row_bucket[_]
        
        return ans


                

"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows > n:
            return s

        ans = [["" for _ in range(n)] for _ in range(numRows)]

        goingDown = True
        r = c = 0

        for char in s:
            ans[r][c] = char

            if goingDown:
                if r < numRows - 1:
                    r += 1
                else:
                    goingDown = False
                    r -= 1
                    c += 1
            else:
                if r > 0:
                    r -= 1
                    c += 1
                else:
                    goingDown = True
                    r += 1

        ans_str = ""

        for i in range(numRows):
            for j in range(n):
                if ans[i][j] != "":
                    ans_str += ans[i][j]

        return ans_str
"""
```

## Complexity

- **Time:** O(n) — We iterate through the string once to place characters into buckets.
- **Space:** O(n) — We use an array of strings (buckets) to store the characters, which in the worst case can hold all characters of the input string.
