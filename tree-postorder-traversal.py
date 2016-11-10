"""
Hackerrank.com
[Data Structures  Trees  Tree: Postorder Traversal]

-----------------------
[Sample Input]
tree object
-----------------------
Sample Output
1 4 5 6 2 3
"""

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def postOrder(root):
    if root.left != None:
        postOrder(root.left)
    if root.right != None:
        postOrder(root.right)
    print(str(root.data) + " ", end="", flush=True)