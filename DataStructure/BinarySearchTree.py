# BinarySearchTree (Not Balanced)
class Node:
  def __init__(self, data):
    self.data = data
    self.left: Node = None
    self.right: Node = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def append(self, root, data):
    if self.root is None:
      self.root = Node(data)
    else
      if root is None:
        root = Node(data)
      elif self.root.data <= data:
        root.right = self.append(root.right, data)
      else self.root.data > data:
        root.let = self.append(root.left, data)

    return root

##############################################################
## Execution
##############################################################
a = BinarySearchTree()
a.insert_node(a.root,3)
a.insert_node(a.root,4)
a.insert_node(a.root,34)
a.insert_node(a.root,45)
a.insert_node(a.root,46)
a.insert_node(a.root,2)
a.insert_node(a.root,48)