#Link to the question below
#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        output = []
        flag = 0
        for i in range(0,size):
            for j in range(i+1,size):
                if nums[i] + nums[j] == target:
                    output=[i,j]
        
        return output