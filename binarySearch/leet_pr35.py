'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

# Given
'''
Sorted array of distinct integers and target value. 
Input : sorted array, and Target number which may or may not be present 
        in the sorted array. 
output : index where the target value is present or should be present
desired complexity : Olog(N)



test case0 : {'input' : [2,4,6,8,10,12,14,16,18],  'query':8, 'output' :3}
test case1 : {'input' : [2,4,6,10,12,14,16,18,20], 'query':8,  'output' :3}
test case2 : {'input' : [2,4,6,10,12,14,16,18,20], 'query':1,  'output' :0}
test case3 : {'input' : [2,4,6,10,12,14,16,18,20], 'query':21,  'output' :9}
test case4 : {'input' : [2,4,6,10,12,14,16,18,20], 'query':-1,  'output' :0}
test case4 : {'input' : [], 'query':0, 'output' :0}


condition : 

'''



class Solution(object):
        
    def searchInsert(self,nums ,target ):
    
      low = 0
      high = len(nums)-1
      while low <= high:
        mid = (low+high)//2
        #if mid number is same as target
        if nums[mid] == target:
          return mid
        #if mid number is greater than the target then solution lies in the left
        elif nums[mid]>target:
          high = mid-1
        #if mid number is less than the target then solution lies in the right
        else:
          low = mid+1
      return low
                   
