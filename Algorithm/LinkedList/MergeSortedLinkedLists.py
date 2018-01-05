class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def MergeLists(headA, headB):
  if headA is None and headB is None:
    return None
  elif headA is None and headB is not None:
    return headB
  elif headB is None and headA is not None:
    return headA

  if headA.data < headB.data:
    headA.next = MergeLists(headA.next, headB)
  else:
    tmp = headB
    headB = headB.next
    tmp.next = headA
    headA = tmp
    headA.next = MergeLists(headA.next, headB)
    
  return headA


########################################
## Execute
########################################
headA = None
headB = None
for v in [1,2,3,6,7,24]:
  tmp = Node(v)
  if headA is None:
    headA = tmp
    node = headA
  else:
    node.next = tmp
    node = node.next

for v in [0,4,5,14,63]:
  tmp = Node(v)
  if headB is None:
    headB = tmp
    node = headB
  else:
    node.next = tmp
    node = node.next


head = MergeLists(headA, headB)
while head is not None:
  print(head.data, end=" -> ")
  head = head.next
print("\n")

