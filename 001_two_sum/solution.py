#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lookedUp = dict()
        for i,n in enumerate(nums):
            diff = target - n
            if diff in lookedUp:
                return [lookedUp[diff], i]
            lookedUp[n] = i
        return []

sol = Solution()
print(f"Sol: {sol.twoSum([2,7,11,15], 9)}")
print(f"Sol: {sol.twoSum([3,2,4], 6)}")
print(f"Sol: {sol.twoSum([3,3], 6)}")
