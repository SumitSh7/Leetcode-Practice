class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        y = str(x)
        b = len(y)

        for i in  range(b//2):
            if y[i] != y[b-i-1]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(371873))