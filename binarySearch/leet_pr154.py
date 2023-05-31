'''Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.'''


#***solution***
'''
Input : Rotated sorter array of integers which can have duplicates
OutPut : Minimun number in the list
Idea :
 In a sorted rotated array, the minimum number should always be less than the numbers at both ends of the array.



When an array is sorted in non-decreasing order and then rotated, the minimum element will be located at the pivot point, which is the point where the rotation occurred. This minimum element will be smaller than both the element at the beginning of the array and the element at the end of the array.



Here's an example to illustrate this:

test case 0 = {'input':[3,4,5,7,1,2],'output: 1}
test case 1 = {'input':[3,4,5,0,0,0,1,2],'output: 0}
test case 2 = {'input':[],'output: -1}
test case 3 = {'input':[1,1,1,2,3,4],'output: 1}
test case 4 = {'input':[1],'output: 1}
test case 5 = {'input':[4,4,4,2,2,2,2,3,4],'output: 2}
test case 6 = {'input':[4,4,4,2,4],'output: 2}
'''




class Solution:
    def findMin(self, nums):
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[start]:
                end = mid
            else:
                end -= 1

        return nums[start]
