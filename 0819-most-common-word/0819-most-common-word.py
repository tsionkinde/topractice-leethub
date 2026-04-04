from collections  import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        for char in ":,!?.';":
            paragraph=paragraph.replace(char," ")
        words=paragraph.split()
        banned=set(banned)
        count=Counter()
        for word in words:
            if word not in banned:
                count[word]+=1
        return max(count,key=count.get)        


        

            

     


        



        