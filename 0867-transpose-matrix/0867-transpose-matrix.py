class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix)
        cols=len(matrix[0])

        result=[[0]* row for _ in range(cols)]
        for r in range(row):
            for c in range(cols):
                result[c][r]=matrix[r][c]
        return result        



        
            


        
        
        