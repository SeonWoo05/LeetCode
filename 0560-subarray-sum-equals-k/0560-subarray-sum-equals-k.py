class Solution(object):
    def subarraySum(self, nums, k):
        left = 0
        sum = 0
        cnt = 0
        for i in range(len(nums)):
            sum += nums[i]

            while sum > k:
                sum -= nums[left]
                left += 1

            if sum == k:
                cnt += 1
                sum -= nums[left]
                left += 1

        return cnt