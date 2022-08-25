class Queue:

    def __init__(self):

        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty Cannot delete")

        else:
            item = self.items.pop(0)
            print("Deleted Element is : ",item)

    def display(self):
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            print(self.items)

    def isEmpty(self):
        return len(self.items)==0

    def length(self):
        return len(self.items)

q = Queue()
while True:

    print("1:Enqueue 2:Dequeue 3:Display 4:Length 5:Exit")
    choice = int(input("Enter your Choice : "))

    if choice == 1:
        item = int(input("Enter Element to Insert : "))
        q.enqueue(item)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.display()

    elif choice == 4:
        l = q.length()
        print("The Length of The Queue is : ",l)

    elif choice == 5:
        break

    else:
        print("Invalid Entry!")
