class Stack:
  def __init__(self):
    self.__stack = []

  def push(self, data):
    self.__stack.append(data)

  def pop(self):
    return self.__stack.pop()

  def peek(self):
    return self.__stack[-1]

  def is_empty(self):
    return len(self.__stack) == 0

  def print_stack(self):
    print(self.__stack)


class SortStack:
  def __init__(self):
    self.tmp_stack = Stack()

  def execute(self, stack):
    while not stack.is_empty():
      item = stack.pop()
      while not self.tmp_stack.is_empty() and int(self.tmp_stack.peek()) < int(item):
        stack.push(self.tmp_stack.pop())
      self.tmp_stack.push(item)

    while not self.tmp_stack.is_empty():
      stack.push(self.tmp_stack.pop())
    return stack


########################################
## Execute
########################################
sort_stack = SortStack()
stack = Stack()

for i in [4,3,6,1,8,9,5]:
  stack.push(i)

stack.print_stack()
sort_stack.execute(stack).print_stack()

