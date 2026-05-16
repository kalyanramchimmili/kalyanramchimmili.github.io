---
title: Evaluate Reverse Polish Notation
description: "Given an array of strings representing an arithmetic expression in Reverse Polish Notation (RPN), evaluate the expression and return the…"
tags: [Arrays, Stack]
---

# Evaluate Reverse Polish Notation

## Problem

Given an array of strings representing an arithmetic expression in Reverse Polish Notation (RPN), evaluate the expression and return the resulting integer. The expression can contain integers and the operators '+', '-', '*', '/'. Division should truncate towards zero.

## Approach

The solution uses a stack to evaluate the Reverse Polish Notation expression. When a number is encountered, it is pushed onto the stack. When an operator is encountered, the top two numbers are popped from the stack (the second popped number is the first operand, and the first popped number is the second operand). The operation is performed using these two numbers and the operator, and the result is pushed back onto the stack. Finally, the single remaining value on the stack is the result of the expression.

## Solution

```python
"""
1. The solution is using stack.
2. If it is a number push it to stack, else if it is any operator then, we will have to pop the 2 number n1 and n2
3. the top 2 numbers will be popped, n2 being the first and n1 being 2nd, we perform with the operators either by a switch/match case or if else
4. append the result back to stack
5. at last return stack[0] as the output.

time comp:- O(N)
space comp:- O(N)
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                n1 = int(stack.pop())
                n2 = int(stack.pop())

                if token == "+":
                    stack.append(n2 + n1)
                elif token == "-":
                    stack.append(n2 - n1)
                elif token == "*":
                    stack.append(n2 * n1)
                elif token == "/":
                    stack.append(int(n2 / n1))
            else:
                stack.append(int(token))

        return stack[0]
```

## Complexity

- **Time:** O(N) - We iterate through the tokens array once. Stack operations (push and pop) take constant time.
- **Space:** O(N) - In the worst case, if all tokens are numbers, the stack will store all of them.
