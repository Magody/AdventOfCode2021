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
day = 15
path = f"/home/magody/programming/AdventOfCode2021/files/{folder}/input{day}.txt"


matrix = readMatrixTogether(path,mapping=int)

memo = dict()

def dijkstra(g, s, t):

    q = []
    d = {k: math.inf for k in g.keys()}
    p = {}

    d[s] = 0 
    heapq.heappush(q, (0, s))

    while q:
        last_w, curr_v = heapq.heappop(q)
        for n, n_w in g[curr_v]:
            cand_w = last_w + n_w
            if cand_w < d[n]:
                d[n] = cand_w
                p[n] = curr_v
                heapq.heappush(q, (cand_w, n))

    return d[t]


def solve1(inp):
    
    n = len(inp)
    m = len(inp[0])


    inp[0][0] = 0
    
    names = [[-1 for _ in range(n)] for _ in range(m)]
    c = 0
    for i in range(n):
        for j in range(m):
            names[i][j] = str(c)
            c+=1
    
    answer = 0
    
    graph = dict()
        
    for i in range(n):
        for j in range(m):
            
            node_from = names[i][j]
            graph[node_from] = []
            
            if j+1 < m:
                node_to = names[i][j+1]
                graph[node_from].append((node_to, inp[i][j+1]))
            if i+1 < n:
                node_to = names[i+1][j]
                graph[node_from].append((node_to, inp[i+1][j]))
    
    answer = dijkstra(graph, names[0][0], names[-1][-1])
    
    # 7 offset
    return answer - 7
            

def solve2(inp):
    inp = np.array(inp)
    
    original_n = len(inp)
    original_m = len(inp[0])
    
    inp_new = np.array([[0 for _ in range(original_n*5)] for _ in range(original_m*5)])
    n = len(inp_new)
    m = len(inp_new[0])
    
    
    for row in range(5):
        toplefti = row * original_n   
        bottomrighti = toplefti + original_n-1
        
        inp_new[toplefti:bottomrighti+1,0:original_m] = inp + row
        
        for col in range(1,5):
            topleftj = col * original_m
            bottomrightj = topleftj + original_m-1
            
            inp_new[toplefti:bottomrighti+1,topleftj:bottomrightj+1] = ((inp + col + row - 1) % 9) + 1

    
    """
    with open("output.txt","w") as f_out:
        
        out = ""
        for i in range(n):
            for j in range(m):
                out += str(inp_new[i][j])
            out += "\n"

        f_out.write(out)
    """
    
    return solve1(inp_new)

print(solve2(matrix))
    