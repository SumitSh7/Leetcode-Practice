class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        arrmap = {}

        for i, j in enumerate(nums):

            value = target - nums[i]
            if(value in arrmap):
                return (arrmap[value], i)
            
            arrmap[j] = i
        
        return []


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([3, 2, 4], 6))
    print(sol.twoSum([3, 3], 6))
    print(sol.twoSum([2,7,11,15], 9))


        
