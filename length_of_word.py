class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        
        i= len(s) - 1
        count = 0
        

        while s[i] == " " and i >= 0:
            i -= 1

        while s[i] != " " and i >= 0:

            count += 1
            i -= 1

        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World"))
    print(sol.lengthOfLastWord("luffy is still joyboy"))
    print(sol.lengthOfLastWord("   fly me   to   the  moon   "))
    print(sol.lengthOfLastWord("     "))
    print(sol.lengthOfLastWord("Hello"))