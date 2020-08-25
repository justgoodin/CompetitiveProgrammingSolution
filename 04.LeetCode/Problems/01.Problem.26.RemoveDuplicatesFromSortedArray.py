#Link to the question below
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        
        while i<len(nums):
            if len(nums)<=1:
                break       
            elif nums[i-1]==nums[i]:
                nums.pop(i-1)
            else:
                i +=1