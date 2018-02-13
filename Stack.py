class Stack:

    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return self.items == []

    def print(self):
        return self.items[:]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.pop()
print(a.isEmpty())
print(a.peek())
print(a.print())
print(a.size())
