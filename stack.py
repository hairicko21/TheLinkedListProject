class Stack:
    def __init__(self):
        self.internalArray = []

    def push(self, item):
        # Code to add an item to the stack will go here
        self.internalArray.append(item)

    def pop(self):
        # Code to remove an item from the top of the stack will go here 
        if len(self.internalArray)==0 :
          print('Stack is Empty - cannot pop')
        else: 
         a = self.internalArray[-1]

        del self.internalArray[-1]

        return a

    def __str__(self):
        return self.internalArray.__str__()

stack1 = Stack()

stack1.push(1)
a = stack1.pop()
stack1.push(4)
b = stack1.pop()
stack1.push(9)
c = stack1.pop()

print(stack1)