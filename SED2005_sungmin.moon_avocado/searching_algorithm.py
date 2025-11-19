
def LinearSearch(arr, x):
    n = len(arr)
    
    # Iterate over the array in order to
    # find the key x
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1

def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1