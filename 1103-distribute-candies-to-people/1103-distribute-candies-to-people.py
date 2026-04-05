class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans=[0]*num_people
        i=0
        while candies>0:
            give=i+1
            person=i%num_people
            ans[person]+=min(give,candies)
            candies-=give
            i+=1
        return ans    
           

        