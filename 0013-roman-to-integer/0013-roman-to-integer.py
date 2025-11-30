class Solution:
    def romanToInt(self, s: str) -> int:
        # Step 1: Roman symbols and their values
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0  # final answer
        i = 0      # pointer to scan the string

        #  Loop through the string
        while i < len(s):

            # Check if this is a "subtraction case"
            # Example: IV (4), IX (9), XL (40), etc.
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                # subtract the smaller from the bigger
                total += values[s[i + 1]] - values[s[i]]
                i += 2  # move pointer by 2 (we used two characters)
            else:
                # normal case: just add the value
                total += values[s[i]]
                i += 1  # move pointer by 1

        return total


