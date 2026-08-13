class Solution:
    def maximum69Number (self, num: int) -> int:
        the_num=[]
        for i in str(num):
            the_num.append(int(i))
        for i in range(len(the_num)):
            if the_num[i]==6:
                the_num[i]=9
                break
        final=""
        for i in the_num:
            final+=str(i) 
        return int(final)          


       


        