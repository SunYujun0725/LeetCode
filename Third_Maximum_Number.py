class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        cmp_num = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if cmp_num != nums[i]:
                cmp_num = nums[i]
                count += 1
            if count == 3:
                return nums[i]
        
        return nums[0]