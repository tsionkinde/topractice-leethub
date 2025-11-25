class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_arr=[]
        odd_arr=[]
        the_whole=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                even_arr.append(nums[i])
            else:
                odd_arr.append(nums[i])
        the_whole= even_arr +  odd_arr
        return the_whole      



                

        