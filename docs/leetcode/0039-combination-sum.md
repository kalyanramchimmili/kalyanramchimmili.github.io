---
title: Combination Sum
description: Find all unique combinations of distinct integers that sum up to a target value.
tags: [Backtracking, Array, Depth-First Search]
---

# Combination Sum

## Problem

Given an array of distinct integers and a target integer, find all unique combinations of numbers from the array that sum up to the target. The same number can be used multiple times in a combination.

## Approach

The solution uses a recursive backtracking approach to explore all possible combinations. It starts with an empty combination and the full target value. At each step, it iterates through the available candidates starting from a given index. If a candidate is chosen, it's added to the current combination, and the function recursively calls itself with the reduced target and the same candidate index (to allow for reuse). If the target becomes zero, a valid combination is found and added to the results. If the target becomes negative, that path is invalid. After a recursive call returns, the last chosen candidate is removed from the combination (backtracking) to explore other possibilities. Using a start index in the loop prevents duplicate combinations and ensures that the same number can be reused by passing `i` instead of `i + 1` to the recursive call.

## Solution

```python
"""
1. brute force to div 2, with the remaining check if it is part of any candiate add it to path, but that wouldn't give us all combinations. So do it recursively, with the remaining so we check all the combinations.
2. Start with an empty combination and the full target as the remaining value. At each step, choose a candidate and subtract it from the remaining target.
3. If remaining becomes 0, a valid combination is found. Add a copy of the current path to the result and return.
4. If remaining becomes negative, this path cannot form the target, so return.
5. For every recursive call, try all candidates starting from the current index. Using a start index prevents duplicate combinations such as [2,3,3] and [3,2,3].
6. When choosing a candidate, append it to the current path and recursively call solve(i, remaining - candidates[i], path). Use i instead of i+1 because the same number can be reused unlimited times.
7. After the one branch of recursive call finishes, remove the last element from the path using path.pop(). Once one branch completes we want to start over with new i moving the index.
8. Start the recursion with solve(0, target, []).

Time Comp:- O(N^(target/min_candidate)) -> roughly
Space Comp:- O(target/min_candidate) for the recursion stack and current path.
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l = len(candidates)
        res = []

        def solve(start, remaining, path):
            if remaining == 0:
                res.append(list(path))
                return

            if remaining < 0:
                return

            for i in range(start, l):
                path.append(candidates[i])
                solve(i, remaining - candidates[i], path)
                path.pop()

        solve(0, target, [])
        return res
```

## Complexity

- **Time:** O(N^(target/min_candidate)) — In the worst case, the recursion depth can be `target / min_candidate`, and at each level, we iterate through `N` candidates.
- **Space:** O(target/min_candidate) — This is due to the recursion stack depth and the space used to store the current combination path.
