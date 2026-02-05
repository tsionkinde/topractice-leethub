class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index2 = {word: i for i, word in enumerate(list2)}
        
        min_sum = float('inf')
        result = []

        for i, word in enumerate(list1):
            if word in index2:
                s = i + index2[word]
                
                if s < min_sum:
                    min_sum = s
                    result = [word]
                elif s == min_sum:
                    result.append(word)

        return result


            
            