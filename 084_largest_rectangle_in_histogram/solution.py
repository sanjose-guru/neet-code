#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # if there is no item in stack add this index and height
        # if h is higher than previous add its index and height to stack
        # if this height is lower than previous in stack, previous height cannot extend.
        #   * pop the item from stack
        #   * calculate area with previous h, store if max height.
        #   * extending current height back:
        #       * we should run the pop as a loop until we removed all heights taller than current
        #       * the loop will stop when stack height is equal to current
        #       * add current h with the index of last we popped from stack (the height being taller, we can extend current h from that point)
        #       * if lower calculate area with previous index, store max area if high, else extend new h with previous index
        maxA = 0
        stk = []  # while hold [index, height]

        for i,h in enumerate(heights):
            lpi = i # last popped index

            while stk and stk[-1][1] > h:
                pi, ph = stk.pop()
                print(f"popped: {pi, ph}")
                a =  (i - pi) * ph
                if a > maxA:
                    maxA = a
                    print(f"updated maxA: {maxA}")
                lpi = pi

            print(f"adding: {lpi, h}")
            stk.append([lpi, h])
            
        # empty the stack
        print("emptying stack")
        while stk:
            pi, ph = stk.pop()
            print(f"popped: {pi, ph}")
            a = (len(heights) - pi) * ph
            if a > maxA:
                maxA = a
                print(f"updated maxA: {maxA}")
        print(f"final maxA: {maxA}")
        return maxA


sol = Solution()
print(f"{sol.largestRectangleArea([2,1,5,6,2,3]) == 10}")
print(f"{sol.largestRectangleArea([2,4]) == 4}")
print(f"{sol.largestRectangleArea([3,5]) == 6}")
