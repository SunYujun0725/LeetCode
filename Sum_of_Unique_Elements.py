'''
Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
Date: 2024-02-20 00:36:01
LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
LastEditTime: 2024-02-22 00:58:18
FilePath: /vscode_cpp_for_Mac-master/Sum_of_Unique_Elements.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        uniqe = []
        repeat = []
        ans = 0
        for i in range(len(nums)):
            if nums[i] in uniqe:
                repeat.append(nums[i])
                uniqe.remove(nums[i])
                ans -= nums[i]
            elif nums[i] not in repeat:
                uniqe.append(nums[i])
                ans += nums[i]

        return ans