class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        current_width = 0
        for ch in s:
            idx=ord(ch)-ord('a')
            char_width = widths[idx]
            if current_width + char_width > 100:
                lines += 1
                current_width = char_width
            else:    
                current_width += char_width    
        return [lines,current_width]        
        