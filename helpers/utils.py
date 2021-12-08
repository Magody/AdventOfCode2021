import re

def readAll(path):
    output = ""
    with open(path, 'r') as file:
        output = file.read()
    
    return output

def readArray(path, mapping="none"):
    array = []
    with open(path, 'r') as file:
        array = file.readlines()
        if mapping == "int":
            array = list(map(int,array))
        elif mapping == "float":
            array = list(map(float,array))
        else:
            array = list(map(lambda s: s.replace("\n", ""),array))
    
    return array

def readMatrix(path, mapping=int):
    matrix = []
    with open(path, 'r') as file:
        
        lines = list(map(lambda s: s.replace("\n", ""), file.readlines()))
        
        for line in lines:
            line = line.strip()
            if line == "":
                break
            s = re.split('\s+', line)
            matrix.append(list(map(mapping,s)))
        
    
    return matrix

def readMatrices(path, mapping=int):
    matrices = []
    with open(path, 'r') as file:
        
        lines = list(map(lambda s: s.replace("\n", ""), file.readlines()))
        
        matrix = []
        for line in lines:
            line = line.strip()
            if line == "":
                if len(matrix) > 0:
                    matrices.append(matrix)
                    matrix = []
                continue
            s = re.split('\s+', line)
            matrix.append(list(map(mapping,s)))
        if len(matrix) > 0:
            matrices.append(matrix)
    
    return matrices

def readArrayIgnoreBlankLines(path):
    array = []
    with open(path, 'r') as f:
        lines = list(map(lambda s: s.replace("\n", ""), f.readlines()))
        
        array = []
        val = ""
        for line in lines:
            line = line.strip()
            
            if line == "":
                array.append(val)
                val = ""
            else:
                if val == "":
                    val = line
                else:
                    val += " " + line
        if len(val) > 0:
            array.append(val)
            
    return array

def readArrayOneLine(path, mapping="none"):
    array = []
    with open(path, 'r') as f:
        array = list(map(lambda s: s.replace("\n", ""), f.readline().split(",")))
            
        if mapping != "none":
            array = list(map(mapping, array))
    return array
    