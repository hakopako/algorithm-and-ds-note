"""
Hackerrank.com
[Data Structures  Linked Lists  Delete a Node]

"""

"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if position == 0:
        return head.next
    n = head
    i = 0
    while i != position -1:
        n = n.next
        i += 1
    tmp = n.next.next
    n.next = tmp
    return head
  