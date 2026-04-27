```yaml
title: "Two Sum"
tags: ["array", "hash table"]
```

# Two Sum

## Approach

This solution utilizes a single pass through the input array `nums` and a hash map (dictionary in Python) to efficiently find two numbers that sum up to the `target`. The hash map stores the numbers encountered so far along with their corresponding indices.

For each number `n` at index `i` in the array:
1. Calculate the `complement` needed to reach the `target` (i.e., `target - n`).
2. Check if this `complement` already exists as a key in the `seen` hash map.
   - If it does, it means we have found the pair: the index of the complement is stored in the map, and the current index `i` is the index of the second number. We return these two indices.
   - If it does not, we add the current number `n` and its index `i` to the `seen` hash map. This allows future iterations to check against this number.

This approach significantly optimizes the problem by avoiding a brute-force O(n^2) nested loop comparison. Instead, it achieves O(n) time complexity by leveraging the O(1) average time complexity of hash map lookups and insertions. The trade-off is the use of O(n) extra space to store the seen numbers.

## Solution

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []
```

## Complexity

- **Time Complexity**: O(n)
  The algorithm iterates through the input array `nums` exactly once. Each operation within the loop (calculating the complement, checking for its existence in the hash map, and inserting into the hash map) takes, on average, constant time O(1).

- **Space Complexity**: O(n)
  In the worst-case scenario, if the target sum is not found until the very end of the array, the `seen` hash map might store up to `n` key-value pairs, where `n` is the number of elements in the `nums` array.
