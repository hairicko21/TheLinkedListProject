class Node:
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None
  
    
  def link(self, otherNode):
    self.next = otherNode 
    otherNode.prev = self

  def __str__(self):
   return self.data.__str__()
   self.first = None
   self.last = None
  
  def add(self, Node):
    if (self.first is None):
      self.first = newNode

    else:
      self.last.link(newNode)
      
      self.last = newNode
  def get(self, index):
    pass
    
class Linkedlist:
  def __init__(self):



n1 = Node('apple')
n2 = Node('orange')

print(n1)
print(n2)

n1.link(n2)

print(n1.prev)
print(n1.next)
print(n2.prev)
print(n2.next)