---
title: Climbing Stairs
tags: [Dynamic Programming, Recursion, Memoization]
---

# Climbing Stairs

## Problem

You need to find the number of distinct ways to climb a staircase with `n` steps, given that you can take either 1 or 2 steps at a time.

## Approach

The author observed that listing out the number of ways for small values of `n` (1, 2, 3, 4, 5) reveals a pattern corresponding to the Fibonacci sequence, starting with 1 and 2. A direct recursive approach leads to Time Limit Exceeded for larger inputs. Therefore, an iterative approach is used, where for `n=1` and `n=2`, the result is `n` itself. For `n > 2`, the solution iteratively computes the Fibonacci series up to `n` and returns the last computed sum.

## Solution

```python
"""
1. Listing out till 5 
1 2 3 4 5
1 2 3 5 8
-> it is Fibonacci series starting from 1 and 2
2. Doing the recursive apporach, it gives TLE for n >= 44
3. Doing iterative apporach, n == 1 and 2 return n else for 3 to n, compute Fibonacci series and return the last sum.

time comp:- O(N)
space comp:- O(1)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n==2:
            return n
        a = 1
        b = 2
        for i in range(3,n+1):
            a, b = b, a+b
        
        return b

        """return self.climbStairs(n-1)+self.climbStairs(n-2)"""
```

## Complexity

- **Time:** O(N) - The solution iterates from 3 up to `n` once.
- **Space:** O(1) - The solution uses a constant amount of extra space for variables `a` and `b`.
