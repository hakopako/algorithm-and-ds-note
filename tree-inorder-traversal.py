"""
Hackerrank.com
[Data Structures  Trees  Tree: Inorder Traversal]

-----------------------
[Sample Input]
tree object
-----------------------
Sample Output
1 5 4 3 6 2
"""

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def inOrder(root):
    if root.left != None:
        inOrder(root.left)
    print(str(root.data) + " ", end="", flush=True)
    if root.right != None:
        inOrder(root.right)

"""
visit left node, current node and right node recursively
"""