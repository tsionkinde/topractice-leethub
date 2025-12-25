from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        pre = 0
        freq[0] = 1
        counter = 0   # fixed variable name

        for num in nums:
            pre += num
            my = pre - k
            counter += freq[my]
            freq[pre] += 1

        return counter

        