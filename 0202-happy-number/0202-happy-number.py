class Solution(object):
    def isHappy(self, n):
        A = set()
        while True:
            B = 0
            for i in str(n):
                B += int(i)**2
            
            if B == 1:
                return True
            
            elif B in A:
                return False

            else:  
                A.add(B)
                n = B
                