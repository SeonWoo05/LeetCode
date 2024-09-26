class Solution(object):
    def selfDividingNumbers(self, left, right):
        C = []
        for i in range(left,right+1):
            D = []
            for j in str(i):
                D.append((i % int(j))
            if len(D) == 1:
                C.append(D[0])
        
        return C