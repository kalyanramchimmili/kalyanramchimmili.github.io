---
title: Middle of the Linked List
tags: [Linked List]
---

# Middle of the Linked List

## Problem

Given the head of a singly linked list, find and return the middle node. If there are two middle nodes, return the second one.

## Approach

The problem can be solved using the fast and slow pointer technique. We initialize two pointers, `fast` and `slow`, both pointing to the head of the linked list. The `fast` pointer moves two steps at a time, while the `slow` pointer moves one step at a time.

When the `fast` pointer reaches the end of the list (or one step before the end), the `slow` pointer will be at the middle node.

For linked lists with an even number of nodes, the `fast` pointer will end up at the second-to-last node. In this case, we advance the `slow` pointer one more step to point to the actual second middle node before returning it.

## Solution

```python
"""
1. fast and slow pointer method, move fast pointer to 2 steps and slow to one
2. for even ll, fast would be at n-1 node, so if fast.next exists, then move slow one step further and return slow

time comp:- O(N)
space comp:- O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if fast.next:
            slow = slow.next
        
        return slow
```

## Complexity

- **Time:** O(N) — We traverse the linked list at most once.
- **Space:** O(1) — We only use a constant amount of extra space for the pointers.
