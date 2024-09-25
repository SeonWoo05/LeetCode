class Solution(object):
    def runningSum(self, nums):
        A = [nums[1]] * len(nums)
        for i in range(1,len(nums)):
            A[i] = nums[i] + A[i-1]
        
        return A