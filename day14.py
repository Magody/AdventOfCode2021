from helpers.utils import *

import numpy as np
import re
import math

from copy import deepcopy

from itertools import cycle, permutations
from collections import defaultdict, Counter, deque


folder = "standard"  # "practice_2020" "standard"
day = 14
path = f"/home/magody/programming/AdventOfCode2021/files/{folder}/input{day}.txt"


polymer = "CBNBOKHVBONCPPBBCKVH"

inp = readArray(path)

m = dict()

for instruction in inp:
    ab,c = instruction.split(" -> ")
    m[ab] = c
    
def solve1():
    
    # brute force in 2 min lol, juicy 30 points

    for t in range(40):
        new_polymer = ""
        pol_len = len(polymer)
        for i in range(pol_len-1):
            pair = polymer[i] + polymer[i+1]
            new_polymer += polymer[i] + m[pair]
            
        new_polymer += polymer[-1]
        # print(new_polymer)
        polymer = new_polymer
        
        
    freq = [0 for _ in range(26)]

    # print(new_polymer)
    for letter in new_polymer:
        freq[ord(letter) - ord('A')]+=1
        
    mi = math.inf
    for value in freq:
        if value > 0:
            mi = min(mi, value)
            
    print(max(freq) - mi)
    

def solve2():
    
    # this is like the fish problem
    
    freq = dict()
    for i in range(len(polymer)-1):
        key = polymer[i:i+2]
        if key not in freq:
            freq[key] = 0
        freq[key] += 1
        
        
    for iteration in range(40):
        
        temp = dict()
        for key in freq:
            left = key[0] + m[key]
            right = m[key] + key[1]
            
            if left not in temp:
                temp[left] = 0
            if right not in temp:
                temp[right] = 0
                
            temp[left] += freq[key]
            temp[right] += freq[key]
            
        freq = temp
        
    res = [0 for _ in range(26)]
    
    for key in freq:
        letter = key[0]
        res[ord(letter) - ord('A')]+=freq[key]
    
    letter_final = polymer[-1]
    res[ord(letter_final) - ord('A')]+=1
        
    mi = math.inf
    for value in res:
        if value > 0:
            mi = min(mi, value)
    
    # print(max(res))
    return max(res) - mi
    
print(solve2())
    