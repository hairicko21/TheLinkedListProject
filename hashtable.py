class Hashtable:
  def __init__(self, capacity=127):
    self.nbuckets = capacity
    self.buckets = [None] * self.nbuckets
    #Empty array of buckets

  def put (self, key, value):
    pass

  
  #lookup a value in the Hashtable using its Key

  def get (self, key):
    pass

table = Hashtable()
table.put('cat', 'A furry animal which goes meow')
table.put('dog', 'A furry animal that goes woof')
print(table.get('cat'))