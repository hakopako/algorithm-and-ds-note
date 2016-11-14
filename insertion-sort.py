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

"""
O(n^2)
 => two nested for loops.
 => worst case is reversed list.
 
Firstly, assume the first elem is sorted.
Then focuse on second elem so called A and compare the sorted array and A in descending order.
when the elem which is smaller than A is found, swap larger elems to the next place in the array
and put A into the rest place.
 
this is one cycle. 
repeat this action by changing target elem A to next one.
"""
