import sys

class ItemWithMin:
  def __init__(self, item, m):
    self.item = item
    self.min = m

class StackWithMin:
  def __init__(self):
    self.__stack = []
    self.min = sys.maxsize

  def push(self, item):
    if item < self.min:
      self.min = item
    self.__stack.append(ItemWithMin(item, self.min))

  def pop(self):
    item = self.__stack.pop()
    if self.is_empty():
      self.min = sys.maxsize
    elif item.item == self.min:
      self.min = self.get_min()
    return item.item

  def is_empty(self):
    return self.__stack == []

  def get_min(self):
    item = self.__stack[-1]
    return item.min


########################################
## Execute
########################################
stack = StackWithMin()

for i in [4,3,6,1,8,9,0,5]:
  stack.push(i)
  print(i, stack.get_min(), sep=" / ", end="\n")

stack.pop()
stack.pop()
stack.push(10)
print(stack.get_min())
