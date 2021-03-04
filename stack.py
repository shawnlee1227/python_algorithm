class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def get_stack(self):
        return self.items


if __name__ == "__main__":
    myStack = Stack()
    myStack.push("CEA")
    myStack.push("PLB")
    print(myStack.get_stack())
    myStack.push("ZVM")
    print(myStack.get_stack())
    myStack.pop()
    print(myStack.get_stack())
    print(myStack.peek())