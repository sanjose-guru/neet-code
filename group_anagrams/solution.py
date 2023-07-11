#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    res = collections.defaultdict(list) # mapping charCount to list of anagrams

    for s in strs:
      count = [0] * 26 # a...z
      print(f"count: {count}")

      for c in s:
        count[ord(c) - ord('a')] += 1
      print(f"count: {count}")

      res[tuple(count)].append(s)

    print(f"res: {res}")
    return res.values()

sol = Solution()
print(f"sol: {sol.groupAnagrams(['eat','tea','tan','ate','nat','bat'])}")

