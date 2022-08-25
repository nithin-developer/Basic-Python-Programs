import matplotlib.pyplot as plt

def linearsearch(array,target):

    n = len(array)
    for i in range(n):
        if array[i] == target:
            return True
    return False

array = [10,50,40,60,11,30,78,30]
target = 1

if linearsearch(array,target):
    print("Target Element is Found in the Array!")

else:
    print("Target Element is not Found in the Array")

x = list(range(1,10000))
plt.plot(x,[y for y in x])
plt.title("Linear Search - Time Complexity")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()
    
