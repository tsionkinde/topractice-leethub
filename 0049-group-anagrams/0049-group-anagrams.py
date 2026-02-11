from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        result = []  
        if not strs:
            return result
        
      
        anagram_map = defaultdict(list)
        
    
        for s in strs:
            key = ''.join(sorted(s))  
            anagram_map[key].append(s)
        
      
        for group in anagram_map.values():
            result.append(group)
        
        return result

        