class MyStack(object):

    def __init__(self):
        self.array = []

    def pushStack(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.array.append(x)
        

    def popStack(self):
        """
        :rtype: int
        """
        return self.array.pop()
        

    def peekStack(self):
        """
        :rtype: int
        """
        return self.array[-1]
        

    def emptyStack(self):
        """
        :rtype: bool
        """
        return not bool(len(self.array))

# print(MyStack().array)
# obj = MyStack()
# obj.push(1)
# obj.push(2)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# print(param_2,param_3,param_4)

class MyQueue(object):

    def __init__(self):
        self.stack1=MyStack()
        self.stack2=MyStack()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.stack1.emptyStack():
            self.stack1.pushStack(x)
        else:
            self.stack2.pushStack(x)

    def pop(self):
        """
        :rtype: int
        """
        poped_value = self.stack1.popStack()

        while not self.stack2.emptyStack():
            self.stack1.pushStack(self.stack2.popStack())
        if not self.stack1.emptyStack():
            firstVal = self.stack1.popStack()
            while not self.stack1.emptyStack():
                self.stack2.pushStack(self.stack1.popStack())
            self.stack1.pushStack(firstVal)
        
        return poped_value
        
        

    def peek(self):
        """
        :rtype: int
        """
        return self.stack1.peekStack()

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack1.emptyStack()

obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()
print(param_2,param_3,param_4)
