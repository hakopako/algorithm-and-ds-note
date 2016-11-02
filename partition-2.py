"""
Hackerrank.com
[Algorithms  Sorting  Quicksort 1 - Partition]
-----------------------
[Sample Input]
5
4 5 3 7 2
-----------------------
[Sample Output]
3 2 4 5 7
"""

import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split(" ")]

pivot = arr[0]
left = list()
right = list()
for i in range(1,n):
    if arr[i] < pivot:
        left.append(arr[i])
    else:
        right.append(arr[i])
        
result = [str(x) for x in left + [pivot] + right]

print(" ".join(result))
