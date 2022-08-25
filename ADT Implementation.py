import time
class stack:

    def __init__(self):

        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def display(self):
        return (self.items)

s = stack()
start = time.time()
print(s.isEmpty())
print("Push Operations")
s.push(11)
s.push(20)
s.push(25)
print("Size : ",s.size())
print(s.display())
print("Peek : ",s.peek())
print("Pop Operation")
print(s.display())
print(s.pop())
print(s.pop())
print(s.display())
print("Size = ",s.size())

end = time.time()
print("Runtime of the Program is : ",end - start)
