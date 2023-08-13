#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections

class Solution:
    def isValid(self, s: str) -> bool:
        sB = {
            "{" : "}",
            "(" : ")",
            "[" : "]",
        }
        eB = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        stk = collections.deque()

        for c in s:
            if c in sB:
                stk.append(c)
            if c in eB:
                if not stk:
                    return False
                if stk.pop() != eB[c]:
                    return False

        if len(stk) == 0:
            return True
        return False
    
sol = Solution()
print(f"{sol.isValid('()') == True}")
print(f"{sol.isValid('()[]{}') == True}")
print(f"{sol.isValid('({[]})') == True}")
print(f"{sol.isValid('(]') == False}")
print(f"{sol.isValid('({[}])') == False}")
print(f"{sol.isValid(')') == False}")
