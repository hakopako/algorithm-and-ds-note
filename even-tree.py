"""
Hackerrank.com
[Algorithms  Graph Theory  Even Tree]

-----------------------
[Sample Input]
10 9
2 1
3 1
4 3
5 2
6 1
7 2
8 6
9 8
10 8
-----------------------
Sample Output
2
"""
import sys

input = sys.stdin.read().split("\n")
num = input.pop(0).split(" ")

class Node:
    def __init__(self, d:int):
        self.data = d
        self.children = []
    def set_child(self, n):
        self.children.append(n)
    def get_children(self):
        return self.children

class Tree:
    def __init__(self, elem:int):
        self.htable = {}
        for i in range(1, elem+1):
            self.htable[i] = Node(i)
    def add_connection(self, root:int, child:int):
            self.htable[root].set_child(self.htable[child])
    def get_tree_root(self, root:int):
        return self.htable[root]

##-- create tree --##
tree = Tree(int(num[0]))
for i in input:
    node = i.split(" ")
    tree.add_connection(int(node[1]), int(node[0]))

##-- count nodes --##
result = 0
for i in range(2, int(num[0])+1):
    root = tree.get_tree_root(i)
    q = []
    q.append(root)
    count = 1
    while len(q) > 0:
        n = q.pop(0)
        count += len(n.get_children())
        for v in n.get_children():
            q.append(v)
    if count % 2 == 0:
        result += 1

print(str(result))

"""
Nodes numbers are given from input.
FirstrlyCreate every node, and then add connections so that a tree is created.

From the bottom to the top of the tree, check if the subtree has even nodes.
Count up numbers of the positive place.

In-order traversal would work.
"""