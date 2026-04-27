class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts=set()
        for x,y in paths:
            starts.add(x)
        for x,y in paths:
            if y not in starts:
                return y



       
        