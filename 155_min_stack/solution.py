#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections

class MinStack:

    def __init__(self):
        self.s = []
        self.mS = []
        
    def push(self, val: int) -> None:
        self.s.append(val)
        self.mS.append(min(val, self.mS[-1] if self.mS else val))

    def pop(self) -> None:
        self.mS.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]        

    def getMin(self) -> int:
        return self.mS[-1]
        

minStack = MinStack()
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print(f"{minStack.getMin() == -3}")
minStack.pop();
print(f"{minStack.top() == 0}")
print(f"{minStack.getMin() == -2}")
