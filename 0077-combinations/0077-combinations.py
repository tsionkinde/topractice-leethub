class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def combi(path,i):
            #basecase
            if len(path)==k:
                ans.append(path.copy())
                return 


            #choices
            for j in range(i,n+1):
                path.append(j)
                combi(path,j+1)
                path.pop()
            return 



        combi([],1)
        return ans