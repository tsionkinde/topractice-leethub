class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        rev=int(str(num)[::-1])
        rev_rev=int(str(rev)[::-1])
     
        if num==rev_rev:
            return True
        else:
            return False    
        