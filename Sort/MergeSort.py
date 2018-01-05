def MergeSort(aList):
  """
  divide list into 2 sub-lists.
  and do mergesort for them recursively. and combine them.
  """
  if len(aList) == 1:
    return aList

  num = int(len(aList) / 2)
  left = MergeSort(aList[:num])   # 0 <= index < num
  right = MergeSort(aList[num:])    # num <= index < len(aList)

  arr = []
  i = 0
  k = 0
  while i < len(left) or k < len(right):
    if i < len(left) and k >= len(right):
      arr.append(left[i])
      i += 1
    elif k < len(right) and i >= len(left):
      arr.append(right[k])
      k += 1
    elif left[i] > right[k]:
      arr.append(right[k])
      k += 1
    else:
      arr.append(left[i])
      i += 1

  return arr

########################################
## Execute
########################################
aList = [5,7,2,4,9,1]

print("MergeSort")
print(MergeSort(aList))