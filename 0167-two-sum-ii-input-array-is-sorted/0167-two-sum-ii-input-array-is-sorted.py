class Solution(object):
    def twoSum(self, numbers, target):
        ht = {}

        for idx,val in enumerate(numbers):
            match_num = target - val
            match_idx = ht.get(match_num)

            if match_idx is not None:
                return [match_idx + 1, idx + 1]
            
            ht[val] = idx