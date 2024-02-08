class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cmp = -101
        count = 0
        new_nums = []
        for i in range(len(nums)):
            if nums[i] != cmp:
                count += 1
                cmp = nums[i]
                new_nums.append(nums[i])
        nums.clear()
        for i in range(len(new_nums)):
            nums.append(new_nums[i])
        return count