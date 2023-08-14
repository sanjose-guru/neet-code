#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    # we will start with a open parenthesis, from there we will branch
    # of to possible combinations of parenthesis.
    def generateParenthesis(self, n: int) -> list[str]:

        tre = []  # we will generate a tree of combinations

        def builder(s: str, pOpen, pClose: int) -> str:
            # if number of open and closed parenthesis matches to n we
            # we are done with this combination (node), add to tre and return.
            if pOpen == pClose == n:
                tre.append(s)
                return 

            # If number of open parenthesis is less then n we can branch off
            # by adding one more open parenthesis.
            if pOpen < n:
                builder(f'{s}(', pOpen+1, pClose)

            # we can add close parenthesis only when its count in less then
            # number of opened.
            if pClose < pOpen:
                builder(f'{s})', pOpen, pClose+1)

        builder("", 0, 0)
        return tre

sol = Solution()
print(f'{sol.generateParenthesis(1) == ["()"]}')
print(f'{sol.generateParenthesis(2) == ["(())", "()()"]}')
print(f'{sol.generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]}')
