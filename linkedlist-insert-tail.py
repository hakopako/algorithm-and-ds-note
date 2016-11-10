"""
Hackerrank.com
[Data Structures  Linked Lists  Insert a Node at the Tail of a Linked List]

"""

"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""
def Insert(head, data):
    if head == None:
        return Node(data=data, next_node=None)
    n = head
    while n.next != None:
        n = n.next
    n.next = Node(data=data, next_node=None)
    return head
