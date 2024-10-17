class Solution(object):
    def topKFrequent(self, nums, k):
        ht = {}

        for i in nums:
            if i in ht:
                ht[i] += 1
            else:
                ht[i] = 1

        sorted_items = sorted(ht.items(), key = lambda x: x[1], reverse = True)

        result = [item[0] for item in sorted_items[:k]]

        return result