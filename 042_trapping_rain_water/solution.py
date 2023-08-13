#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def trap(self, height: list[int]) -> int:

        # if input it empty return 0
        if not height:
            return 0

        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]  # Initialize to boundaries
        res = 0

        while (l < r):
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                res += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                res += rMax - height[r]

        return res

sol = Solution()
print(f"{sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6}")
print(f"{sol.trap([4,2,0,3,2,5]) == 9}")
print(f"{sol.trap([0,2,1,0]) == 0}")
