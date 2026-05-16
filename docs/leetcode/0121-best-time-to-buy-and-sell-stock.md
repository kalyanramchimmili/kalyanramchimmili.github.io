---
title: Best Time to Buy and Sell Stock
description: "Given an array of stock prices for consecutive days, find the maximum profit that can be achieved by buying on one day and selling on a…"
tags: [Arrays, Hashing]
---

# Best Time to Buy and Sell Stock

## Problem

Given an array of stock prices for consecutive days, find the maximum profit that can be achieved by buying on one day and selling on a future day. If no profit can be made, return 0.

## Approach

The approach involves iterating through the prices to find the minimum price encountered so far and calculating the potential profit by subtracting this minimum from the current price. The maximum profit is updated if the current profit is greater.

## Solution

```python
"""
1. min value as first int, profit as 0
2. find the min value of the list and record it
3. find the max value by sub current prices[i]-min value and record it
4. after iteration return profit

timecomp:- O(n)
space:- O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        min_value = prices[0]
        
        for i in range(n):
            min_value = min(min_value, prices[i])
            profit = max(profit, prices[i]-min_value)
        
        return profit
```

## Complexity

- **Time:** O(n) — The solution iterates through the `prices` array once.
- **Space:** O(1) — The solution uses a constant amount of extra space for variables.
