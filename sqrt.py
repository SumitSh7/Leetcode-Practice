class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            num = mid * mid
            if num > x:
                right = mid - 1
            elif num < x:
                left = mid + 1
            else:
                return mid
        
        # After the loop, 'right' is the largest integer whose square is <= x
        return right
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(124432))
