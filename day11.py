from helpers.utils import *

import numpy as np
import re
import math

from copy import deepcopy

from itertools import cycle, permutations


folder = "standard"  # "practice_2020" "standard"
day = 11
path = f"/home/magody/programming/AdventOfCode2021/files/{folder}/input{day}.txt"

inp = readMatrixTogether(path, mapping=int)
# inp = readArrayIgnoreBlankLines(path)
# inp = readArrayOneLine(path,int)

n = len(inp)
m = len(inp[0])

def is_invalid_range(a,b):
    return a<0 or b<0 or a>=n or b>=m
 
def solve1(steps):
    
    answer = 0
    
    for _ in range(steps):
        
        for i in range(n):
            for j in range(m):
                inp[i][j] += 1
        
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if inp[i][j] > 9:
                    
                    def dfs(inp,i,j):
                        
                        if is_invalid_range(i,j):
                            return 0
                        
                        if visited[i][j]:
                            return 0
                                                
                        count = 1
                        visited[i][j] = True
                        inp[i][j] = 0
                        
                        directions = [
                            [i-1,j-1],
                            [i-1,j],
                            [i-1,j+1],
                            [i,j+1],
                            [i+1,j+1],
                            [i+1,j],
                            [i+1,j-1],
                            [i,j-1],
                        ]
                        
                        for direction in directions:
                            new_i = direction[0]
                            new_j = direction[1]
                            if not is_invalid_range(new_i,new_j):
                                
                                if not visited[new_i][new_j]:
                                    inp[new_i][new_j] += 1
                                    
                                    if inp[new_i][new_j] > 9:
                                        # new flash in this direction
                                        count += dfs(inp, new_i, new_j)
                            
                                       
                        return count
                                        
                    answer += dfs(inp,i,j)
                    
    return answer

def solve2(steps):
    
    answer = 0
    
    for step in range(steps):
        
        for i in range(n):
            for j in range(m):
                inp[i][j] += 1
        
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if inp[i][j] > 9:
                    
                    def dfs(inp,i,j):
                        
                        if is_invalid_range(i,j):
                            return 0
                        
                        if visited[i][j]:
                            return 0
                                                
                        count = 1
                        visited[i][j] = True
                        inp[i][j] = 0
                        
                        directions = [
                            [i-1,j-1],
                            [i-1,j],
                            [i-1,j+1],
                            [i,j+1],
                            [i+1,j+1],
                            [i+1,j],
                            [i+1,j-1],
                            [i,j-1],
                        ]
                        
                        for direction in directions:
                            new_i = direction[0]
                            new_j = direction[1]
                            if not is_invalid_range(new_i,new_j):
                                
                                if not visited[new_i][new_j]:
                                    inp[new_i][new_j] += 1
                                    
                                    if inp[new_i][new_j] > 9:
                                        # new flash in this direction
                                        count += dfs(inp, new_i, new_j)
                            
                                       
                        return count
                                        
                    answer += dfs(inp,i,j)
        
        if np.sum(inp) == 0:
            return step
        
    return -1

# print(solve1(100))
print(solve2(1000000))

    
