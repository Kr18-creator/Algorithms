""" Tell me if a particular element is present in a 2D matrix or not. 
https://leetcode.com/problems/search-a-2d-matrix/
"""

def searchMatrix(matrix, key):
    m= len(matrix)
    n= len(matrix[0])
    left=0
    right= m*n-1
    while left<=right:
        mid= (left+right)//2
        mid_val= matrix[mid//n][mid%n]
        if key==mid_val:
            return (mid//n, mid%n)
        if key<mid_val:
            right=mid-1
        else:
            left=mid+1

matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
key = 16

print(searchMatrix(matrix, key))





