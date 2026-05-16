---
title: String to Integer (atoi)
description: "Implement the `myAtoi` function to convert a string to a 32-bit signed integer."
tags: [Strings, Math]
---

# String to Integer (atoi)

Implement the `myAtoi` function to convert a string to a 32-bit signed integer. The conversion involves ignoring leading whitespace, determining the sign, reading digits until a non-digit or end of string, and finally clamping the result to the 32-bit signed integer range.

## Approach

The author's notes outline a step-by-step process for implementing the `myAtoi` function. First, leading whitespace is skipped. Then, the sign (+ or -) is determined if present and the string `ans` is not already populated. Next, any non-digit characters encountered will cause the process to break. If digits are found, they are appended to the `ans` string. After iterating through the input string, if `ans` is empty or only contains a sign, 0 is returned. Otherwise, `ans` is converted to an integer and then checked against the 32-bit signed integer range, returning the clamped value if it falls outside.

## Solution

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ""
        for char in s:
            if char == " ":
                if ans == "":
                    continue
                else:
                    break
            elif char == "-" or char == "+":
                if ans != "":
                    break
                else:
                    ans += char
            elif not char.isdigit():
                break
            else:
                ans += char

        if ans == "" or ans == "+" or ans == "-":
            return 0

        res = int(ans)
        if res > (2**31)-1 :
            return (2**31)-1
        elif res < (-2**31):
            return (-2**31)
        else:
            return res
```

## Complexity

- **Time:** O(N) — We iterate through the input string `s` once.
- **Space:** O(N) — In the worst case, the `ans` string can store all characters of `s` if they are all valid for conversion.
