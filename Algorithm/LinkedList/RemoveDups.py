class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def printList(self):
    res = []
    node = self
    while node.next is not None:
      res.append(node.data)
      node = node.next
    res.append(node.data)
    print(res)


def removeDup(head):
  h = dict()
  pre = None
  node = head
  while node is not None:
    if node.data in h:
      pre.next = node.next
      pre = node.next 
    else:
      h[node.data] = True
      pre = node    
    node = node.next
  return head


########################################
## Execute
########################################
head = None
for v in [3,4,1,3,5,7,1]:
  if head is None:
    head = Node(v)
    node = head
  else:
    node.next = Node(v)
    node = node.next


head.printList()

print("removeDup")
removeDup(head).printList()

