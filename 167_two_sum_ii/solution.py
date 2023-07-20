#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -=1
            elif sum < target:
                l += 1
            else: # we found the sum
                return [l+1, r+1]


sol = Solution()
numbers, target = [2,7,11,15], 9
print(f"sol: {sol.twoSum(numbers, target) == [1, 2]}")
numbers, target = [2,3,4], 6
print(f"sol: {sol.twoSum(numbers, target) == [1, 3]}")
numbers, target = [-1,0], -1
print(f"sol: {sol.twoSum(numbers, target) == [1, 2]}")
