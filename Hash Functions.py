class Hash:

    def __init__(self):
        self.buckets = [[],[],[],[],[]]

    def insert(self,value):
        buc_index = key%5
        self.buckets[buc_index].append(key)
        print(key, "Inserted in Bucket Number : ",buc_index + 1)
        
    def search(self,key):
        buc_index = key%5
        if key in self.buckets[buc_index]:
            print(key," is Present in Bucket Number : ",buc_index + 1)
        else:
            print(key," is Not Present in the Bucket")

    def display(self):
        for i in range(0,5):
            print("\n Buckets Number : ",i+1,end = " ")
        for j in self.buckets[i]:
            print(j,end = " = ")

h = Hash()
while True:
    print("Hash Operation\n 1:Insert 2:Search 3:Display 4:Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        key = int(input("Enter Key to Insert : "))
        h.insert(key)

    elif choice == 2:
        key = int(input("Enter key to Search : "))
        h.search(key)

    elif choice == 3:
        h.display()

print("Hash Operation\n 1:Insert 2:Search 3:Display 4:Exit")
choice = int(input("Enter Your Choice : "))
