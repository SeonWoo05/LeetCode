class Solution(object):
    def moveZeroes(self, nums):
        left = 0
        Z = nums.count(0)

        for i in range(len(nums)-Z):
            while nums[left] == 0:
                left += 1
            
            nums[i] = nums[left]
            left += 1

        for i in range(Z):
            nums[len(nums)-Z+i] = 0
        