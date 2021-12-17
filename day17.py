from helpers.utils import *

import numpy as np
import re
import math

from copy import deepcopy

from itertools import cycle, permutations
from collections import defaultdict, Counter, deque
from queue import PriorityQueue
import heapq


folder = "standard"  # "practice_2020" "standard"
day = 17
path = f"/home/magody/programming/AdventOfCode2021/files/{folder}/input{day}.txt"

f = open(path, "r")
f_in = f.read()
f.close()

_,c = f_in.split(": ")
x,y = c.split(", ")
x1,x2 = map(int, x[2:].split(".."))
y1,y2 = map(int, y[2:].split(".."))


def isInside(xt,yt,x1,x2,y1,y2):
    return xt >= x1 and xt <=x2 and yt >= y1 and yt <= y2

def isPassed(xt,yt,x1,x2,y1,y2):
    return xt > x2 or yt < y1


def solve(x1,x2,y1,y2):
    
    answer = 0
    best_high = -math.inf
    
    
    print(x1,x2,y1,y2)

    
    for xv in range(-400,400):
        for yv in range(-400,400):
            
                
            xt = 0
            yt = 0
            
            dx = -1 if xv > 0 else 1
            dy = -1 if yv > 0 else 1
            
            
            possible = True
            high = 0
            iteration = 0
            while possible:
                
                if isInside(xt,yt,x1,x2,y1,y2):
                    
                    answer += 1
                    # print(xv,yv)
                    break
                elif isPassed(xt,yt,x1,x2,y1,y2):
                    possible = False
                    break
                
                if dx == -1:
                    xt = xt + max(0, xv + iteration * dx)
                else:
                    xt = xt + min(0, xv + iteration * dx)
                    
                yt = yt + (yv - iteration) 
                iteration += 1
                high = max(high,yt)
            if possible:
                if high > best_high:
                    best_high = max(best_high, high)
                    print(best_high)
                
    
    
    return best_high, answer



print(solve(x1,x2,y1,y2))