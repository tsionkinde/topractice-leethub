class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)
        res = []
        for x in s1 | s2 | s3:
            count = 0
            if x in s1:
                count += 1
            if x in s2:
                count += 1
            if x in s3:
                count += 1

            if count >= 2:
                res.append(x)

        return res      
        