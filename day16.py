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
day = 16
path = f"/home/magody/programming/AdventOfCode2021/files/{folder}/input{day}.txt"

f = open(path, "r")
message = f.read()
f.close()


def solve1(message):
    global answer
    answer = 0
    
    def parse(decoded_bin):
        
        global answer

        V = int(decoded_bin[0:3], 2)
        answer += V
        
        T = int(decoded_bin[3:6], 2)

        if T == 4:
            t = ""
            packs_rest = decoded_bin[6:]
            while True:
                t += packs_rest[1:5]
                bit = packs_rest[0]
                packs_rest=packs_rest[5:]
                if bit == '0':
                    break
        else:
            I = int(decoded_bin[6:7], 2)

            L = None
            if I == 0:
                L = int(decoded_bin[7:22],2) # represents the total length in bits of the sub-packets contained by this packet.
                
                packs_rest = decoded_bin[22:]
                other_packs = packs_rest[:L]
                while other_packs:
                    other_packs = parse(other_packs)
                packs_rest=packs_rest[L:]
                
            else:
                L = int(decoded_bin[7:18],2) # represents the number of sub-packets immediately contained by this packet.
                packs_rest=decoded_bin[18:]
                for i in range(L):
                    packs_rest=parse(packs_rest)
        return packs_rest


    bins = bin(int(message, 16))[2:]
    bins_len = len(bins)
    bins = bins.zfill(math.ceil(bins_len/4)*4)
    print(parse(bins))
    
    return answer

def solve2(message):
    
    
    def parse(decoded_bin):
        
        V = int(decoded_bin[0:3], 2)       
            
        T = int(decoded_bin[3:6], 2)

        mapreduce = []
        if T == 4:
            t = ""
            packs_rest = decoded_bin[6:]
            while True:
                t += packs_rest[1:5]
                bit = packs_rest[0]
                packs_rest=packs_rest[5:]
                if bit == '0':
                    break
                
            return (packs_rest, int(t,2))
        else:
            I = int(decoded_bin[6:7], 2)

            L = None
            if I == 0:
                L = int(decoded_bin[7:22],2) # represents the total length in bits of the sub-packets contained by this packet.
                
                packs_rest = decoded_bin[22:]
                other_packs = packs_rest[:L]
                while other_packs != "":
                    other_packs,res = parse(other_packs)
                    mapreduce.append(res)
                packs_rest=packs_rest[L:]
                
                
    
                
            else:
                L = int(decoded_bin[7:18],2) # represents the number of sub-packets immediately contained by this packet.
                packs_rest=decoded_bin[18:]
                
                for i in range(L):
                    packs_rest,res=parse(packs_rest)
                    mapreduce.append(res)
                    
                    
            """
            
    Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
    Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
    Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
    Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
    Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
    Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
    Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.

            """
            if T == 0:
                return (packs_rest, sum(mapreduce))
            elif T == 1:
                p = 1
                for res in mapreduce:
                    p*=res
                return (packs_rest,p)
            elif T == 2:
                return (packs_rest, min(mapreduce))
            elif T == 3:
                return (packs_rest, max(mapreduce))
            elif T == 5:
                return (packs_rest, 1 if mapreduce[0]>mapreduce[1] else 0)
            elif T == 6:
                return (packs_rest, 1 if mapreduce[0]<mapreduce[1] else 0)
            elif T == 7:
                return (packs_rest, 1 if mapreduce[0]==mapreduce[1] else 0)
            print("ERROR")
            return (packs_rest, -1)       


    bins = bin(int(message, 16))[2:]
    bins_len = len(bins)
    bins = bins.zfill(math.ceil(bins_len/4)*4)
    return parse(bins)

print(solve2(message))