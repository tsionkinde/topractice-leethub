class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n=len(nums)
        avg=[]
        for i in range(n//2):
            minn=min(nums)
            maxx=max(nums)
            avg.append((minn+maxx)/2)
            nums.remove(minn)
            nums.remove(maxx)
        return min(avg)    


        