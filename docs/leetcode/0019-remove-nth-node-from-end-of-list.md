---
title: Remove Nth Node From End of List
tags: [Linked List, Two Pointers]
---

# Remove Nth Node From End of List

## Problem

Given the head of a linked list, remove the nth node from the end of the list and return its head.

## Approach

This problem can be solved using a two-pointer approach. Both pointers, `fast` and `slow`, are initialized at the head of the list. The `fast` pointer is then moved `n` steps ahead of the `slow` pointer. This creates a gap of `n` nodes between them.

If, after moving `fast` `n` steps, it becomes `None`, it means we need to remove the head node (i.e., the length of the list is `n`). In this case, we return `head.next`.

Otherwise, we move both `fast` and `slow` pointers one step at a time until `fast.next` is `None`. At this point, the `slow` pointer will be pointing to the node *before* the node we need to remove. We then bypass the node to be removed by setting `slow.next` to `slow.next.next`. Finally, we return the original `head` of the list.

## Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head

        # Handle the edge case where the list has only one node and we need to remove it
        if fast.next == None and n == 1:
            head = head.next
            return head

        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # If fast is None, it means we need to remove the head node
        if not fast:
            return head.next

        # Move both pointers until fast reaches the end of the list
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from the end
        slow.next = slow.next.next
        return head
```

## Complexity

- **Time:** O(L) — We traverse the list at most twice (once for the fast pointer to reach the end, and implicitly once for the slow pointer).
- **Space:** O(1) — We only use a constant amount of extra space for the two pointers.
