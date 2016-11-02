"""
Hackerrank.com
[Algorithms  Sorting  Quicksort 2 - Sorting]
-----------------------
[Sample Input]
7
5 8 1 3 7 9 2
-----------------------
Sample Output
2 3
1 2 3
7 8 9
1 2 3 5 7 8 9
"""

import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split(" ")]

def partition(arr):
    if len(arr) <= 1:
        return arr
    n = len(arr)
    pivot = arr[0]
    left = list()
    right = list()
    for i in range(1,n):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    left_a = partition(left)
    right_a= partition(right)
    result = [str(x) for x in left_a + [pivot] + right_a]
    print(" ".join(result))
    return result

partition(arr)
