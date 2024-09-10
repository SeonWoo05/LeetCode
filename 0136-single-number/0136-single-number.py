class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num  # XOR 연산으로 중복 숫자를 제거
        return result