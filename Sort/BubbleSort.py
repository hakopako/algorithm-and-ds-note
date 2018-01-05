def BubbleSort(aList):
  """
  compare 2 elements leanerly and switch them. 
  O(n^2)
  best: sorted 
  worst: reversed
  """
  for i in reversed(range(len(aList))): # 0 <= i < len(aList)
    for k in range(i): # 0 <= k < i
      if aList[k] > aList[k+1]:
        tmp = aList[k+1]
        aList[k+1] = aList[k]
        aList[k] = tmp
  return aList

########################################
## Execute
########################################
aList = [5,7,2,4,9,1]

print("BubbleSort")
print(BubbleSort(aList))