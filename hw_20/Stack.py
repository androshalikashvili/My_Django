class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

#=================================
            
stack_1 = Stack()

stack_1.push(2)
stack_1.push(5)
stack_1.push(15)
stack_1.push(27)
arr = stack_1.pop()

print(arr)
print(stack_1.stack)
