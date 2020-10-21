class Queue:
  def __init__(self, capacity=5):
    self.internalArray = [None] * capacity
    self.front = 0
    self.back = 0
    self.n_items = 0
    


  def add (self, item):
    if self.n_items == len(self.internalArray):
      return False # return False to indicate error ! 
    self.n_items += 1
    self.internalArray[self.back] = item
    self.back += 1
    if self.back > len(self.internalArray):
      self.back = 0 # implementing the circular aspect of the queue
    return True #indicate success
    #returning indicating messeges is better than printing an error messege, making your code more reusable 



  def remove (self):
    if self.n_items == 0:
      return None
    self.n_items -= 1
    curfrontitem = self.internalArray[self.front]
    self.front += 1 # now the front of the queue is the next item back
    return self.internalArray[self.front] #return front item
    if self.front > len(self.internalArray):
      self.front = 0 #implementing circular aspect of the queue
    return curfrontitem# return the front item

q = Queue(6)
q.add('cat')
q.add('dog')
q.add('rat')
print(q.remove())
print(q.remove())
print(q.remove())
if q.remove is None:
  print('Cannot remove queue as its empty')