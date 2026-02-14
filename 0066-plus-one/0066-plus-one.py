class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits)))  # convert list to int
        num += 1                              # add one
        return [int(d) for d in str(num)] 
        