#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = collections.Counter(nums)
        # most_common will return a tuple of value and its frequency
        # Do a list compression to just return the values
        return [x[0] for x in freq.most_common(k)]

    def topKFrequentAlt(self, nums: list[int], k: int) -> list[int]:
        freq = collections.defaultdict(int) # for counting frequency of each nums

        maxF = 0  # maximum frequency so far (will be used to initialize the fNums
        for n in nums:
            freq[n] += 1
            if maxF < freq[n]: 
                maxF = freq[n]  # keep track of maximum frequency 

        fNums = [[] for i in range(maxF)]  # list of numbers by their frequency
        for n,f in freq.items():
            fNums[f-1].append(n)  # list starts from 0, frequency starts from 1 (so offset by 1)

        res = []
        for l in fNums[::-1]:
            for n in l:
                res.append(n)
                if len(res) == k:
                    return res

        return res


sol = Solution()
print(f"sol: {sol.topKFrequent([1,1,1,2,2,3], 2)}")
print(f"sol: {sol.topKFrequent([1], 1)}")
print(f"sol: {sol.topKFrequent([1,1,2,2,4,4,4], 2)}")
print(f"AltSol: {sol.topKFrequentAlt([1,1,1,2,2,3], 2)}")
print(f"AltSol: {sol.topKFrequentAlt([1], 1)}")
print(f"AltSol: {sol.topKFrequentAlt([1,1,2,2,4,4,4], 2)}")
