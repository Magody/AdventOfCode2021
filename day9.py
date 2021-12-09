from helpers.utils import *

import numpy as np
import re

from copy import deepcopy

from itertools import cycle, permutations


folder = "standard"  # "practice_2020" "standard"
day = 9
path = f"/home/magody/programming/AdventOfCode2021/files/{folder}/input{day}.txt"

inp = readMatrixTogether(path, mapping="none")
# inp = readArrayIgnoreBlankLines(path)
# inp = readArrayOneLine(path,int)


 
def solve1(inp):

    answer = 0

    
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            
            value = int(inp[i][j])
            
            up = i-1
            right = j+1
            down = i +1
            left = j - 1
            
            if up >= 0 and int(inp[up][j]) <= value:
                continue
            if right < len(inp[0]) and int(inp[i][right]) <= value:
                continue
            if down < len(inp) and int(inp[down][j]) <= value:
                continue
            if left >= 0 and int(inp[i][left]) <= value:
                continue
            
            answer += value + 1 
            
    
        
    return answer

def solve2(inp):
    
    answer = 0

    values = []
    
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            
            def dfs(a, i, j):
                
                if i < 0 or i >= len(a) or j < 0 or j >= len(a[0]):
                    return 0
                
                if a[i][j] == 9:
                    return 0
                
                inp[i][j] = 9
                res = 1
                
                res += dfs(inp,i-1,j)
                res += dfs(inp,i,j+1)
                res += dfs(inp,i+1,j)
                res += dfs(inp,i,j-1)
                return res
            
            if inp[i][j] != 9:
                values.append(dfs(inp, i, j))
            
    values.sort()
    
    
    
        
    return values[-1] * values[-2] * values[-3]


print(solve2(inp))