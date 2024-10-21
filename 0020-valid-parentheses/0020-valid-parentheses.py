from collections import deque

class Solution(object):
    def isValid(self, s):
        dq = deque()
        mapping = {')':'(', ']':'[', '}':'{'}
        
        for i in s:
            if i in ['(','[',"{"]:
                dq.append(i)
            else:
                if not dq or dq.pop() != mapping[i]:
                    return False

        return len(dq) == 0