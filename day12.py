from helpers.utils import *

import numpy as np
import re
import math

from copy import deepcopy

from itertools import cycle, permutations
from collections import defaultdict, Counter, deque


folder = "standard"  # "practice_2020" "standard"
day = 12
path = f"/home/magody/programming/AdventOfCode2021/files/{folder}/input{day}.txt"

inp = readArray(path)

graph = defaultdict(list)

for line in inp:
    a,b = line.split('-')
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()
    

def solve1():
    
    def dfs(node: str, visited: list):
        
        if node in visited:
            return 0
        
        if node == "end":
            return 1
    
        is_lower = node.lower() == node
        is_start = node == "start"
        
        if is_lower:
            visited.append(node)
            
        count = 0
        for child in graph[node]:
            count += dfs(child, visited)
        
        
        if is_lower and not is_start:
            visited.remove(node) 
        return count
    
    return dfs("start", [])
    


def solve2():
    
    debug = []
    
    def dfs(node: str, visited: dict, twice_made):
        
        if node == "end":
            # print(debug)
            return 1
        
        is_visited = visited.get(node, 0) > 0
        
        twice = twice_made
        
        is_lower = node.lower() == node
        is_start = node == "start"
        
        if is_visited:
            if is_start:
                return 0
            if twice_made:
                return 0
            
        if is_lower:
            if is_visited:
                visited[node] += 1
                twice = visited[node] == 2 or twice_made 
            else:
                visited[node] = 1
        
        # debug.append(node)
        count = 0
        for child in graph[node]:
            count += dfs(child, visited, twice)
        
        
        if is_lower and not is_start:
            visited[node] -= 1
            
        # debug.pop(-1)
        
        return count
    
    return dfs("start", dict(), False)


print(solve1())
print(solve2())