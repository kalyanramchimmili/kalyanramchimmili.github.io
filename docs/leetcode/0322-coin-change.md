---
title: Coin Change
description: Find the minimum number of coins to make a target amount, or return -1 if impossible
tags: [Dynamic Programming, Arrays]
---

# Coin Change

## Problem

Given an array of coin denominations and a target amount, find the fewest number of coins needed to reach that amount. If the amount cannot be formed using any combination of the given coins, return -1. You have an unlimited supply of each coin denomination.

## Approach

This problem is solved using dynamic programming. We initialize a DP array where each index represents an amount, and the value at that index stores the minimum number of coins required to make that amount. The array is initialized with a value larger than any possible valid result (e.g., `amount + 1` or infinity) to signify that an amount is currently unreachable. `dp[0]` is set to 0, as zero coins are needed to make an amount of zero.

We then iterate through each coin denomination. For each coin, we iterate through possible amounts starting from the coin's value up to the target amount. If the current amount is greater than or equal to the coin's value, we consider using this coin. The number of coins needed for the current amount would be 1 (for the current coin) plus the minimum number of coins needed for the remaining amount (`dp[currentAmount - coin]`). We update `dp[currentAmount]` with the minimum of its current value and this new calculated value.

Finally, if `dp[amount]` is still its initial "unreachable" value, it means the target amount cannot be made; otherwise, `dp[amount]` holds the minimum number of coins required.

## Solution

```python
"""
1. Learnt dp for this problem, there is still a lot to learn in dp space on how to build towards the approach. Dp is basically backtracking with memorization.
2. how this one is solved is first a dp array is intialized with amount + 1, for comaprision, it can be float('inf') as well.
3. dp[0] is 0, and considering for all coins begin with first coin, for dp[1] for 1 Rs, it would be 1 coing which is either min(dp[1], 1+dp[0]) i.e if 1 is not visited before it would be amount+1, so it woukd be 1 coin more than dp[0].
4. Same thing with dp[2] etc until dp[amount], now coin 2, it will start from currAmount >= coin that index, so say for making 4 we take 4 1Rs coins, now we have a 4rs, so it shld be 1 min(4, dp[4-4]+1) i.e 1, for coin 7 etc.
5. if sp[amount] is same as intial set value then there is no solution return -1 else return the dp value.

ref:- Neetcode vedio helped for this appraoch.

Time comp:- O(amount*coins) worst case:- N^2
space comp:- O(amount)/O(N)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for currAmount in range(1, amount+1):
                if currAmount >= coin:
                    dp[currAmount] = min(dp[currAmount], 1+dp[currAmount-coin])
                    
        return dp[amount] if dp[amount] != amount+1 else -1
```

## Complexity

- **Time:** O(amount * number_of_coins) - We have a nested loop where the outer loop iterates through each coin, and the inner loop iterates up to the target amount.
- **Space:** O(amount) - We use a DP array of size `amount + 1` to store the minimum coins needed for each amount.
