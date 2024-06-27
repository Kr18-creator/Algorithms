"""34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def searchLeft(nums, target):
            left =0
            right= len(nums)-1

            while left<=right:
                mid= (left+right)//2

                if target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            return left
        
        def searchRight(nums, target):
            left =0
            right= len(nums)-1

            while left<=right:
                mid= (left+right)//2

                if target>=nums[mid]:
                   
                    left=mid+1
                else:
                     right=mid-1
            return right
        
        
        left_index=searchLeft(nums, target)
        right_index= searchRight(nums,target)
        
        if left_index<=right_index and 0<=left_index and right_index<=len(nums) and nums[left_index]==target and nums[right_index]==target:
            return [left_index, right_index]
        else:
            return [-1,-1]
        