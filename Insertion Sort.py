import matplotlib.pyplot as plt

def insertionsort(array):

    for i in range(1,len(array)):
        search_index = i
        insert_value = array[i]

        while search_index > 0 and array[search_index - 1] > insert_value:

            array[search_index] = array[search_index - 1]
            search_index -= 1

        array[search_index] = insert_value


array = [10,30,80,2,33,90,74,12,32,55,29]
print("Before Sorting : ",array)
insertionsort(array)
print("After Sorting : ",array)

x = list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("Insertion Sort - Time Complexity")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()
            
