# Singly linked list
class SingleList:
  def __init__(self, data):
    self.data = data
    self.next: SingleList = None

# Double linked list
class DoubleList:
  def __init__(self, pre, data):
    self.data = data
    self.pre: DoubleList = pre
    self.next: DoubleList = None


