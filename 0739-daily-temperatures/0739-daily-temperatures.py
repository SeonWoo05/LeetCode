from collections import deque

class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        dq = deque()

        for idx, val in enumerate(temperatures):
            while dq and temperatures[dq[-1]] < val:
                prev_idx = dq.pop()
                ans[prev_idx] = idx - prev_idx
            dq.append(idx)

        return ans