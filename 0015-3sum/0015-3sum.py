

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the input list
        nums.sort()
        threesum_zero = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Found a triplet
                    threesum_zero.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers
                    left += 1
                    right -= 1
                
                elif current_sum < 0:
                    left += 1  # We need a larger sum
                else:
                    right -= 1  # We need a smaller sum
        
        return threesum_zero