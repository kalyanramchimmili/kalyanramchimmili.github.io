---
title: Permutations
description: Find all possible arrangements of distinct integers in an array.
tags: [Backtracking, Recursion, Arrays]
---

# Permutations

## Problem

Given an array of unique integers, find all the distinct ways to arrange them. The order of the arrangements in the output doesn't matter.

## Approach

The problem can be solved using a recursive backtracking approach. We maintain a list to store all valid permutations and a temporary list to build each permutation step-by-step. The backtracking function explores possibilities by adding a number to the temporary list if it hasn't been used yet. When the temporary list's length matches the original array's length, a complete permutation is found and added to the solution list. After exploring a path, we backtrack by removing the last added element to explore other possibilities.

## Solution

```python
"""
Okay took a lot of time to get this solution click, ofc im dumb 
1. simple dfs or backtracking, a sol array with all sol, a temp storing our trials onw.
2. start of with 1st var say [1,2,3], start with 1, then we have either 1,2 or 1,3, say 1,2 then we append 3 if temp len is equal to actual array then append it to solution.
3. Once we append we need to go back, when backtrack returns after appending or if dosent enter the for loop it returns none, so backtrack returns none and pops the last element, undoing the temp array one by one until 1 this case, and add 3 now and continue in that path to get 1,3,2.
4. Intiate the backtrack fun, and return the final sol array with all possible combinations.

time comp:- O(n!)
Space comp:- O(n)
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        temp = []
        def backtrack():
            if len(nums) == len(temp):
                sol.append(temp[:])
                return

            for num in nums:
                if num not in temp:
                    temp.append(num)
                    backtrack()
                    temp.pop()
        backtrack()
        return sol
```

## Complexity

- **Time:** O(n! * n) — For each of the n! permutations, we are creating a copy of the current permutation (which takes O(n) time).
- **Space:** O(n) — For the recursion depth and the temporary list used to build permutations.
