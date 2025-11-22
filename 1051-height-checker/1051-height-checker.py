class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        sorted_height=sorted(heights)
        for i in range(len(heights)):
            if sorted_height[i]!=heights[i]:
                count+=1
        return count
        