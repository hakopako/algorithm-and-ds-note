"""
Hackerrank.com
[Data Structures  Trees  Tree: Height of a Binary Tree]
https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree
-----------------------
[Sample Input]
tree object
-----------------------
Sample Output
3
"""

"""
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
"""
    def getHeight(self,root):
        if root == None:
            return 0
        if root.left != None or root.right != None:
            return max([self.getHeight(root.left), self.getHeight(root.right)]) + 1
        else:
            return 0