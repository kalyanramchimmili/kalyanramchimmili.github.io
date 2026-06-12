---
title: Rotting Oranges
description: Return the minimum time until no fresh oranges remain, or -1 if impossible.
tags: [Breadth-First Search, Array, Matrix]
---

# Rotting Oranges

## Problem

Given a grid representing oranges, where 0 is empty, 1 is fresh, and 2 is rotten, determine the minimum minutes for all fresh oranges to rot. A fresh orange rots in one minute if it's adjacent to a rotten orange. If it's impossible for all oranges to rot, return -1.

## Approach

This problem can be solved using a Breadth-First Search (BFS) approach, similar to the 01 Matrix problem, but adapted for a multi-source BFS pattern.

1.  Initialize a queue and add all initially rotten oranges to it. Each element in the queue will store the orange's coordinates and the current time (level) it became rotten.
2.  Count the total number of fresh oranges. If there are no fresh oranges initially, return 0.
3.  Perform BFS: Dequeue a rotten orange and explore its four adjacent cells.
4.  If an adjacent cell contains a fresh orange, rot it (change its value to 2), decrement the fresh orange count, and enqueue it with an incremented time (level + 1).
5.  Keep track of the maximum time (level) reached during the BFS.
6.  After the BFS completes, if the count of fresh oranges is 0, return the maximum time. Otherwise, return -1, indicating that some fresh oranges could not be reached and rotted.

Time Complexity: O(m*n), where m and n are the dimensions of the grid.
Space Complexity: O(m*n) in the worst case, for the queue.

## Solution

```python
"""
1. Similar to 01 matrix problem, it was distance here is time, both afre bfs, but this is mulit-soruce bfs pattern, the other one normal bfs.
2. Intialize a queue, if the orange is rotten append it to queue with intial level as 0 serving as time here.
3. if the ornage is fresh just count the fresh oranges, if no fresh oranges return 0 else continue.
4. Look through queue, first for all the first identified rotten oranges, all 4 dir of it, if exists then rotten it to, append it back with level+1 indicating +1 min, continue, also dec the fresh oranges count.
5. once the fun is completed, we record the highest level, if the fresh oranges count is 0 return level else -1, cause not all were reachable.

Time comp:- O(m*n), where m and n are rows and col's.
space comp:- O(m*n)
"""
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        lr = len(grid)
        lc = len(grid[0])
        distance = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        fresh_ora = 0
        level = 0

        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == 2:
                    q.append((i, j, level))
                elif grid[i][j] == 1:
                    fresh_ora += 1

        if not fresh_ora:
            return 0

        while q and fresh_ora > 0:
            r, c, l = q.popleft()

            for dr, dc in distance:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < lr and 0 <= nc < lc and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, l + 1))
                    fresh_ora -= 1
                    level = max(level, l + 1)

        if fresh_ora > 0:
            return -1
        else:
            return level
```

## Complexity

-   **Time:** O(m*n) — Each cell is visited at most once.
-   **Space:** O(m*n) — In the worst case, all oranges could be rotten and enqueued.
