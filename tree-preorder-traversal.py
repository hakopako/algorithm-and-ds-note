"""
Hackerrank.com
[Data Structures  Trees  Tree: Preorder Traversal]

-----------------------
[Sample Input]
tree object
-----------------------
Sample Output
3 5 1 4 2 6
"""

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def preOrder(root):
    print(str(root.data) + " ", end="", flush=True)
    if root.left != None:
        preOrder(root.left)
    if root.right != None:
        preOrder(root.right)