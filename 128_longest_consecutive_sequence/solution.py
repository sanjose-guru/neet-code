#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # if we have a previous number, this number is not start of the sequence
            if (n-1) not in numSet:
                l = 0 # start counter for calculating this sequence's length
                while (n+l) in numSet: # continue until we find next number in sequence
                    l += 1
                if l > longest:
                    longest = l
        return longest

sol = Solution()
nums = [100,4,200,1,3,2]
print(f"sol: {sol.longestConsecutive(nums) == 4}")
nums = [0,3,7,2,5,8,4,6,0,1]
print(f"sol: {sol.longestConsecutive(nums) == 9}")



