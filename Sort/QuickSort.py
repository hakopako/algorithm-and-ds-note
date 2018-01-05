def QuickSort(aList):
  if not aList:
    return []

  pivot = [x for x in aList if x == aList[0]]
  lesser = QuickSort([x for x in aList if x < aList[0]])
  greater = QuickSort([x for x in aList if x > aList[0]])

  return lesser + pivot + greater
  

########################################
## Execute
########################################
aList = [5,7,2,4,9,1]

print("QuickSort")
print(QuickSort(aList))