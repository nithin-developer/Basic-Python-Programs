class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insert(self, item):
        if item < root.val:
            root.left = Node(item)
        elif item > root.val:
            root.right = Node(item)
        elif item < root.val & item < root.left:
            root.left.left = Node(item)
        elif item > root.val & item > root.left:
            root.left.right = Node(item)

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.val, end=" ")
        Inorder(root.right)

def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.val, end=" ")

def Preorder(root):
    if root:
        print(root.val, end=" ")
        Preorder(root.left)
        Preorder(root.right)

n = int(input("Enter the Root Node : "))
root = Node(n)
while True:
    print("\n1:Add Element 2:Display 3:Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        num = int(input("Enter the Element : "))
        root.insert(num)
    elif choice == 2:
        print("Pre - Oreder Traversal\n")
        Preorder(root)
        print("\nPost - Oreder Traversal\n")
        Postorder(root)
        print("\nIn - Oreder Traversal\n")
        Inorder(root)
    else:
        break