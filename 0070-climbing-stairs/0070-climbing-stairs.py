class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def dynamicprogramming(k):
            if k <= 2:
                return k
            if k not in memo:
                memo[k] = dynamicprogramming(k-1) + dynamicprogramming(k-2)
            return memo[k]
        return  dynamicprogramming(n)    

        