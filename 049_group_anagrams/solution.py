#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = collections.defaultdict(list) # mapping charCount to list of anagrams

        for s in strs:
            # a...z. This list will be used as the key in res dict
            count = [0] * 26

            # calculate char count for the string
            for c in s:
                count[ord(c) - ord('a')] += 1

            # All strings with same char-count as key will be grouped together
            res[tuple(count)].append(s)

        return list(res.values())

sol = Solution()
print(f"sol: {sol.groupAnagrams(['eat','tea','tan','ate','nat','bat'])}")
print(f"sol: {sol.groupAnagrams([''])}")
print(f"sol: {sol.groupAnagrams(['a'])}")

