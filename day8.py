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


def complement_list_string(lst):
    return list(set(list("abcdefg")) - set(lst))

def getNumber(inp):
    
    positions = {
        -1:[],
        0:[0,1,2,4,5,6],
        1:[2,5],
        2:[0,2,3,4,6],
        3:[0,2,3,5,6],
        4:[1,2,3,5],
        5:[0,1,3,5,6],
        6:[0,1,3,4,5,6],
        7:[0,2,5],
        8:[0,1,2,3,4,5,6],
        9:[0,1,2,3,5],
    }
    
    known = {
        2:1,
        3:7,
        4:4
    }
    
    dp = [[0 for _ in range(7)] for _ in range(7)]
    
    sp = inp.split(" | ")
    pattern = sp[0].split(" ")
    objective = sp[1].split(" ")
    
    for word in pattern:
        word_len = len(word)
        if word_len  in known:
            pos = positions[known[word_len]]
            pos_comp = complement(pos)
            letters = [letter for letter in word]
            letters_comp = complement_list_string(letters)
            
            for i in pos:
                
                for letter in letters:
                    j = ord(letter) - ord('a')
                    if dp[i][j] == 0:     
                        # this means possible   
                        dp[i][j] = 1
                for letter in letters_comp:
                    j = ord(letter) - ord('a')            
                    # this means imposible
                    dp[i][j] = -1
                    
            for i in pos_comp:
                for letter in letters:
                    j = ord(letter) - ord('a')            
                    # this means imposible
                    dp[i][j] = -1
                    
    for word in pattern:
        word_len = len(word)
        if word_len not in known:
            pos = set()
            
            for k,v in positions.items():
                if len(v) == word_len:
                    for element in v:
                        pos.add(element)
            
            letters = [letter for letter in word]
            
            for i in pos:
                
                for letter in letters:
                    j = ord(letter) - ord('a')
                    dp[i][j] += 1/len(pos)
            
            
            
    def printMatrix(matrix):
        out = ""
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                out += "{0:>7}".format(str(round(matrix[i][j],2)))
            out += "\n"
        print(out)
    printMatrix(dp)
                    
            
                    
print(getNumber("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | acdeg fdbaec ged gebc"))


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