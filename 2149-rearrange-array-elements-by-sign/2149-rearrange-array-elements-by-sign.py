class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg=[]
        pos=[]
        res=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        p1=0
        p2=0
        for j in range(len(pos)):
            res.append(pos[p1])
            res.append(neg[p2])
            p1+=1
            p2+=1
        return res    




        