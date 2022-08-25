def binarysearch(array,key):

    low = 0
    high = len(array)-1

    while low <= high:
        mid = (high+low)//2

        if key == array[mid]:
            return mid

        elif key < array[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return -1

array = [12,50,60,70,85,20,31,99,52]
print("The Array Elements are : ",array)

key = int(input("Enter Element to Search : "))
r = binarysearch(array,key)

if r == -1:
    print("Search is Unsuccessful, Element not Found")
else:
    print("Search is Successful key found at : ",r+1)
