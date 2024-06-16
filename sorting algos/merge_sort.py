""""Merge sort is a divide-and-conquer algorithm that divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge function assumes that the two halves are sorted and merges them.

Implementation Steps:
Divide: The array is recursively divided in half until the base case of an array with a single element is reached (which is inherently sorted).

Conquer: The merge_sort function recursively sorts the two halves.

Combine: The merge function merges the two sorted halves to produce a single sorted array.

"""

def merge_sort(arr):
    if len(arr)<2:
        return arr
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2
        
        # Dividing the elements into 2 halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        # Merge the temp arrays back into arr
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Checking if any element was left in the left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Checking if any element was left in the right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
arr = [12, 11, 13, 5, 6, 7]
print("Given array is")
print(arr)
merge_sort(arr)
print("Sorted array is")
print(arr)



"""Complexity Analysis of Merge Sort:
Time Complexity:

Best Case: O(n log n), When the array is already sorted or nearly sorted.
Average Case: O(n log n), When the array is randomly ordered.
Worst Case: O(n log n), When the array is sorted in reverse order.
Space Complexity: O(n), Additional space is required for the temporary array used during merging.

Advantages of Merge Sort:
Stability: Merge sort is a stable sorting algorithm, which means it maintains the relative order of equal elements in the input array.
Guaranteed worst-case performance: Merge sort has a worst-case time complexity of O(N logN), which means it performs well even on large datasets.
Simple to implement: The divide-and-conquer approach is straightforward.
Parallelism: Merge sort can be easily parallelized, making it efficient for parallel computing.

Disadvantage of Merge Sort:
Space complexity: Merge sort requires additional memory to store the merged sub-arrays during the sorting process. 
Not in-place: Merge sort is not an in-place sorting algorithm, which means it requires additional memory to store the sorted data. This can be a disadvantage in applications where memory usage is a concern.


Applications of Merge Sort:
Sorting large datasets
External sorting (when the dataset is too large to fit in memory)
Inversion counting (counting the number of inversions in an array)
Finding the median of an array"""
