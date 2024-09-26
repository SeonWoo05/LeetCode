class Solution(object):
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        
        while left < right:
            # left와 right 위치의 값을 교환
            s[left], s[right] = s[right], s[left]
            # 포인터 이동
            left += 1
            right -= 1