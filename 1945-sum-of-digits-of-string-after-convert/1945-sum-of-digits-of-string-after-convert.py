class Solution(object):
    def getLucky(self, s, k):
        numbers = [str(ord(char) - ord('a') + 1) for char in s]
        numsum = "".join(numbers)
        
        for i in range(k):  
            total_sum = 0  
            for digit in numsum:
                total_sum += int(digit)

            numsum = str(total_sum)

        return int(numsum)
        