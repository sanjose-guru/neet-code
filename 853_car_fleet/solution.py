#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # create a combined list of both position and speed
        cars = [[p, s] for p,s in zip(position, speed)]

        # sort the list by position (1st item in p,s) so that we can work from 
        # the reverse positions. Car at the last position will gate other cars
        cars.sort()

        aTimes = []
        while cars:
            p, s = cars.pop()
            aTimes.append((target-p)/s)

        fleets = 0
        maxT = 0
        for t in aTimes:
            if t > maxT: # if the car is slower than previous ones, it will create a new fleet.
                fleets += 1
                maxT = t
        return fleets


sol = Solution()
print(f"{sol.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3}")
print(f"{sol.carFleet(10, [3], [3]) == 1}")
print(f"{sol.carFleet(100, [0,2,4], [4,2,1]) == 1}")
