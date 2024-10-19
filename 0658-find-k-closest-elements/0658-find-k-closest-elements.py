class Solution:
    def findClosestElements(self, arr, k, x):
        left = 0
        right = len(arr)-1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        
        while (right-left-1 < k):
            if left == -1:
                right += 1
            elif right == len(arr):
                left -= 1
            elif (abs(arr[left]-x) <= abs(arr[right]-x)):
                left -= 1
            else:
                right += 1

        return arr[left+1:right]    