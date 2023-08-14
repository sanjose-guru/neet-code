#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    # o(n2) solution
    def dailyTemperatures1(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            for j in range(i+1, len(temperatures)):  # range will skip the last value so don't need to do len(list)-1
                if temperatures[j] > t:
                    res[i] = j - i
                    break
        return res

    # o(n) solution
    # pass through the list, if 
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stk = []  # will save temperatures for which next highest temp is not found yet.

        for i, t in enumerate(temperatures):
            # If current temp is greater than previous values in the stack,
            # we found the next day with high temp for that value on top of 
            # the stack. Pop the entry from the stack and update the result
            # for that day with the difference between the index.
            while stk and t > stk[-1][1]:
                j,v = stk.pop()
                res[j] = i - j
            stk.append([i,t])

        return res


sol = Solution()
print(f"{sol.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]}")
print(f"{sol.dailyTemperatures([30,40,50,60]) == [1,1,1,0]}")
print(f"{sol.dailyTemperatures([30,60,90]) == [1,1,0]}")
