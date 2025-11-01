class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_array=[]
        left=0
        right=n

        for i in range(len(nums)):
            while right<len(nums) and left<len(nums)//2:
                shuffled_array.append(nums[left])
                shuffled_array.append(nums[right])
                left+=1
                right+=1
        return  shuffled_array        

         


        