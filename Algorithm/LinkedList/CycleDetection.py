class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


def cycleDetection(head):
  n1 = head
  checker = n1

  while True:
    head = head.next.next
    n1 = n1.next
    if head == n1:
      break

  while True:
    checker = checker.next
    n1 = n1.next
    if checker == n1:
      return n1


########################################
## Execute
########################################
head = None
for v in [3,4,1,3,5,7,1,2,6]:
  tmp = Node(v)
  if v == 7 :
    con = tmp
  if head is None:
    head = tmp
    node = head
  else:
    node.next = tmp
    node = node.next
else:
  node.next = con


print(cycleDetection(head).data)

