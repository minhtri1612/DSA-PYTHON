class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Queue:
  def __init__(self):
    self.head=None
    self.last=None
  
  def enqueue(self,data):
    if self.last is None:
      self.head=Node(data)
      self.last=self.head
    else:
      self.last.next=Node(data)
      self.last=self.last.next

  def dequeue(self):
    if self.head is None:
      return None
    else:
      temp=self.head
      self.head=self.head.next
      temp.next=None
      return temp.data

  def print_queue(self):
    if self.head is None:
      return None
    else:
      temp=self.head
      while temp is not None:
        print(temp.data)
        temp=temp.next
      return

  def is_empty(self):
    return self.head==None

q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.print_queue()
print(q.dequeue())
print(q.dequeue())