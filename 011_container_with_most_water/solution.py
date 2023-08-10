#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def maxArea(self, height: list[int]) -> int:
        mx = 0
        l, r = 0, len(height) - 1

        while l < r:
            a = (r-l) * min(height[l], height[r])
            if a > mx:
                mx = a
            if (height[l] > height[r]):
                r -= 1
            else:
                l += 1

        return mx



sol = Solution()
print(f"{sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49}")
print(f"{sol.maxArea([1,1]) == 1}")
