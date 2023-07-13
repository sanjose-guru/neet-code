#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        present = set()

        for n in nums:
            if n in present:
                return True
            present.add(n)
        return False

sol = Solution()
print(f"sol: {sol.containsDuplicate([1,2,3,1])}")
print(f"sol: {sol.containsDuplicate([1,2,3,4])}")
print(f"sol: {sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2])}")

