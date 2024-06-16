"""Insertion sort is a simple and intuitive sorting algorithm that builds the final sorted array one item at a time. It is much like sorting playing cards in your hands; we start with an empty left hand and the cards face down on the table. We then pick the cards one at a time and insert them into the correct position in the left hand.

Logic
Start from the second element: Assume the first element is already sorted.
Pick the next element: Store it in a temporary variable.
Shift the sorted elements: Compare the picked element with the sorted elements and shift the sorted elements one position to the right to make space for the picked element.
Insert the picked element: Place it in the correct position.
Repeat: Repeat until all elements are sorted."""

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array is:", sorted_arr)

"""Time Complexity of Insertion Sort
Best case: O(n), If the list is already sorted, where n is the number of elements in the list.
Average case: O(n2), If the list is randomly ordered
Worst case: O(n2), If the list is in reverse order

Space Complexity of Insertion Sort
Auxiliary Space: O(1), Insertion sort requires O(1) additional space, making it a space-efficient sorting algorithm.
Advantages of Insertion Sort:
Simple and easy to implement.
Stable sorting algorithm.
Efficient for small lists and nearly sorted lists.
Space-efficient.

Disadvantages of Insertion Sort:
Inefficient for large lists.
Not as efficient as other sorting algorithms (e.g., merge sort, quick sort) for most cases.

"""


""""Frequently Asked Questions on Insertion Sort
Q1. What are the Boundary Cases of the Insertion Sort algorithm?

Insertion sort takes the maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted. 

Q2. What is the Algorithmic Paradigm of the Insertion Sort algorithm?

The Insertion Sort algorithm follows an incremental approach.

Q3. Is Insertion Sort an in-place sorting algorithm?

Yes, insertion sort is an in-place sorting algorithm.

Q4. Is Insertion Sort a stable algorithm?

Yes, insertion sort is a stable sorting algorithm.

Q5. When is the Insertion Sort algorithm used?

Insertion sort is used when number of elements is small. It can also be useful when the input array is almost sorted, and only a few elements are misplaced in a complete big array."""