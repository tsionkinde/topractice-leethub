class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        colori=1
        typei=0
        namei=2
        count=0
        for item in items:            
            if ruleKey=="color" and item[colori]==ruleValue:
                count+=1
            elif ruleKey=="type" and item[typei]==ruleValue:
                count+=1
            elif ruleKey=="name" and item[namei]==ruleValue:
                count+=1                      


                 
        return count         
        