"""
Hackerrank.com
[Algorithms  Graph Theory  Breadth First Search: Shortest Reach]

-----------------------
[Sample Input]
12
4 2
1 2
1 3
1
3 1
2 3
2
-----------------------
Sample Output
6 6 -1
-1 6
"""

import sys
from enum import Enum

input = sys.stdin.read().split("\n")
q_num = int(input.pop(0))

class Status(Enum):
    unvisited = 1
    visited = 2
    
class Node:
    def __init__(self, d:int):
        self.data = d
        self.children = []
        self.distance = 0
        self.status = Status.unvisited
    def add_child(self, n):
        if n not in self.children:
            self.children.append(n)
    def get_children(self):
        return self.children

class Tree:
    def __init__(self, elem:int):
        self.htable = {}
        for e in range(1, elem + 1):
            self.htable[int(e)] = Node(int(e))
    def add_connection(self, root:int, child:int):
        if child not in self.htable[root].get_children():
            self.htable[root].add_child(self.htable[child])
    def get_root(self, root:int):
        return self.htable[root]
    def search_connection(self, root:int):
        if root not in self.htable:
            return
        q = []
        q.append(self.htable[root])
        while len(q) > 0:
            n = q.pop(0)
            for v in n.get_children():
                if v.status == Status.visited:
                    continue
                v.status = Status.visited
                v.distance = n.distance + 6
                q.append(v)
    def output(self, start:int):
        result = []
        for i in range(1, len(self.htable)+1):
            if i not in self.htable:
                result.append("-1")
            elif i == start:
                continue
            elif self.htable[i].distance == 0:
                result.append("-1")
            else:
                result.append(str(self.htable[i].distance))
        print(" ".join(result))
            
 ##--- main ---##
for a in range(0, q_num):
    b = input.pop(0).split(" ")
    tree = Tree(int(b[0]))
    while True:
        row = input.pop(0)
        n = row.strip().split(" ")
        if len(n) < 2:
            start = int(n[0])
            tree.search_connection(start)
            tree.output(start)
            break;
        else:
            tree.add_connection(int(n[0]), int(n[1]))
            tree.add_connection(int(n[1]), int(n[0]))
 