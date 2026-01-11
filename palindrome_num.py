class Solution:
    def isPalindrome(self, x: int) -> bool:

        # if x < 0:
        #     return False
        #     
        # y = str(x)
        # b = len(y)
        #
        # for i in range(b//2):
        #     if y[i] != y[b-i-1]:
        #         return False
        # return True

        if x < 0:
            return False
        
        original = x
        reverse = 0

        while x > 0:
            last_digit = x%10
            reverse = (reverse*10)+last_digit
            x = x // 10
        return original == reverse




if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(37173))