---
title: Implement Queue Using Stacks
description: "Implement a queue data structure (First-In, First-Out) using only the standard operations of two stacks."
tags: [Stacks, Design]
---

# Implement Queue Using Stacks

## Problem

Implement a queue data structure (First-In, First-Out) using only the standard operations of two stacks. The implementation should support the typical queue operations: push, pop, peek, and checking if the queue is empty.

## Approach

The approach uses two stacks, `stack1` and `stack2`, to simulate a queue.
When pushing an element, it is simply appended to `stack1`.
To pop an element, all elements from `stack1` are transferred to `stack2`. The top element of `stack2` is then popped (this is the front of the queue). Finally, the elements are moved back from `stack2` to `stack1` to restore the original order for subsequent operations.
Peeking involves returning the first element of `stack1`.
An empty queue is determined by checking if `stack1` is empty.

## Solution

```python
"""
1. 2 stacks for a queue, to push, push it to stack 1
2. to pop, push all elements of stack 1 to stack 2, pop the stack 2, store the values, and shift all the elements back from stack 2 to stack 1, and return the value
3. for peek return stack[0] the first element in stack
4. for empty, check the size of stack 1, return true or false

time comp:- O(n)
space:- O(n)
"""
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 =[]

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        popped_item = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
        return popped_item
        

    def peek(self) -> int:
        return self.stack1[0]
        

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

## Complexity

- **Time:** O(N) — In the worst case, for `pop` and `peek` operations, all elements need to be transferred between stacks.
- **Space:** O(N) — The space complexity is determined by the storage required for the elements in the two stacks.
