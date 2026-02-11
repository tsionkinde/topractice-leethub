from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)

        chars = list(count.keys())

        
        def get_frequency(char):
            return count[char]

       
        chars.sort(key=get_frequency, reverse=True)

        result = ""
        for char in chars:
            result += char * count[char]

        return result
                



        