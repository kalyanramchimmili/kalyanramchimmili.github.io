---
title: Linked List Cycle
description: "Given the head of a linked list, determine if there's a cycle present."
tags: [Linked Lists, Two Pointers]
---

# Linked List Cycle

## Problem

Given the head of a linked list, determine if there's a cycle present. A cycle exists if any node can be reached again by following the `next` pointers.

## Approach

The approach uses two pointers, a `slow` pointer that moves one step at a time and a `fast` pointer that moves two steps at a time. If there is a cycle, the `fast` pointer will eventually catch up to the `slow` pointer. Edge cases are handled by checking for an empty list or a list with only one node.

## Solution

```python
"""
1. slow and fast pointers, inc fast pointer by 2 steps and slow by 1
2. if they meet then there is loop, if not no loop, check he intial condition, if we have no nodes in ll and only one node with no cycle and return false early

time comp:- o(n)
space :- o(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if (not head) or (not head.next):
            return False

        fast = head.next
        slow = head

        while fast and fast.next:
            if fast == slow:
                return True

            fast = fast.next.next
            slow = slow.next

        return False
```

## Complexity

- **Time:** O(n) — In the worst case, the fast pointer traverses the list twice.
- **Space:** O(1) — Only a constant amount of extra space is used for the pointers.
