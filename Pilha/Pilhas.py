class Stack:
    def __init__(self):
        self.len = 0
        self.stack = []

    def insert(self, i):
        self.stack.append(i)
        self.len += 1

    def isEmpty(self):
        if self.len == 0:
            return True
        return False

    def remove(self):
        if not self.isEmpty():
            self.stack.pop(self.len - 1)
            self.len -= 1

    def top(self):
        if not self.isEmpty():
            return print(self.stack[-1])
        return None

    def length(self):
        return self.len

    def show(self):
        if not self.isEmpty():
            return print(self.stack)
        return None


mystack = Stack()

mystack.insert(1)
mystack.insert(2)
mystack.insert(3)
mystack.insert(4)
mystack.remove()
mystack.top()
mystack.show()
