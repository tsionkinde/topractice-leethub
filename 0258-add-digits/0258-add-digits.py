class Solution:
    def addDigits(self, num: int) -> int:
        my_list=list(map(int, str(num)))        
        while len(my_list)>1:
            total=sum(my_list)
            my_list=list(map(int,str(total)))
        return my_list[0]    
               

    
        