class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        # My linear search solution
        # if not nums:
        #     return 0
        # 
        # for i in range(len(nums)):
        #     if nums[i] >= target:
        #         return i
        # 
        # return len(nums)

        left = 0
        right = len(nums) - 1
        
        #Binary Search

        while left <= right:

            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid  # Found the exact target at midpoint
            elif nums[mid] < target:
                left = mid + 1  # Target is in the right half
            else:
                right = mid - 1 # Target is in the left half
                
        return left
            
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1,3,5,6], 5))   #2
    print(sol.searchInsert([1,3,5,6], 2))   #1
    print(sol.searchInsert([1,3,5,6], 7))   #None <--
    print(sol.searchInsert([], 7))          #0
