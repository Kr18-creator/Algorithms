"""" Bubble Sort Algorithm
Bubble sort is a straightforward sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order. This process continues until no more swaps are needed, indicating that the list is sorted.

Logic
Compare Adjacent Elements: Compare each pair of adjacent elements in the list.
Swap if Necessary: If a pair is in the wrong order (i.e., the first element is greater than the second), swap them.
Repeat: Repeat the process for the entire list until no swaps are needed in a complete pass."""

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Track if any elements were swapped in this pass
        swapped = False
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, the array is already sorted
        if not swapped:
            break
    return arr

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array is:", sorted_arr)


"""Time and Space Complexity
Time Complexity:
Best Case: 

O(n) when the list is already sorted (due to the swapped flag).
Average and Worst Case: 

O(n2) due to the nested loops.
Space Complexity: 

O(1), as bubble sort is an in-place sorting algorithm and uses only a constant amount of extra space.
Summary
Bubble sort is a simple sorting algorithm suitable for small lists or nearly sorted lists. Its primary advantage is its simplicity, but it is generally not efficient for large lists compared to more advanced algorithms like quicksort or mergesort.

Advantages of Bubble Sort:
Bubble sort is easy to understand and implement.
It does not require any additional memory space.
It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in the sorted output.
It is suitable for small data sets or nearly sorted data sets.

Disadvantages of Bubble Sort:
Bubble sort has a time complexity of O(N2) which makes it very slow for large data sets.
Bubble sort is a comparison-based sorting algorithm, which means that it requires a comparison operator to determine the relative order of elements in the input data set. It can limit the efficiency of the algorithm in certain cases.
Bubble sort is not suitable for large data sets or data sets with a large number of elements.

Does sorting happen in place in Bubble sort?
Yes, Bubble sort performs the swapping of adjacent pairs without the use of any major data structure. Hence Bubble sort algorithm is an in-place algorithm.

Is the Bubble sort algorithm stable?
Yes, the bubble sort algorithm is stable.

Where is the Bubble sort algorithm used?
Due to its simplicity, bubble sort is often used to introduce the concept of a sorting algorithm. In computer graphics, it is popular for its capability to detect a tiny error (like a swap of just two elements) in almost-sorted arrays and fix it with just linear complexity (2n). 

Example: It is used in a polygon filling algorithm, where bounding lines are sorted by their x coordinate at a specific scan line (a line parallel to the x-axis), and with incrementing y their order changes (two elements are swapped) only at intersections of two lines.

"""