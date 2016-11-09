"""
Hackerrank.com
[Algorithms  Dynamic Programming  Fibonacci Modified]

t[i+2] = t[i] + t[i+1]^2
-----------------------
[Sample Input]
0 1 10
-----------------------
Sample Output
84266613096281243382112
"""
import sys

input = sys.stdin.readline().split(" ")
t1 = int(input[0])
t2 = int(input[1])
num = int(input[2])

htable = {1:t1, 2:t2}

for i in range(3, num+1):
    htable[i] = htable[i-2] + htable[i-1] * htable[i-1]

print(str(htable[num]))