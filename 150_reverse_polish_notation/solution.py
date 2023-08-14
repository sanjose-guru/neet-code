#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stk = collections.deque()

        for c in tokens:
            if c in ops:
                a,b = stk.pop(), stk.pop()
                if c == "+":
                    stk.append(b+a)
                elif c == "-":
                    stk.append(b-a)
                elif c == "*":
                    stk.append(b*a)
                elif c == "/":
                    stk.append(int(b/a))  # // in python3 does a floor division https://stackoverflow.com/questions/5535206/negative-integer-division-surprising-result
            else:
                stk.append(int(c))

        return stk[-1]

sol = Solution()
print(f"{sol.evalRPN(['2','1','+','3','*']) == 9}")
print(f"{sol.evalRPN(['4','13','5','/','+']) == 6}")
print(f"{sol.evalRPN(['10','6','9','3','+','-11','*','/','*','17','+','5','+']) == 22}")
