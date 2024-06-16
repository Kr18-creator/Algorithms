""" Summary
Time Complexity: 
O(n2) for best, average, and worst cases.
Space Complexity: 
O(1)
Here’s a summary of the selection sort algorithm with its time and space complexities:

Initialization: Set min_index for the current position.
Find Minimum: Iterate through the unsorted part to find the minimum element.
Swap: Swap the found minimum element with the first unsorted element.
Repeat: Repeat the process for the next element until the entire array is sorted."""



def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element
        min_index = i
        # Iterate over the unsorted elements
        for j in range(i + 1, n):
            # Find the minimum element in the remaining unsorted array
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted array
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage:
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array is:", sorted_arr)
