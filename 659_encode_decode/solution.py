#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s:str) -> list[str]:
        res = []
        i = 0
        while i < len(s):

            # lets get the length of next encoded string
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])

            res.append(s[j+1:j+1+l]) # add 1 to skip # next to the number
            i = j + 1 + l
        return res


sol = Solution()
strs = ["lint", "code", "love", "you"]
print(f"sol: {sol.decode(sol.encode(strs)) == strs}")
