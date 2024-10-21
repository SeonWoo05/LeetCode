from collections import deque

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        dq = deque()
        ans = [-1] * len(nums1)

        for num in nums1:
            nums2_idx = nums2.index(num)
            dq.append(nums2_idx)

        for i in range(len(nums1)):
            idx2 = dq.popleft()
            for j in nums2[idx2+1:]:
                if nums2[idx2] < j:
                    ans[i] = j
                    break
                
        return ans