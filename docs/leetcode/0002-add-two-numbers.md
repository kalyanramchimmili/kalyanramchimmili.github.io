---
title: Add Two Numbers
description: "Given two non-empty linked lists representing non-negative integers in reverse order, add them and return the sum as a new linked list."
tags: [Linked Lists, Arithmetic]
---

# Add Two Numbers

## Problem

Given two non-empty linked lists representing non-negative integers in reverse order, add them and return the sum as a new linked list. Each node contains a single digit, and the lists do not have leading zeros.

## Approach

_(approach inferred from code — author notes were empty)_
The solution iterates through both linked lists simultaneously, simulating manual addition with a carry-over. A dummy head node simplifies the construction of the result linked list. For each position, it sums the digits from both lists (treating missing digits as 0) and the carry from the previous step. The unit digit of this sum becomes the value of the new node in the result list, and the tens digit becomes the carry for the next iteration. This process continues until both lists are exhausted and there's no remaining carry.

## Solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        current = ans
        prev_rem = 0
        
        while l1 or l2 or prev_rem:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + prev_rem
            prev_rem = total//10
            total = total%10
            
            current.next = ListNode(total)
            current = current.next

            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
        
        return ans.next
```

## Complexity

- **Time:** O(max(N, M)) — where N and M are the lengths of the two linked lists. We iterate through each list once.
- **Space:** O(max(N, M)) — for the new linked list that stores the sum. In the worst case, the sum list can be one element longer than the longer of the two input lists.
