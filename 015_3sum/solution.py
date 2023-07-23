#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        ln = len(nums)

        for i, n in enumerate(nums):
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, ln-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else: # we found a triplet
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                # skip duplicate
                while nums[l] == nums[l-1] and l < r:
                    l += 1
                # we can skip duplicate check for r as we did for i & l so triplet will be unique
        return res


sol = Solution()
nums = [-1,0,1,2,-1,-4]
print(f"sol: {sol.threeSum(nums) == [[-1,-1,2],[-1,0,1]]}")
nums = [0,1,1]
print(f"sol: {sol.threeSum(nums) == []}")
nums = [0,0,0]
print(f"sol: {sol.threeSum(nums) == [[0,0,0]]}")
