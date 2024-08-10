# Stack data structure with push, pop and peek functions.

class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def pop(self):
        if self.stack.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def push(self, element):
        self.stack.append(element)

    def peek(self):
        if self.stack.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
homeworkStack = Stack()
