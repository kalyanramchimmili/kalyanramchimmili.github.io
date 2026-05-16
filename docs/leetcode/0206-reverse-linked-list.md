---
title: Reverse Linked List
description: "Given the head of a singly linked list, reverse the list and return the head of the reversed list."
tags: [Linked List, Iteration, Recursion]
---

# Reverse Linked List

## Problem

Given the head of a singly linked list, reverse the list and return the head of the reversed list.

## Approach

The approach uses three pointers to reverse the linked list iteratively.
1. `ptr1` is a pointer that will eventually point to the new head of the reversed list. It starts as `None`.
2. `ptr2` is the current node being processed. It starts at the original `head`.
3. `ptr3` is used to keep track of the next node to visit, allowing traversal without losing the rest of the list. It also starts at the original `head`.

The algorithm iterates as long as `ptr3` is not `None`. In each iteration, `ptr3` moves to the next node. Then, `ptr2`'s `next` pointer is redirected to point to `ptr1`, effectively reversing the link. Subsequently, `ptr1` is updated to `ptr2`, and `ptr2` is updated to `ptr3` for the next iteration. When the loop finishes, `ptr1` will be pointing to the last node of the original list, which is the head of the reversed list.

## Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
1. 3 pointers, 1st pointer is ref node to reverse to, 2nd pointer is the current element to reverse, 3rd element is next element to traverse to
2. start with null, head, head for ptr1 , 2 ,3 
3. if ptr3 is true, move ptr3 to next, ptr2.next to ptr1, ptr1 would be ptr2 and ptr2 would go to ptr3 pos
4. to return head return ptr1, ptr2 and 3 would have gone to null when checking for last node.

time comp:- O(N)
space comp:- O(1)
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = None
        ptr2 = head
        ptr3 = head
        while ptr3:
            ptr3 = ptr3.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = ptr3
        
        return ptr1
```

## Complexity

- **Time:** O(N) — We iterate through the linked list once.
- **Space:** O(1) — We only use a constant amount of extra space for the three pointers.
