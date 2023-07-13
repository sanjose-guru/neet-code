#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = collections.defaultdict(list) # mapping charCount to list of anagrams

        for s in strs:
            count = [0] * 26 # a...z. This list will be used a key in res dict

            # the char count list will be the key in res dict, 
            # All strings with same char count will grouped in res
            for c in s:
                count[ord(c) - ord('a')] += 1

            # All strings with same char count will grouped under same key
            res[tuple(count)].append(s)

        return list(res.values())

sol = Solution()
print(f"sol: {sol.groupAnagrams(['eat','tea','tan','ate','nat','bat'])}")
print(f"sol: {sol.groupAnagrams([''])}")
print(f"sol: {sol.groupAnagrams(['a'])}")

