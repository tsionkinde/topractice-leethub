class NumArray:

    def __init__(self, nums: List[int]):
        self.presum=[0]
        current=0
        for num in nums:
            current+=num
            self.presum.append(current)

        

    def sumRange(self, left: int, right: int) -> int:
        rightsum=self.presum[right+1]
       
       
        leftsum=self.presum[left]
        return rightsum - leftsum    
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)