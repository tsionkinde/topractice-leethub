class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores=sorted(score,reverse=True)
        rank={}
        for i,val in enumerate( sorted_scores):
            if i==0:
                rank[val]="Gold Medal"
            elif i==1:
                rank[val]="Silver Medal"
            elif i==2:
                   rank[val]= "Bronze Medal" 
            else:
                rank[val]=str(i+1)
        result=[]
        for s in score:
            result.append(rank[s])
        return result                   


      





        