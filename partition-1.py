import sys

n = int(sys.stdin.readline())
input = [int(x) for x in sys.stdin.readline().split(" ")]

def partition(arr, p, q):
    x = arr[p]   # pivot
    i = p
    for j in range(i+1,q):
        if arr[j] < x:
            tmp = arr[j]
            arr[j] = arr[i+1]
            arr[i+1] = tmp
            i += 1
    tmp = arr[i]
    arr[i] = x
    arr[p] = tmp
    return i 
    
partition(input, 0, n)