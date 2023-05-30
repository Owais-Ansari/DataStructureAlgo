'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = '[0,1,2,4,5,6,7]' might become:

`[4,5,6,7,0,1,2]` if it was rotated 4 times.
`[0,1,2,4,5,6,7]` if it was rotated 7 times.
Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.
'''

#***solution***
'''
Input : Rotated sorter array of unique integers
OutPut : Minimun number in the list
test case 0 = {'input':[3,4,5,7,1,2],'output: 1}
test case 1 = {'input':[3,4,5,0,1,2],'output: 0}
test case 2 = {'input':[],'output: -1}
test case 3 = {'input':[1,2,3,4],'output: 1}
test case 4 = {'input':[1],'output: 1}
'''



class Solution(object):
    def findMin(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0 
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            #print(mid)
            # If previous number is greater than the current (mid) number 
            if mid > 0 and nums[mid] < nums[mid-1]:
                return nums[mid]
            elif mid > 0 and nums[mid] < nums[high]:
            # Answer lies in the left half
                high = mid-1  
            else:
             # Answer lies in the right half
                low = mid + 1
        if high>=0:
          # if list is not empty
            return nums[0]
        else:
            return -1

