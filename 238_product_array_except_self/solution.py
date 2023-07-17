#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)  # initialize an array with 1 (multiplying with 1 will give same answer)

        # calculate product of all prefix
        p = 1
        for i in range(len(nums)):
            res[i] = p
            p *= nums[i]

        # calculate product of prefix and suffix
        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= p
            p *= nums[i]

        return res


sol = Solution()
print(f"sol: {sol.productExceptSelf([1,2,3,4])}")
print(f"sol: {sol.productExceptSelf([-1,1,0,-3,3])}")
