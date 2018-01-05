# Queue (FIFO)
class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, data):
    self.queue.append(data)

  def dequeue(self):
    return self.pop(0)
  
  def isEmpty(self):
    return self.queue == []
  
  def peek(self):
    retrun self.queue[0]
