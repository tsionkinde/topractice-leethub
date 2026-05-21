class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1=set()
        res2=set()
        for i in nums1:
            if i not in nums2:
                res1.add(i)
        for j in nums2:
            if j not in nums1:
                res2.add(j)
        return [list(res1),list(res2)]        

        