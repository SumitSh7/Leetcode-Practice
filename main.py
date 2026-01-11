class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        arrmap = {}

        for i, j in enumerate(nums):
            if(target - nums[i] in arrmap):
                return arrmap[i], i
            
            arrmap[j] = i
        
        return []


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([3, 2, 4], 6))

        
