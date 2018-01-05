class Node:
  def __init__(self, data):
    self.data = data
    self.adjacents = []


class Graph:
  def __init__(self):
    self.nodes = []

  def add(self, nodeA, nodeB):
    nodeA.adjacents.append(nodeB)
    nodeB.adjacents.append(nodeA)
    if nodeA not in self.nodes:
      self.nodes.append(nodeA)
    if nodeB not in self.nodes:
      self.nodes.append(nodeB)

  def remove(self, nodeA):
    if nodeA not in self.nodes:
      return

    for n in nodeA.adjacents:
      n.adjacents.remove(nodeA)
    self.nodes.remove(nodeA)
