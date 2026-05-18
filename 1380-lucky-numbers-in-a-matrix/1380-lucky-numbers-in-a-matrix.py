class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        for i in range(len(matrix)):
            row_min=min(matrix[i])
            col_index=matrix[i].index(row_min)
            is_lucky=True
            for j in range(len(matrix)):
                if matrix[j][col_index]>row_min:
                    is_lucky=False
                    break
            if is_lucky:
                res.append(row_min)
        return res                    
       

        