class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum=0
        squareSum=0
        for i in str(n):
            digitSum+=int(i)
            squareSum+=int(i)*int(i)
        if squareSum - digitSum >= 50:
            return True
        else:
            return False      
        