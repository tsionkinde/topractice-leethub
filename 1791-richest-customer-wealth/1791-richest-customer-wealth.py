class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth=0
        for inner_array in accounts:
            if max_wealth < sum(inner_array):
                max_wealth=sum(inner_array)
        return max_wealth



        