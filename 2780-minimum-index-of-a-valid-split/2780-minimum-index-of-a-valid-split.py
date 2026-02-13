class Solution:
    def minimumIndex(self, nums):
        n = len(nums)
   
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
      
        total_count = nums.count(candidate)
        
      
        if total_count <= n // 2:
            return -1
        
      
        left_count = 0
        
        for i in range(n - 1):
            if nums[i] == candidate:
                left_count += 1
            
            right_count = total_count - left_count
            
            left_size = i + 1
            right_size = n - left_size
            
            if (left_count > left_size // 2 and
                right_count > right_size // 2):
                return i
        
        return -1
        