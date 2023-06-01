'''
***Search in a rotated list***

There is an integer array nums sorted in ascending order (with distinct values)..

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.'''



# Given
'''

Input : rotated sorted array of unique integers, and Target number which need to be find in the sorted array.
output : index where the target value is present 
desired complexity : Olog(N)

***Solution***
The intuition behind checking if the target number is in the left half or right half of a rotated array and then slicing the array to find its index is to take advantage of the sorted nature of the subarrays after rotation.

When an array is sorted and then rotated, it can be divided into two sorted subarrays. The pivot point, which represents the point of rotation, separates these subarrays.

By comparing the target number with the first element of the array, we can determine if the target is in the left half or right half of the rotated array.

If the target is greater than or equal to the first element, it means the target is in the left half of the rotated array. Since the left half is sorted, we can perform a standard binary search on this portion to find the index of the target.

If the target is less than the first element, it means the target is in the right half of the rotated array. Again, since the right half is sorted, we can perform a binary search on this portion to find the index of the target.


test case0 : {'input' : [14,16,18, 2,4,6,8,10,12],  'target':8,  'output' :6}
test case1 : {'input' : [16,18,20, 2,4,6,10,12,14], 'target':8,  'output' :-1}
test case2 : {'input' : [16,18,20,2,2,2,4,6,10,12],  'target':2,   'output' :3}
test case3 : {'input' : [2,4,6,10,12,14,16,18,20],  'target':20,  'output' :9}
test case4 : {'input' : [], 'query':0, 'output' :-1}

'''


class Solution:
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low +high) // 2
            if mid>=0 and nums[mid] == target:
                if mid>0 and nums[mid-1] == nums[mid]:
                    high = mid - 1
                else:
                    return mid
            # we're in the first sorted list
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
           # we're in the second sorted list
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
