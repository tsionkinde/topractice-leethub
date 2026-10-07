class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:       
        dictionary = {}
        for key, value in knowledge:
            dictionary[key] = value
        result = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                i += 1
                key = ""
                
                while s[i] != ')':
                    key += s[i]
                    i += 1

                
                result.append(dictionary.get(key, '?'))

            else:
                result.append(s[i])

            i += 1

        return "".join(result)
        
        