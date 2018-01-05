def SelectionSort(aList):
  """
  Iterate through and find minimum data. and swap that with right position
  """
  p = 0
  for p in range(len(aList)):
    m = p
    for i in range(p, len(aList)):
      if aList[i] < aList[m]:
        m = i
    tmp = aList[p]
    aList[p] = aList[m]
    aList[m] = tmp
  return aList


########################################
## Execute
########################################
aList = [5,7,2,4,9,1]

print("SelectionSort")
print(SelectionSort(aList))