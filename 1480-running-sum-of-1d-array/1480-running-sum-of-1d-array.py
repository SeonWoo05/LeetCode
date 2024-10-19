class Solution(object):
    def runningSum(self, nums):
        A = [nums[0]]
        for i in range(1,len(nums)):
            A.append(nums[i] + A[i-1])
        
        return A