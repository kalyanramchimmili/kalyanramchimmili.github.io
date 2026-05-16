---
title: Flood Fill
description: "Given a 2D grid representing an image, a starting pixel's coordinates, and a new color, change the color of the starting pixel and all…"
tags: [Depth-First Search, Breadth-First Search, Recursion, Array]
---

# Flood Fill

## Problem

Given a 2D grid representing an image, a starting pixel's coordinates, and a new color, change the color of the starting pixel and all connected pixels of the same original color to the new color. Connectivity is defined by horizontal and vertical adjacency.

## Approach

The problem can be solved using recursion, similar to a Depth-First Search (DFS) approach. First, we capture the original color of the starting pixel. If this original color is already the target color, no changes are needed, and we return the image as is. Otherwise, we define a recursive helper function. This function checks if the current pixel is within the image boundaries and if its color matches the original color. If these conditions are met, it changes the pixel's color to the new color and then recursively calls itself for its four neighbors (up, down, left, right). The process begins by calling this helper function with the initial starting pixel coordinates.

## Solution

```python
"""
1. this one was pretty hard to understand, but it was simple after that via recurrsion
2. capture the orignal value, if the value is already same as colour, nothing to change, return the image
3. we have fill fun within, which checks the boundary for rows and columns, if the new index is equal to orignal value or not, if not or out of index return simply.
4. if not then change it to colour, do the same thing for up down, right left 
5. start the fun by first calling the given index and return the image after it

time comp:- O(m*n)
space comp:- O(m*n)
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        orginal_value = image[sr][sc]

        if orginal_value == color:
            return image

        def fill(r, c):
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or (image[r][c] != orginal_value):
                return

            image[r][c] = color

            fill(r-1, c)
            fill(r+1, c)
            fill(r, c-1)
            fill(r, c+1)
        
        fill(sr,sc)
        return image

```

## Complexity

- **Time:** O(m*n) - In the worst case, we might visit every pixel in the image.
- **Space:** O(m*n) - The recursion depth can be up to m*n in the worst case, leading to stack overflow. This is due to the recursive calls.
