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


def reverse(head):
  pre = None
  while head is not None:
    node = head
    head = head.next
    node.next = pre
    pre = node

  return pre


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

print("reverse")
reverse(head).printList()

