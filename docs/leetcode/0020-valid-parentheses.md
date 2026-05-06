---
title: Valid Parentheses
tags: [Stack, String]
---

# Valid Parentheses

## Problem

Given a string containing only parentheses, determine if the brackets are correctly matched and ordered. This means every opening bracket must have a corresponding closing bracket of the same type, and they must close in the correct sequence.

## Approach

The problem can be solved using a stack. When an opening bracket is encountered, it is pushed onto the stack. When a closing bracket is encountered, we check if the stack is not empty and if the top of the stack contains the corresponding opening bracket. If they match, the top element is popped from the stack. If there is a mismatch or the stack is empty, the string is invalid. Finally, after processing the entire string, if the stack is empty, it means all brackets were correctly matched, and the string is valid; otherwise, it is invalid.

## Solution

```python
"""
1. Stack solution, if opening brackets push it in stack, if not check the closing brackets match with opening ones and stack is not empty, if so stack.pop

2. if any mismatch with brackets then return False, check if stack is empty at the end, if so pass true else false

time comp:- O(N)
space comp:- O(N)
"""
class Solution:
    def isValid(self, char: str) -> bool:
        stack = []
        for s in char:
            if s == "(" or s == "[" or s == "{":
                stack.append(s)
            else:
                if stack and (
                    (s == ")" and stack[-1] == "(")
                    or (s == "]" and stack[-1] == "[")
                    or (s == "}" and stack[-1] == "{")
                ):
                    stack.pop()
                else:
                    return False

        return not stack
```

## Complexity

- **Time:** O(N) — We iterate through the string once, and stack operations (push/pop) take O(1) time.
- **Space:** O(N) — In the worst case (e.g., a string with all opening brackets), the stack can grow up to the size of the input string.
