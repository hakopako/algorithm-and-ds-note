class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


def has_intersection(headA, headB):
  while headA.next is not None:
    headA = headA.next
  while headB.next is not None:
    headB = headB.next
  return headA == headB

def intersection(headA, headB):
  pA = headA
  pB = headB
  lenA = 0
  lenB = 0
  while headA is not None:
    headA = headA.next
    lenA += 1

  while headB is not None:
    headB = headB.next
    lenB += 1

  if lenA > lenB:
    while lenA != lenB:
      pA = pA.next
      lenA -= 1
  else:
    while lenA != lenB:
      pB = pB.next
      lenB -= 1

  while True:
    if pA == pB:
      return pA
    pA = pA.next
    pB = pB.next



########################################
## Execute
########################################
headA = None
headB = None
con = None
for v in [3,4,1,3,5,7,1,2,6]:
  tmp = Node(v)
  if v == 7 :
    con = tmp
  if headA is None:
    headA = tmp
    node = headA
  else:
    node.next = tmp
    node = node.next

for v in [5,0,14,63,4]:
  tmp = Node(v)
  if headB is None:
    headB = tmp
    node = headB
  else:
    node.next = tmp
    node = node.next
else:
  node.next = con

if has_intersection(headA, headB):
  print(intersection(headA, headB).data)
