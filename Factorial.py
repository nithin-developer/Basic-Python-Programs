def factorial(n):
    if n == 0:
        return 1
    return (n*factorial(n-1))

num = int(input("Enter a Number to Find Factorial Value : "))
print("Factorial Value is : ",factorial(num))
