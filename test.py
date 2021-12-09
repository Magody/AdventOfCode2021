"""
a = [(2,3),(-1,15), (4,7)]

a.sort(key=lambda t: t[1], reverse=False)

print(a)


import heapq

# theminimum value is in index 0
heap = [-21,-1,-45,-78,-3,-5]
# Use heapify to rearrange the elements
heapq.heapify(heap)
print(heap)

# Add element
heapq.heappush(heap,-8)

# Remove element from the heap
heapq.heappop(heap)

print(heap)

"""
from itertools import permutations, combinations

s = "abc"
print(list(combinations(s,2)))