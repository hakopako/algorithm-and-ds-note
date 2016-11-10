"""
Hackerrank.com
[Algorithms  Search  Ice Cream Parlor]
https://www.hackerrank.com/challenges/icecream-parlor
-----------------------
[Sample Input]
2
4
5
1 4 5 3 2
4
4
2 2 4 3
-----------------------
[Sample Output]
1 4
1 2
"""

import sys
input = sys.stdin.read().split("\n")
t = int(input.pop(0))

for a in range(0,t):
    is_found = False
    m = int(input.pop(0))
    n = int(input.pop(0))
    arr = [ int(x) for x in input.pop(0).split(" ") ]
    i = 0
    while is_found == False and i < n:
        for j in range(0, n):
            if i == j :
                continue
            if arr[i] + arr[j] == m:
                if i < j : print(str(i+1) + " " + str(j+1))
                else : print(str(j+1) + " " + str(i+1))
                is_found = True
                break
        i += 1
        