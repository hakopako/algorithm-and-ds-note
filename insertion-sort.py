"""
Hackerrank.com
[Algorithms  Sorting  Insertion Sort - Part 1]
-----------------------
[Sample Input]

5
2 4 6 8 3
-----------------------
[Sample Output]

2 4 6 8 8 
2 4 6 6 8 
2 4 4 6 8 
2 3 4 6 8 
"""
import sys

n = int(sys.stdin.readline())
arr = sys.stdin.readline().split(" ")

for i in range(1,n):
    for j in range(0,i):
        if int(arr[j]) > int(arr[i]):
            tmp = arr[i]
            for k in range(0,i-j):
                arr[i-k] = arr[i-k-1]
                print(" ".join(arr))
            arr[j] = tmp
print(" ".join(arr))
