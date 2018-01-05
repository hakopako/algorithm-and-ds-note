def InsertionSort(aList):
  """
  pick an element one by one, inset int sorted list.
  compare from the end of sorted list.
  O(n^2)
  best: sorted
  worst: reversed
  """
  for i in range(1, len(aList)):  # 1 <= i < len(aList)
    for k in reversed(range(i)): # 0 <= k < i / i-1, i-2, .... 3, 2, 1, 0
      if aList[i] < aList[k]:
        tmp = aList[k]
        aList[k] = aList[i]
        aList[i] = tmp
        i -= 1
  return aList


########################################
## Execute
########################################
aList = [5,7,2,4,9,1]

print("InsertionSort")
print(InsertionSort(aList))
