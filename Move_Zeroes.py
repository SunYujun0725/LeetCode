class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = len(nums)
        i = 0
        while i < count:
            if nums[i] == 0:
                nums.append(0)
                del nums[i]
                count -= 1
            else:
                i += 1