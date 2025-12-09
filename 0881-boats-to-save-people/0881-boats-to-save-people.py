class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)# the boat can carry at most two peoples regardless of the limit 
        left=0
        right=len(people)-1
        boats=0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                left += 1
            boats += 1
        return boats
        
          


                




                

        