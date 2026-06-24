---
title: Merge Intervals
description: Merge overlapping intervals in a list and return the non-overlapping intervals that cover all inputs
tags: [Arrays, Sorting]
---

# Merge Intervals

## Problem

Given a list of intervals, where each interval is represented by a start and end point, merge any intervals that overlap. The goal is to return a new list containing only the non-overlapping intervals that encompass all original intervals.

## Approach

The author recalls a similar problem and outlines a strategy involving sorting the intervals first. An empty list is initialized to store the merged results. The first interval is taken as the current interval. Then, the code iterates through the remaining intervals, comparing the start of the next interval with the end of the current interval. If they overlap (i.e., the next interval's start is less than or equal to the current interval's end), the current interval is updated to encompass both by taking the minimum start and maximum end. If there's no overlap, the current interval is added to the results, and the next interval becomes the new current interval. Finally, after the loop, the last current interval is added to the results. The author also notes that sorting is crucial for this approach to work correctly.

## Solution

```python
"""
1. Had done a similar problem beforem but cant recall which. Checking the intervals
2. an empty ans list, start of with first range as curr, in a for loop of 1 to l, compare 1st range with 2nd, if the start of 2nd range is smaller or equal to end of 1st range there is an overlap.
3. if there is overlap, start would be min of both and end would be max of both, these would be curr var so it can be compared with next range.
[[1,3],[2,6],[8,10],[15,18]], here after 1st 2 sets it would be 1,6 and now 1,6 shld compare to 8,10. 
4. if the overlap is not there append the curr var's and start fresh by initializing curr as say 8,10. now 8,10 will compare with 15,18.
5. at last say one case [[1,4],[4,5]], loop ends after 1,5 append it to ans and return ans.
6. one test case fails as the interval list is not sorted so interval.sort() would sort based on 0th index element.

time comp:- O(N logn) + O(N) ~ O(nlogn), n being number of intervals, nlogn for sorting.
space comp:- O(1)
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l = len(intervals)
        ans = []
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        for i in range(1, l):
            s2 = intervals[i][0]
            e2 = intervals[i][1]
            if s2 <= curr_end:
                curr_start = min(curr_start, s2)
                curr_end = max(curr_end, e2)
            else:
                ans.append([curr_start, curr_end])
                curr_start = s2
                curr_end = e2

        ans.append([curr_start, curr_end])
        return ans
```

## Complexity

- **Time:** O(N log N) - due to sorting the intervals, where N is the number of intervals. The subsequent iteration is O(N).
- **Space:** O(1) - if we consider the output list not as extra space, otherwise O(N) in the worst case for the output list.
