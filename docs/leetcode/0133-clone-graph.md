---
title: Clone Graph
description: "Given a connected undirected graph represented by a reference to one of its nodes, create a deep copy of the entire graph."
tags: [Graphs, DFS, BFS, Hashing]
---

# Clone Graph

## Problem

Given a connected undirected graph represented by a reference to one of its nodes, create a deep copy of the entire graph. Each node contains an integer value and a list of its neighbors.

## Approach

The solution involves traversing the graph and creating a new, independent copy of each node and its connections. A hash map is used to keep track of already cloned nodes to avoid infinite recursion and ensure that each original node is mapped to exactly one cloned node.

For DFS, a recursive function is used. If a node has already been cloned and is present in the hash map, its clone is returned. Otherwise, a new node is created with the same value, stored in the hash map, and then its neighbors are recursively cloned and appended to the new node's neighbor list.

For BFS, a queue is used. The starting node is cloned, and both the original and cloned nodes are added to the hash map and the queue. Then, nodes are dequeued, and their neighbors are processed. If a neighbor hasn't been cloned, it's cloned, added to the hash map and the queue. The cloned neighbor is then appended to the current cloned node's neighbor list. This process continues until the queue is empty, ensuring all nodes and their connections are copied.

## Solution

```python
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
# using DFS
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        newmap = {}

        if not node:
            return None

        def clone(node):
            if node in newmap:
                return newmap[node]

            newNode = Node(node.val)
            newmap[node] = newNode
            for i in node.neighbors:
                newNode.neighbors.append(clone(i))
            return newNode
        
        return clone(node)

"""
# using BFS
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        newmap = {}
        if not node:
            return None
        
        newNode = Node(node.val)
        newmap[node] = newNode
        q = []
        left = 0
        right = 0
        q.append(node)
        right += 1
        while left < right:
            curr_node = q[left]
            left += 1
            for i in curr_node.neighbors:
                if i not in newmap:
                    newNode = Node(i.val)
                    newmap[i] = newNode
                    q.append(i)
                    right += 1

                newmap[curr_node].neighbors.append(newmap[i])

        return newmap[node]
"""
```

## Complexity

- **Time:** O(V + E) — where V is the number of nodes and E is the number of edges. Both DFS and BFS traverse each node and each edge once.
- **Space:** O(V) — for the hash map to store cloned nodes and the recursion stack (DFS) or queue (BFS).
