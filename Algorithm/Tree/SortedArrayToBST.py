class Node:
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None


class BST:
  def __init__(self):
    self.root = None

  def traversal(self, root):
    if root is None:
      return
    self.traversal(root.left)
    print(root.data)
    self.traversal(root.right)

  def append(self, root, data):
    if self.root is None:
      self.root = Node(data)

    if root is None:
      return Node(data)
    else:
      if root.data > data:
        root.left = self.append(root.left, data)
      else:
        root.right = self.append(root.right, data)
      return root

  def createWithSortedArray(self, arr):
    if arr == []:
      return
    pivot = int(len(arr)/2)
    self.append(self.root, arr[pivot])
    self.createWithSortedArray(arr[:pivot])
    self.createWithSortedArray(arr[pivot + 1:])


aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 17]
bst = BST()
bst.traversal(bst.root)
bst.createWithSortedArray(aList)
bst.traversal(bst.root)




