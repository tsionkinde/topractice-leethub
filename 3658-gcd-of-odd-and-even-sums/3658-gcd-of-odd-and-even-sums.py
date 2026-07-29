import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd=0
        sumEven=0
        for i in range(1,2*n+1):
            if i%2==0:
                sumEven+=i
            else:
                sumOdd+=i
        # return gcd(sumOdd,sumEven) 
        gcd=1
        for i in range(1,min(sumOdd,sumEven)+1):
            if sumOdd%i==0 and sumEven%i==0:
                gcd=i
        return gcd        




        