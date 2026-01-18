class Solution:
    def climbStairs(self, n: int) -> int:

        i = 0
        a = 0
        b = 1

        while i < n:
            c = a + b
            a = b
            b = c
            i += 1
            print(c)

        return c

if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(5))