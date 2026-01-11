class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        arrmap = {}

        for i, j in len(nums):
            if(target - nums[i] in arrmap):
                return arrmap[j], i
            
            else:
                arrmap[j] = i
                target = target - nums[i]




        




