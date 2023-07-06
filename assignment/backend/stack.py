class Stack:
    def _init_(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Usage example
stack = Stack()

# Push elements into the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Check if the stack is empty
print("Is stack empty?", stack.isEmpty())

# Get the top element of the stack
print("Top element:", stack.peek())

# Pop elements from the stack
print("Popped element:", stack.pop())
print("Popped element:", stack.pop())

# Get the size of the stack
print("Stack size:", stack.size())

# Pop remaining element from the stack
print("Popped element:", stack.pop())

# Check if the stack is empty
print("Is stack empty?", stack.isEmpty())