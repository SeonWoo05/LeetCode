class Solution(object):
    def minSubArrayLen(self, target, nums):
        min_len = float('inf')
        left = 0
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]

            while sum >= target:
                min_len = min(min_len,i - left + 1)
                sum -= nums[left]
                left += 1
        
        return min_len if min_len != float('inf') else 0