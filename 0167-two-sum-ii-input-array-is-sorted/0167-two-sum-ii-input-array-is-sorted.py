

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-based indices
            elif current_sum < target:
                left += 1  # Move left pointer to the right to increase the sum
            else:
                right -= 1  # Move right pointer to the left to decrease the sum
        
        return []  # Return an empty list if no solution is found


        
        