from helpers.utils import *

import numpy as np
import re

from copy import deepcopy

from itertools import cycle, permutations


folder = "standard"  # "practice_2020" "standard"
day = 8
path = f"/home/magody/programming/AdventOfCode2021/files/{folder}/input{day}.txt"

inp = readArray(path, mapping=int)
# inp = readArrayIgnoreBlankLines(path)
# inp = readArrayOneLine(path,int)


 
def solve1(inp):

    answer = 0
    
    
    d = {
        1: ["c", "f"],
        4: ["b", "c", "d", "f"],
        7: ["a", "c", "f"],
        8: ["a", "b", "c", "d", "e", "f", "g"]
    }

    
    for comb in inp:
        s = comb.split(" | ")
        
        nums = [1,4,7,8]
        for num in s[1].split(" "):
            
            num_len = len(num)
            
            value = -1
            for n in nums:
                a = d[n]
                if num_len != len(a):
                    continue
                value = n
                
            if value != -1:
                answer += 1
        
    
        
    return answer

def complement(num_positions):
    return list(set([0,1,2,3,4,5,6]) - set(num_positions))

def complement_string(str):
    return list(set("abcdefg") - set(str))


def solve2(inp):
    answer = 0
    platform_correct = {
        "abcdefg": 8,
        "bcdef": 5,
        "acdfg": 2,
        "abcdf": 3,
        "abd": 7,
        "abcdef": 9,
        "bcdefg": 6,
        "abef": 4,
        "abcdeg": 0,
        "ab": 1
    }
    
    permut = list(permutations(list("abcdefg")))
    
    for case in inp:
        sp = case.split(" | ")    
        lights_saw = sp[0].split(" ")
        lights_four = sp[1].split(" ")
        
        base = "abcdefg"
            
        for permute in permut:
            graph_probably = dict()
            
            nex = False
            for i in range(len(base)):
                letter1 = base[i]
                letter2 = permute[i]
                
                graph_probably[letter1] = letter2


            for word in lights_saw:
                
                probably = ""
                for letter in word:
                    probably += graph_probably[letter]
                    
                arr = sorted(probably)
                
                probably = ""
                for a in arr:
                    probably += a
                    
                    
                if probably not in platform_correct:
                    nex = True
                    break

            if nex:
                continue
        
            # the graph is similar to the same given in the platform
            digits = ""
            
            for word in lights_four:
                probably = ""
                for letter in word:
                    probably += graph_probably[letter]
                    
                arr = sorted(probably)
                
                probably = ""
                for a in arr:
                    probably += a
                
                digits += str(platform_correct[probably])

            answer += int(digits)
 
    return answer


print(solve2(inp))