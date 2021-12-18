
import itertools
from itertools import cycle, permutations
import math
from helpers.utils import *

import numpy as np
import re

from copy import deepcopy

from collections import defaultdict, Counter, deque
from queue import PriorityQueue
import heapq


folder = "standard"  # "practice_2020" "standard"
day = 18
path = f"/home/magody/programming/AdventOfCode2021/files/{folder}/input{day}.txt"




def isList(value):
    return str(type(value)) == "<class 'list'>"

def solve1(arrays):




    def mapreduce(arr):
        changed = False
        
        stack1 = []
        stack2 = []
        
        arr_new = deepcopy(arr)
        
        level = 0
        for i in range(len(arr)):
            
            element = arr[i]
            if re.match("\d", element):
                value = int(element)
                stack1.append(value)
                
                # SPLIT
                if value >= 10:
                    
                    changed = True
                    up = math.ceil(value/2)
                    down = math.floor(value/2)
                    arr_new = f"{arr[:i]}[{down},{up}]{arr[i+1:]}"
                    break
                
            elif element == "[":
                level += 1
            elif element == "]":
                level -= 1
                
            if level == 5:
                # explode
                if len(stack1) > 0:
                    # exist number
                    j = i
                    carry = int(arr[j])
                    element2 = arr[j]
                    while not re.match("\d", element2):
                        j -= 1
                        element2 = arr[j]
                        
                    total = carry + stack1.pop()
                    arr_new = f"{arr[:j]}{total}{arr[i+1:]}"
                else:
                    arr_new = f"{arr[:i]}0{arr[i+1:]}"
                    
            
            stack2.append(element)
            
        return arr_new, changed

    

    """
    
    res = arrays[0]

    for i in range(1, len(arrays)):
        array = arrays[i]
        res = f"[{res},{array}]"
        
        can_reduce = True
        while can_reduce:
                    
            res, can_reduce = mapreduce(res)
            can_reduce = not can_reduce

                
        
    print(res)
    [[[[[1,1],[2,2]],[3,3]],[4,4]],[5,5]]
    [[[[0,[3,2]],[3,3]],[4,4]],[5,5]]
    [[[[3,0],[5,3]],[4,4]],[5,5]]

    With two stacks:

    stackn: 0,3,2,3,3,4,4,5,5
    stack: [[[[0,[3,2]],[3,3]],[4,4]],[5,5]]


    stackn: 0
    stack: [[[[3,0],[5,3]],[4,4]],[5,5]]
    """


    def explode(number, n):
        changed = False
        if not isList(number):
            return changed, None, number, None, -1
        if n == 0:
            changed = True
            return changed, number[0], 0, number[1], -1
        l, r = number
        changed, left, l, right, corr = explode(l, n - 1)
        
        def searchL(number, n):
            if n is None:
                return number
            if not isList(number):
                return number + n
            return [searchL(number[0], n), number[1]]


        def searchR(number, n):
            if n is None:
                return number
            if not isList(number):
                return number + n
            return [number[0], searchR(number[1], n)]
        
        if changed:
            return changed, left, [l, searchL(r, right)], None, 1
        changed, left, r, right, corr = explode(r, n - 1)
        if changed:
            return changed, None, [searchR(l, left), r], right, 1
        return changed, None, number, None, -1


    def split(number):
        changed = False
        if not isList(number):
            if number >= 10:
                div = number/2
                changed = True
                return changed, [math.floor(div), math.ceil(div)]
            return changed, number
        l, r = number
        changed, l = split(l)
        if changed:
            return changed, [l, r]
        changed, r = split(r)
        return changed, [l, r]


    def sumnum(array1, array2):
        res = [array1, array2]
        
        changed = True
        
        while changed:
            changed, left, res, right, corr = explode(res, 4)
            if corr:
                # print("corr")
                pass
            if changed:
                # only a explode or split allowed by iteration
                continue
            changed, res = split(res)
        return res

    res = eval(arrays[0])

    for i in range(1, len(arrays)):
        array = eval(arrays[i])
        
        # map-reduce, left to right. Hadoop like...
        res = sumnum(res, array)
        

    # 15 min penalty ptm :'v
    def getMagnitude(number):
        
        if not isList(number):
            # regular number, direct to result
            return number
        return 3 * getMagnitude(number[0]) + 2 * getMagnitude(number[1])

    return getMagnitude(res)

def solve2(arrays):
    
    
    def explode(number, n):
        changed = False
        if not isList(number):
            return changed, None, number, None, -1
        if n == 0:
            changed = True
            return changed, number[0], 0, number[1], -1
        l, r = number
        changed, left, l, right, corr = explode(l, n - 1)
        
        def searchL(number, n):
            if n is None:
                return number
            if not isList(number):
                return number + n
            return [searchL(number[0], n), number[1]]


        def searchR(number, n):
            if n is None:
                return number
            if not isList(number):
                return number + n
            return [number[0], searchR(number[1], n)]
        
        if changed:
            return changed, left, [l, searchL(r, right)], None, 1
        changed, left, r, right, corr = explode(r, n - 1)
        if changed:
            return changed, None, [searchR(l, left), r], right, 1
        return changed, None, number, None, -1

    def split(number):
        changed = False
        if not isList(number):
            if number >= 10:
                div = number/2
                changed = True
                return changed, [math.floor(div), math.ceil(div)]
            return changed, number
        l, r = number
        changed, l = split(l)
        if changed:
            return changed, [l, r]
        changed, r = split(r)
        return changed, [l, r]


    def sumnum(array1, array2):
        res = [array1, array2]
        
        changed = True
        
        while changed:
            changed, left, res, right, corr = explode(res, 4)
            if corr:
                # print("corr")
                pass
            if changed:
                # only a explode or split allowed by iteration
                continue
            changed, res = split(res)
        return res
    
    # 15 min penalty ptm :'v
    def getMagnitude(number):
        
        if not isList(number):
            # regular number, direct to result
            return number
        return 3 * getMagnitude(number[0]) + 2 * getMagnitude(number[1])

    arrays = list(map(eval, arrays))
    answer = 0
    
    # permutations of two
    for i in range(len(arrays)-1):
        for j in range(1,len(arrays)):
            
            if i == j:
                continue
            # addition is not commutative - x + y and y + x can produce different results.
            x = arrays[i]
            y = arrays[j]
            # map-reduce, left to right. Hadoop like...
            
            answer = max(answer, getMagnitude(sumnum(x, y)), getMagnitude(sumnum(y, x)))
        
        

    

    return answer
    
arrays = readArray(path)
print(solve1(arrays))
arrays = readArray(path)
print(solve2(arrays))