class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        count=0
        store=[]
        for i in nums:
            w=str(i)
            store.append(int(w[::-1]))
        store=store+nums    
        doubled=set(store)
        return len(doubled)    
            

        