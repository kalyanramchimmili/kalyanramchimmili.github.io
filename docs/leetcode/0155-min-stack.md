---
title: Min Stack
description: Design a stack to efficiently track the minimum element in constant time.
tags: [Stacks, Design]
---

# Min Stack

## Problem

Design a stack data structure that allows for standard push, pop, and top operations, but also includes a `getMin` operation that can retrieve the current minimum element in the stack in constant time.

## Approach

This solution utilizes two stacks. The primary stack, `stackA`, stores all the elements pushed onto the `MinStack`. A secondary stack, `stackB`, is used to keep track of the minimum element. When pushing a new value, it's always added to `stackA`. It's only added to `stackB` if `stackB` is empty or if the new value is less than or equal to the current top of `stackB`. When popping an element from `stackA`, if that element is also the top of `stackB`, it's popped from `stackB` as well to maintain the correct minimum. The `top` operation simply returns the top of `stackA`, and `getMin` returns the top of `stackB`.

## Solution

```python
"""
1. 2 stack problem, while appending intially I appened to both a and b and sorted it after each append, but that was inefficent, hence the logic now only stores strictly small or equal values of prev value to stack B
2. Intially when stack si empty append the val else check the condition.
3. Pop would return the pop from stackA if the top of stackB match with popped element of A then pop from B also to eliminate the prev min there was.
4. top would return stackA[-1]
5 min woudl return stakcB[-1]

Time comp:- O(1) for all the cases
space comp:- O(2n) ~ O(n), assuming n no of elements in stack arranged in decreasing order.
"""
class MinStack:

    def __init__(self):
        self.stackA = []
        self.stackB = []
        

    def push(self, val: int) -> None:
        self.stackA.append(val)
        if len(self.stackB) == 0:
            self.stackB.append(val)

        elif self.stackB[-1] >= val:
            self.stackB.append(val)

    def pop(self) -> None:
        val = self.stackA.pop()
        if val == self.stackB[-1]:
            self.stackB.pop()

    def top(self) -> int:
        return self.stackA[-1]

    def getMin(self) -> int:
        return self.stackB[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

## Complexity

- **Time:** O(1) - All operations (push, pop, top, getMin) take constant time.
- **Space:** O(n) - In the worst case, if elements are pushed in decreasing order, the second stack `stackB` will store all elements, leading to linear space complexity.
