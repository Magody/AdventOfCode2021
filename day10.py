from helpers.utils import *

import numpy as np
import re

from copy import deepcopy

from itertools import cycle, permutations


folder = "standard"  # "practice_2020" "standard"
day = 10
path = f"/home/magody/programming/AdventOfCode2021/files/{folder}/input{day}.txt"

inp = readArray(path, mapping="none")
# inp = readArrayIgnoreBlankLines(path)
# inp = readArrayOneLine(path,int)

d = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

d2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}



op = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}


op2 = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
 
def solve1(inp):
    
    

    answer = 0
    
    for case in inp:
        stack = []
        
        for element in case:
            
            if element in ["[","(","{","<"]:
                stack.append(element)
            else:
                if op[element] == stack[-1]:
                    stack.pop(-1)
                else:
                    answer += d[element]
                    break
        
    return answer

def solve2(inp):
    

    scores = []
    
    for case in inp:
        stack = []
        
        answer = 0
        is_corrupted = False
        for element in case:
            
            if element in ["[","(","{","<"]:
                stack.append(element)
            else:
                if op[element] == stack[-1]:
                    stack.pop(-1)
                else:
                    is_corrupted = True
        
        if not is_corrupted:            
            for value in stack[::-1]:
                el = op2[value]
                answer *= 5
                answer += d2[el]
                #print(answer)
            
            scores.append(answer)
            
        
    
    scores.sort()
    
        
    return scores[len(scores)//2]


print(solve2(inp))