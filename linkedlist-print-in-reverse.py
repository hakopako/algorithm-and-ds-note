"""
Hackerrank.com
[Data Structures  Linked Lists  Print in Reverse]

-----------------------
[Sample Input]
1 --> 2 --> NULL 
2 --> 1 --> 4 --> 5 --> NULL
-----------------------
[Sample Output]
2
1
5
4
1
2
"""

"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""
def ReversePrint(head):
    stack = []
    if head == None:
        return
    while head != None:
        stack.append(head.data)
        head = head.next
    while len(stack) != 0:
        print(stack.pop())

        