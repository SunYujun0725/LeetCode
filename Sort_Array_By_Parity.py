class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = []
        even = []
        for i in range(len(nums)):
            if nums[i]%2 != 0:
                even.append(nums[i])
            else:
                ans.append(nums[i])
        
        for i in range(len(even)):
            ans.append(even[i])
        
        return ans