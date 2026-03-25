class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def combi(path,i):
            #basecase
            if len(path)==k:
                ans.append(path.copy())
                return 


            if i>n:
                return 
                #pick
            path.append(i)
            combi(path,i+1)
            path.pop()
            # not pick
            combi(path,i+1)    

        combi([],1)
        return ans