"""
Hackerrank.com
[Algorithms  Search  Missing Numbers]

-----------------------
[Sample Input]
10
203 204 205 206 207 208 203 204 205 206
13
203 204 204 205 206 207 205 208 203 206 205 206 204
-----------------------
Sample Output
204 205 206
"""

import sys

numA = int(sys.stdin.readline())
arrA = [int(x) for x in sys.stdin.readline().split(" ")]
numB = int(sys.stdin.readline())
arrB = [int(x) for x in sys.stdin.readline().split(" ")]

hashtable = {}   # key is the number, value is count of the number
for i in range(0,numB):
    if arrB[i] not in hashtable:
        hashtable[arrB[i]] = 0
    hashtable[arrB[i]] += 1
    
for i in range(0,numA):
    hashtable[arrA[i]] -= 1
    if hashtable[arrA[i]] == 0:
        del(hashtable[arrA[i]])
        
# insertion sort
arr = list(hashtable.keys())
for i in range(1,len(arr)):
    tmp = arr[i]
    while i > 0 and arr[i-1] > tmp:
        arr[i]=arr[i-1]
        i -= 1
    arr[i]=tmp

print(" ".join([str(x) for x in arr]))