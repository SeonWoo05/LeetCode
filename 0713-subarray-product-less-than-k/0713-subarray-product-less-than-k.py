class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        left = 0
        prod = 1
        cnt = 0

        for right in range(len(nums)):
            prod *= nums[right]

            while prod >= k and left <= right:
                prod /= nums[left]
                left += 1
        
        cnt += right - left + 1

        return cnt    