from helpers.utils import *

import numpy as np
import re
import math

from copy import deepcopy

from itertools import cycle, permutations
from collections import defaultdict, Counter, deque


folder = "standard"  # "practice_2020" "standard"
day = 13
path = f"/home/magody/programming/AdventOfCode2021/files/{folder}/input{day}.txt"

n = 1300
m = 1300
matrix = [[0 for _ in range(m)] for _ in range(n)]
folds = []
matrix_xy = [] # more easy with this

with open(path, "r") as f:
    txt = f.read() # all
    points, folds_raw = txt.split("\n\n")
    
    
    for line in points.split("\n"):
        x,y = map(int, line.split(","))
        # matrix[y][x] = 1
        matrix_xy.append([x,y])
        
    for line in folds_raw.split("\n"):
        _, edge = re.split("along ", line)
        axis,value = edge.split("=")
        folds.append((axis,int(value)))
        

# print(matrix_xy)
def invert(value, cut_point, axis):
    
    if axis == 0:
        return cut_point - (value - cut_point) 
    else:
        return cut_point - (value - cut_point) 

def build_matrix(points, n, m):
    matrix = np.zeros([n, m])
    
    for point in points:
        x,y = point[0], point[1]
        matrix[y][x] = 1
            
    return matrix
    
    


for ins,fold in enumerate(folds):
    axis = 1
    if fold[0] == "x":
        axis = 0
    
    cut_point = fold[1]
    
    for k in range(len(matrix_xy)):
        
        
        if matrix_xy[k][axis] > cut_point:
            matrix_xy[k][axis] = invert(matrix_xy[k][axis], cut_point, axis)
            
    if ins == 0:
        temp = build_matrix(matrix_xy, n, m)
        print(np.sum(temp))
    elif ins == len(folds)-1:
        with open("output13.txt", "w") as f_out:
            mat = build_matrix(matrix_xy, n, m)
            out = ""
            for mat_i in range(len(mat)):
                for mat_j in range(len(mat[0])):
                    out += "#" if int(mat[mat_i][mat_j]) == 1 else "."
                out += "\n"
                
            f_out.write(out)