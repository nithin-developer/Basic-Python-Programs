import matplotlib.pyplot as plt

def bubblesort(array):

    n = len(array)
    for i in range(n-1):
        for j in range(n-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

array = [10,90,20,40,60,11,3,21,98,22,42]
print("Before Sorting : ",array)
bubblesort(array)
print("After Sorting : ",array)

x = list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("Bubble Sort - Time Complexity")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()
