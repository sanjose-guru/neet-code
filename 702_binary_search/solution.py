#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1

sol = Solution()
print(f"{sol.search([-1,0,3,5,9,12], 9) == 4}")
print(f"{sol.search([-1,0,3,5,9,12], 2) == -1}")
