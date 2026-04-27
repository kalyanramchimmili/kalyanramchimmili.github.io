"""
APPROACH:
Walk through the array once, keeping a hash map of {value: index} we've seen.
For each new number, check if its complement (target - num) is already in the map.
If yes, we have our pair. If no, store it and move on.

This trades O(n) extra space for O(n) time vs. the brute O(n^2) double loop.

TIME: O(n) — single pass, O(1) hash lookups.
SPACE: O(n) — worst case the whole array goes into the map before we find a pair.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []
