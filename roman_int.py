class Solution:
    def romanToInt(self, s: str) -> int:
        
        numDict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        total = 0

        for i in range(len(s)):
             if i + 1 < len(s) and numDict[s[i]] < numDict[s[i+1]]:
                  total -= numDict[s[i]]
             else:
                  total += numDict[s[i]]

        return total
            
if __name__ == "__main__":
        sol = Solution()
        print(sol.romanToInt("LVIII"))