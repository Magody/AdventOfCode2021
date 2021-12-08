"""
a = [(2,3),(-1,15), (4,7)]

a.sort(key=lambda t: t[1], reverse=False)

print(a)
"""

import heapq

heap = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(heap)
print(heap)

heap.append(-100)
print(heap)
