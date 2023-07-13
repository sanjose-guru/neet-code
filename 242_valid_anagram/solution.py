#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = collections.Counter()
        tChars =collections.Counter()

        if len(s) != len(t):
            return False

        for i in range(0, len(s)):
            sChars[s[i]] += 1
            tChars[t[i]] += 1

        return sChars == tChars

sol = Solution()
print(f"sol: {sol.isAnagram('anagram', 'nagaram')}")
print(f"sol: {sol.isAnagram('rat', 'car')}")
