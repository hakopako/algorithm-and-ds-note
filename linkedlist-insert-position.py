"""
Hackerrank.com
[Data Structures  Linked Lists  Insert a node at a specific position in a linked list]

"""

"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def InsertNth(head, data, position):
    if head == None:
        return Node(data=data, next_node=None)
    if position == 0:
        return Node(data=data, next_node=head)
    n = head
    i = 0
    while i != position - 1:
        n = n.next
        i += 1
    tmp = n.next
    n.next = Node(data=data, next_node=tmp)
    return head

"""

"""
    