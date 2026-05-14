---
title: K Closest Points to Origin
tags: [Arrays, Hashing]
---

# K Closest Points to Origin

## Problem

Given a list of 2D points and an integer k, find the k points that are closest to the origin (0,0). The distance is calculated using the Euclidean distance formula.

## Approach

The author's approach involves calculating the Euclidean distance of each point from the origin and storing it along with the point itself. The list of (distance, point) pairs is then sorted based on the distance. Finally, the first k points from the sorted list are extracted and returned.

## Solution

```python
"""
1. distance fun to return the distance, a ans list
2. for point in points, find the distance and append the distance and point in the list 
3. sort based on distance, sorts based of first element by default
4. result list, where we append k points from the ans list and return the result

time comp:- O(nlogn) :- to sort, building list is only n
space comp:- O(n)
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        ans = []

        def distance(x,y):
            return math.sqrt((x)**2+(y)**2)

        for point in points:
            dis = distance(point[0], point[1])
            ans.append((dis, point)) #python automatically sorts based on first element

        ans.sort()
        # or ans.sort(key=lamda x: x[1]) -> sort based on 2nd element
        result = []
        for _ in range(k):
            result.append(ans[_][1])
        
        return result
```

## Complexity

- **Time:** O(N log N) — The dominant operation is sorting the list of points by their distance, which takes O(N log N) time. Building the initial list takes O(N) time.
- **Space:** O(N) — An auxiliary list `ans` is created to store the distance and point for each of the N points, requiring O(N) space.
