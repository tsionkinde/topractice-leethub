class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result=[]
        for i in range(len(arr)-1,0,-1):
            max_arr=max(arr[:i+1])
            index_of_max=arr.index(max_arr)
            if index_of_max==i:
                continue
            if index_of_max!=0:
                arr[:index_of_max+1]=reversed(arr[:index_of_max+1])
                result.append(index_of_max+1) 
            arr[:i+1]=reversed(arr[:i+1])
            result.append(i+1)
        return result           
        