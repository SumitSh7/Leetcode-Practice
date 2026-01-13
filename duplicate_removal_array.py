class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        # if not nums:
        #     return []
        #
        # nums2 = [nums[0]]
        #
        # for i in range(1, len(nums)):
        #     if nums[i] != nums2[-1]:
        #         nums2.append(nums[i])
        #
        # return nums2, len(nums2)

        if not nums:
            return []
        
        upd = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[upd] = nums[i]
                upd += 1

        print(f"Number of unique elements: {upd}")
        print(f"Modified array: {nums[:upd]}") 
        return upd     


if __name__ == "__main__":
    sol = Solution()
    sol.removeDuplicates([1,1,2,2,3,3,3,4,4,5])

