from math import prod
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
        a=n//2
        total=sum(skill)
        target=total//a
        skill.sort()
        l=0
        r=n-1
        res=[]

        while l<r:
            if skill[l]+skill[r]>target:
                r-=1
            elif  skill[l]+skill[r]<target:
                l+=1  
            else:
                res.append([skill[l],skill[r]])
                l +=1 
                r-=1

        if len(res) != a:
            return -1 
        ans=0        
        for i in res:
            ans+=i[0]*i[1]
        return ans    










        